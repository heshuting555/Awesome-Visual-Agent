"""Small brace-aware BibTeX reader and display/venue helpers (standard library)."""
import hashlib
import re
import unicodedata

def strip_comments(s):
 return re.sub(r'(?m)(?<!\\)%[^\n]*','',s)

def split_top(s, sep=','):
 out=[]; start=0; level=0; quote=False; escape=False
 for i,c in enumerate(s):
  if escape: escape=False; continue
  if c=='\\': escape=True; continue
  if c=='"' and level==0: quote=not quote
  if not quote:
   if c=='{': level+=1
   if c=='}': level-=1
   if c==sep and level==0: out.append(s[start:i]); start=i+1
 out.append(s[start:]); return out

def parse(path, recover=False):
 raw=path.read_text(encoding='utf-8'); recovered=[]
 if recover:
  recovered=re.findall(r'(?m)^%\s*(@\w+\s*[({]\s*[^,]+,)',raw)
  raw=re.sub(r'(?m)^%\s*(@\w+\s*[({])',r'\1',raw)
 s=strip_comments(raw); out=[]; strings=[]; errors=[]; pos=0
 while m:=re.search(r'@(\w+)\s*([({])',s[pos:]):
  start=pos+m.start(); typ=m[1].lower(); op=m[2]; a=pos+m.end(); depth=1; quote=False; escape=False; i=a
  while i<len(s):
   c=s[i]
   if escape: escape=False
   elif c=='\\': escape=True
   elif c=='"' and (op=='(' or depth==1): quote=not quote
   elif not quote:
    if c==op: depth+=1
    if c==('}' if op=='{' else ')'): depth-=1
   if depth==0: break
   i+=1
  if depth: errors.append(f'unclosed entry at {start}'); break
  body=s[a:i]; pos=i+1
  if typ in ('comment','preamble'): continue
  if typ=='string': strings.append(body.strip()); continue
  parts=split_top(body); key=parts[0].strip(); fields={}
  for part in parts[1:]:
   if not part.strip(): continue
   fm=re.match(r'\s*(\w+)\s*=\s*([\s\S]+)',part)
   if not fm: errors.append(f'{key}: malformed field {part[:70]}'); continue
   name=fm[1].lower(); val=fm[2].strip()
   if name in fields: errors.append(f'{key}: repeated field {name}')
   fields[name]=val
  out.append(dict(type=typ,key=key,fields=fields,source=path.name,line=s.count('\n',0,start)+1))
 return out,strings,errors,recovered

def bibliography_digest(path):
    """Hash the bibliography consistently across Git checkout line endings."""
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()

def norm(s):
 s=unicodedata.normalize('NFKD',s).lower()
 return re.sub(r'[^a-z0-9]','',s)

def plain(s):
 s=s.strip()
 return s[1:-1] if s and s[0] in '{"' else s


def tex_text(value):
    value = plain(value)
    value = re.sub(r'\\["\']\{?([A-Za-z])\}?', lambda m: unicodedata.normalize('NFC', m[1] + ('\u0308' if m[0][1] == '"' else '\u0301')), value)
    value = value.replace(r'\&', '&').replace(r'\%', '%').replace(r'\_', '_')
    value = value.replace(r'\pi', 'π').replace(r'\textendash', '–')
    value = re.sub(r'\\(?:textit|textbf|mathrm|textrm|text)\s*', '', value)
    value = value.replace('K$^{2}$', 'K²').replace('$', '').replace('{', '').replace('}', '')
    return re.sub(r'\s+', ' ', value).strip()

