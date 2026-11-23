#!/usr/bin/env python3
"""Erzeugt eine deduplizierte FRITZ!Box-Domainliste. Python 3.9+, keine Pakete nötig.
Aufruf: python3 fritzbox_filter_builder.py
Optional: lokale Domains in eigene_blacklist.txt (eine Domain pro Zeile).
Optional: explizite Ausnahmen in allowlist.txt (eine Domain pro Zeile).
"""
import ipaddress
import os
import re
import tempfile
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'fritzbox_blocklist.txt'
SOURCES = {
    'HaGeZi Ultimate': 'https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/ultimate-onlydomains.txt',
    'HaGeZi TIF Medium': 'https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/tif.medium-onlydomains.txt',
    'HaGeZi NSFW': 'https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/nsfw-onlydomains.txt',
    'OISD NSFW': 'https://nsfw.oisd.nl/',
    'Fire TV': 'https://perflyst.github.io/PiHoleBlocklist/AmazonFireTV.txt',
}
# Facebook-Domains NICHT pauschal freigeben: erst nach konkreten Funktionsproblemen.
DOMAIN = re.compile(r'(?i)^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z](?:[a-z0-9-]{0,61}[a-z0-9])?$')

def normalize(line):
    line = line.strip().lstrip('\ufeff')
    if not line or line.startswith(('#', '!', '[', ';')):
        return None
    line = line.split('#', 1)[0].strip()
    if not line or line.startswith('@@') or '$' in line or '/' in line and not line.startswith('||'):
        return None
    if line.startswith('||'):
        line = line[2:].split('^', 1)[0]
    elif line.startswith('|') or '*' in line or '^' in line:
        return None
    parts = line.split()
    if len(parts) > 1:
        try:
            ipaddress.ip_address(parts[0])
        except ValueError:
            return None
        if len(parts) != 2:
            return None
        line = parts[1]
    line = line.lower().rstrip('.')
    if line in {'localhost', 'local', 'broadcasthost'} or not DOMAIN.fullmatch(line):
        return None
    return line

def load_local(path):
    if not path.exists():
        return set()
    return {d for line in path.read_text(encoding='utf-8').splitlines() if (d := normalize(line))}

def compress(domains):
    # Entfernt Subdomains NUR, wenn die übergeordnete Domain tatsächlich gesperrt ist.
    # Funktioniert für DNS-Filter, die auch Subdomains einer gesperrten Domain erfassen.
    result = set()
    for domain in sorted(domains, key=lambda d: (d.count('.'), d)):
        labels = domain.split('.')
        if not any('.'.join(labels[i:]) in result for i in range(1, len(labels) - 1)):
            result.add(domain)
    return result

def main():
    all_domains = set()
    for name, url in SOURCES.items():
        print('Lade', name, flush=True)
        request = urllib.request.Request(url, headers={'User-Agent': 'FritzboxFilterBuilder/1.0'})
        with urllib.request.urlopen(request, timeout=90) as response:
            payload = response.read(100 * 1024 * 1024 + 1)
        if len(payload) > 100 * 1024 * 1024:
            raise RuntimeError(f'{name}: Datei zu groß')
        lines = payload.decode('utf-8-sig').splitlines()
        parsed = {d for line in lines if (d := normalize(line))}
        if len(parsed) < 50:
            raise RuntimeError(f'{name}: verdächtig wenige Domains ({len(parsed)}), Abbruch')
        print(f'  {len(parsed):,} gültige Domains')
        all_domains.update(parsed)
    all_domains.update(load_local(HERE / 'eigene_blacklist.txt'))
    allow = load_local(HERE / 'allowlist.txt')
    # Ausnahmen haben Vorrang; wenn eine übergeordnete Domain geblockt bleibt,
    # kann eine Ausnahmesubdomain je nach FRITZ!OS trotzdem gesperrt sein.
    all_domains.difference_update(allow)
    reduced = compress(all_domains)
    # Keine unabsichtliche vollständige Liste mit nur wenigen Domains veröffentlichen.
    if len(reduced) < 1000:
        raise RuntimeError('Ergebnis ungewöhnlich klein; bestehende Liste bleibt unverändert')
    data = ('\n'.join(sorted(reduced)) + '\n').encode('utf-8')
    fd, temp = tempfile.mkstemp(prefix='.fritzbox-', suffix='.tmp', dir=HERE)
    try:
        with os.fdopen(fd, 'wb') as f:
            f.write(data)
        os.replace(temp, OUT)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)
    print(f'Fertig: {len(reduced):,} Domains, {len(data):,} Bytes -> {OUT}')

if __name__ == '__main__':
    main()
