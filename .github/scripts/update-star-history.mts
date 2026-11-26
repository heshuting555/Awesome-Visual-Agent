import { writeFile } from "node:fs/promises";
import { join } from "node:path";
import { JSDOM } from "jsdom";
import XYChart from "../shared/packages/xy-chart";

const startDate = "2026-11-20";
const dayMs = 24 * 60 * 60 * 1000;
const start = Date.parse(startDate);
const today = Math.floor(Date.now() / dayMs) * dayMs;
const outputDirectory = process.argv[2];
const repository = process.env.GITHUB_REPOSITORY;
if (!outputDirectory || !repository) {
    throw new Error("Set GITHUB_REPOSITORY and pass the chart output directory.");
}

const headers = new Headers({
    "Accept": "application/vnd.github+json",
    "User-Agent": "visual-agent-star-history",
    "X-GitHub-Api-Version": "2026-03-10",
});
if (process.env.GITHUB_TOKEN) {
    headers.set("Authorization", "Bearer " + process.env.GITHUB_TOKEN);
}

interface StarWeek {
    week: number;
    days: number[];
}

const daily = new Map<number, number>();
const api = "https://api.github.com/repos/" + repository + "/stargazers/history";
for (let page = 1; !daily.has(start); page++) {
    const response = await fetch(api + "?per_page=30&page=" + page, {
        headers,
        signal: AbortSignal.timeout(20_000),
    });
    if (!response.ok) {
        throw new Error("GitHub star history returned HTTP " + response.status);
    }
    const weeks: StarWeek[] = await response.json();
    for (const week of weeks) {
        if (!Number.isSafeInteger(week.week) || week.days.length !== 7 ||
            !week.days.every((count) => Number.isSafeInteger(count) && count >= 0)) {
            throw new Error("GitHub returned invalid weekly Star counts.");
        }
        const sunday = Math.floor(week.week * 1000 / dayMs) * dayMs;
        week.days.forEach((count, offset) => daily.set(sunday + offset * dayMs, count));
    }
    if (!response.headers.get("link")?.includes('rel="next"')) {
        break;
    }
}

let total = 0;
const points = [];
for (let day = start; day <= today; day += dayMs) {
    const count = daily.get(day);
    if (count === undefined) {
        // The API can omit the latest day until its aggregate is available.
        if (day === today && points.length) break;
        throw new Error("Missing Star history for " + new Date(day).toISOString().slice(0, 10));
    }
    total += count;
    points.push({ x: new Date(day), y: total });
}
if (points.length < 2) {
    throw new Error("Too little Star history to draw the chart.");
}
const lastDate = points.at(-1)!.x.toISOString().slice(0, 10);

const avatarResponse = await fetch("https://github.com/" + repository.split("/")[0] + ".png?size=96", {
    signal: AbortSignal.timeout(15_000),
});
const imageType = avatarResponse.headers.get("content-type");
const logo = avatarResponse.ok && imageType?.startsWith("image/")
    ? "data:" + imageType + ";base64," + Buffer.from(await avatarResponse.arrayBuffer()).toString("base64")
    : "";
const format = new Intl.DateTimeFormat("en-US", points.length < 120
    ? { month: "short", day: "numeric", timeZone: "UTC" }
    : { month: "short", year: "numeric", timeZone: "UTC" });

const svgNamespace = "http://www.w3.org/2000/svg";
for (const theme of ["light", "dark"] as const) {
    const dom = new JSDOM("<!doctype html><body></body>");
    const document = dom.window.document;
    const svg = document.createElementNS(svgNamespace, "svg");
    svg.setAttribute("xmlns", svgNamespace);
    svg.setAttribute("width", "800");
    document.body.append(svg);
    XYChart(svg, {
        title: "Star History",
        xLabel: "Date",
        yLabel: "GitHub Stars Added",
        data: { datasets: [{ label: repository, logo, data: points.map((point) => ({ ...point })) }] },
        showDots: false,
        transparent: false,
        theme,
    }, { xTickLabelType: "Date", legendPosition: "bottom-right" });

    for (const tick of svg.querySelectorAll(".xaxis .tick")) {
        const label = tick.querySelector("text");
        const date = (tick as unknown as { __data__: Date }).__data__;
        if (label && date) label.textContent = format.format(date);
    }
    const description = document.createElementNS(svgNamespace, "desc");
    description.textContent = repository + " added " + total + " stars from " + startDate + " through " + lastDate + ".";
    svg.prepend(description);

    const suffix = theme === "dark" ? "-dark" : "";
    await writeFile(join(outputDirectory, "star-history-since-" + startDate + suffix + ".svg"), svg.outerHTML + "\n");
    dom.window.close();
}
console.log("Updated both charts with " + total + " stars through " + lastDate + ".");