def entry_venue(entry):
    fields = entry['fields']
    venue = tex_text(fields.get('booktitle', fields.get('journal', fields.get('xxxjournal', ''))))
    low = venue.lower()
    abbreviation = re.search(r'\((CVPR|ICCV|ECCV|ICLR|ICML|NeurIPS|ACL|EMNLP|NAACL|COLM|CoRL|RSS|ICRA|IROS|CHI|AAAI|ACM MM)\)', venue, re.I)
    if abbreviation:
        return {'neurips': 'NeurIPS', 'corl': 'CoRL'}.get(abbreviation[1].lower(), abbreviation[1].upper())
    if 'workshop' in low:
        if 'cvpr' in low: return 'CVPR Workshops'
        if 'corl' in low: return 'CoRL Workshops'
        return venue
    if 'arxiv' in low: return 'arXiv'
    if 'openreview preprint' in low: return 'OpenReview Preprint'
    if low in {'preprints', 'preprints.org'}: return 'Preprints.org'
    if 'lilianweng.github.io' in low: return 'Blog'
    mapping = [
        ('computer vision and pattern recognition', 'CVPR'),
        ('international conference on computer vision', 'ICCV'),
        ('european conference on computer vision', 'ECCV'),
        ('learning representations', 'ICLR'),
        ('machine learning', 'ICML'),
        ('neural information processing systems', 'NeurIPS'),
        ('aaai', 'AAAI'),
        ('european chapter of the association for computational linguistics', 'EACL'),
        ('nations of the americas chapter', 'NAACL'),
        ('association for computational linguistics', 'ACL'),
        ('empirical methods in natural language processing', 'EMNLP'),
        ('conference on robot learning', 'CoRL'),
        ('robotics: science and systems', 'RSS'),
        ('intelligent robots and systems', 'IROS'),
        ('robotics and automation (icra)', 'ICRA'),
        ('automation science and engineering', 'CASE'),
        ('pattern recognition', 'ICPR'),
        ('information retrieval', 'ECIR'),
        ('sigkdd', 'KDD'),
        ('acm international conference on multimedia', 'ACM MM'),
        ('artificial intelligence and statistics', 'AISTATS'),
        ('human factors in computing systems', 'CHI'),
        ('intelligent user interfaces', 'IUI'),
        ('pattern analysis and machine intelligence', 'TPAMI'),
        ('robotics and automation letters', 'RA-L'),
        ('geoscience and remote sensing', 'TGRS'),
    ]
    # Findings often abbreviate the conference in the source string.
    if 'findings' in low:
        for abbreviation in ('CVPR', 'NAACL', 'EMNLP', 'ACL'):
            if abbreviation.lower() in low or (abbreviation == 'CVPR' and 'computer vision and pattern recognition' in low):
                return abbreviation + ' Findings'
    for phrase, abbreviation in mapping:
        if phrase in low:
            if 'system demonstrations' in low: return abbreviation + ' Demos'
            if 'datasets and benchmarks' in low: return abbreviation + ' Datasets and Benchmarks'
            return abbreviation
    if low in {'cvpr', 'iccv', 'eccv', 'iclr', 'icml', 'acl', 'emnlp', 'rss', 'corl', 'icra', 'iros'}:
        return {'corl':'CoRL'}.get(low, low.upper())
    if low == 'artificial intelligence': return 'Artificial Intelligence'
    if low == 'neural networks': return 'Neural Networks'
    if not venue:
        if entry['type'] == 'misc': return 'Official Release'
        return 'Venue Unspecified'
    return venue


def arxiv_id(entry):
    fields = entry['fields']
    value = tex_text(fields.get('eprint', ''))
    match = re.search(r'\b(\d{4}\.\d{4,5})\b', value)
    if not match:
        value = ' '.join(tex_text(fields.get(field, '')) for field in
                         ('journal', 'xxxjournal', 'url', 'xxxurl', 'doi'))
        match = re.search(r'(?:arxiv(?:\.org/(?:abs|pdf)/|[\s:]+)|10\.48550/arxiv[.:])(\d{4}\.\d{4,5})', value, re.I)
    return match[1] if match else None


def venue(entry):
    result = entry_venue(entry)
    return 'arXiv' if result == 'Official Release' and arxiv_id(entry) else result
