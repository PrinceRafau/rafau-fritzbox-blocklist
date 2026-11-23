#!/usr/bin/env python3
"""Modified grouped DNS lists. HaGeZi: GPL-3.0; Perflyst: MIT.
See SOURCES.md and LICENSES for attribution. Python 3.9+.
"""
import re
import urllib.request
from pathlib import Path
import os
import tempfile

HERE = Path(__file__).resolve().parent
BASE = 'https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/'
SOURCES = {
    'fakeshops': [BASE+'fake-onlydomains.txt'],
    'malware': [BASE+'tif.medium-onlydomains.txt'],
    'nsfw': [BASE+'nsfw-onlydomains.txt'],
    'firetv': ['https://perflyst.github.io/PiHoleBlocklist/AmazonFireTV.txt'],
    'gambling': [BASE+'gambling.mini-onlydomains.txt'],
    'ads_tracking': [BASE+'light-onlydomains.txt'],
    'aggressive': [BASE+'ultimate-onlydomains.txt'],
}
SOCIAL = {'analytics.facebook.com','pixel.facebook.com','analytics.tiktok.com',
          'analytics.twitter.com','ads-twitter.com','tr.snapchat.com',
          'ct.pinterest.com','analytics.pinterest.com','px.ads.linkedin.com'}
DOMAIN = re.compile(r'(?i)^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$')
def parse(text):
    out = set()
    for line in text.splitlines():
        line = line.strip().lstrip('\ufeff').split('#',1)[0].strip()
        if line.startswith('||') and line.endswith('^'): line = line[2:-1]
        parts = line.split()
        if len(parts)==2 and parts[0] in ('0.0.0.0','127.0.0.1','::'): line=parts[1]
        line=line.lower().rstrip('.')
        if DOMAIN.fullmatch(line) and not line.rsplit('.',1)[-1].isdigit(): out.add(line)
    return out

def covered(d, rules):
    labels=d.split('.')
    return any('.'.join(labels[i:]) in rules for i in range(len(labels)-1))

def main():
    groups={}
    for name, urls in SOURCES.items():
        domains=set()
        for url in urls:
            print('Lade',name,url,flush=True)
            req=urllib.request.Request(url,headers={'User-Agent':'FritzboxFilterBuilder/2.0'})
            with urllib.request.urlopen(req,timeout=120) as r: data=r.read(100*1024*1024+1)
            if len(data)>100*1024*1024: raise RuntimeError('Datei zu gross')
            parsed=parse(data.decode('utf-8-sig'))
            if len(parsed)<(5 if name=='firetv' else 50): raise RuntimeError(f'{name}: zu wenige Domains')
            domains.update(parsed)
        groups[name]=domains
    groups['social_media']=SOCIAL.copy()
    local=HERE/'eigene_blacklist.txt'
    if local.exists(): groups['ads_tracking'].update(parse(local.read_text(encoding='utf-8')))
    allow=HERE/'allowlist.txt'
    exceptions=parse(allow.read_text(encoding='utf-8')) if allow.exists() else set()
    parents=set()
    for d in exceptions:
        labels=d.split('.')
        parents.update('.'.join(labels[i:]) for i in range(len(labels)-1))
    seen=set(); outputs={}
    for name in ('fakeshops','malware','nsfw','firetv','gambling','social_media','ads_tracking','aggressive'):
        rules={d for d in groups[name] if d not in parents and not covered(d,exceptions) and not covered(d,seen)}
        # Keep subdomains: FRITZ!OS matching semantics must be tested separately.
        seen.update(rules)
        outputs[name]='\n'.join(sorted(rules))+'\n' if rules else ''
        print(name,len(rules))
    for name,data in outputs.items():
        fd,tmp=tempfile.mkstemp(dir=HERE)
        try:
            with os.fdopen(fd,'w',encoding='utf-8',newline='\n') as f: f.write(data)
            os.replace(tmp,HERE/(name+'.txt'))
        finally:
            if os.path.exists(tmp): os.unlink(tmp)
if __name__=='__main__': main()
