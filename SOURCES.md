# Quellen und Lizenzen

Dieses Projekt erstellt automatisch aktualisierte, kategorisierte DNS-Filterlisten für FRITZ!Box-Router.

## 1. HaGeZi DNS Blocklists

- Urheber: HaGeZi
- Projekt: https://github.com/hagezi/dns-blocklists
- Lizenz: GNU General Public License v3.0 (GPL-3.0)
- Lizenztext: https://github.com/hagezi/dns-blocklists/blob/main/LICENSE

### Verwendete Listen

| Originaldatei | Erzeugte Filterdatei |
|---|---|
| tif.medium-onlydomains.txt | malware.txt |
| fake-onlydomains.txt | fakeshops.txt |
| nsfw-onlydomains.txt | nsfw.txt |
| gambling.mini-onlydomains.txt | gambling.txt |
| light-onlydomains.txt | ads_tracking.txt |
| ultimate-onlydomains.txt | aggressive.txt |

Die Originaldateien werden über das jsDelivr-CDN bezogen.

## 2. Perflyst PiHoleBlocklist

- Urheber: Perflyst und Mitwirkende
- Projekt: https://github.com/Perflyst/PiHoleBlocklist
- Lizenz: MIT
- Originaldatei: AmazonFireTV.txt
- Quelle: https://perflyst.github.io/PiHoleBlocklist/AmazonFireTV.txt
- Erzeugte Filterdatei: firetv.txt
- Lizenztext: [MIT-Perflyst.txt](LICENSES/MIT-Perflyst.txt)

## 3. Social Media

Die Datei social_media.txt basiert auf einer manuell zusammengestellten Auswahl von Tracking-Domains folgender Dienste:

- Facebook
- TikTok
- X (Twitter)
- Snapchat
- Pinterest
- LinkedIn

Die Liste dient der Reduzierung von Tracking und soll soziale Netzwerke nicht vollständig sperren.

## 4. Verarbeitung und Änderungen

Die Originalfilterlisten werden durch dieses Projekt verändert und neu zusammengestellt.

Die Verarbeitung umfasst:

- Automatisches Herunterladen der Quelldateien
- Normalisierung der Domainnamen
- Entfernung ungültiger Einträge
- Gruppenübergreifende Duplikatbereinigung
- Berücksichtigung übergeordneter Domains
- Berücksichtigung individueller Ausnahmen
- Aufteilung in separate Filtergruppen
- Regelmäßige automatische Aktualisierung

Der zur Verarbeitung verwendete Python-Quellcode ist öffentlich verfügbar.

## 5. Lizenzinformationen

Die ursprünglichen Urheberrechte und Lizenzbedingungen der verwendeten Quellen bleiben bestehen.

- [GPL-3.0](LICENSE)
- [MIT-Lizenz von Perflyst](LICENSES/MIT-Perflyst.txt)
- [Python-Quellcode](fritzbox_filter_builder.py)

Die veröffentlichten Filterdateien sind bearbeitete Zusammenstellungen und keine unveränderten Kopien der Originalfilterlisten.

## 6. Frühere Quellen

In früheren Versionen dieses Projekts wurde zusätzlich OISD NSFW verwendet.

- Projekt: https://oisd.nl/

OISD ist nicht mehr Bestandteil des aktuellen Filtergenerators.

## 7. Haftungsausschluss

Alle Filterlisten werden ohne Gewähr bereitgestellt. Fehlklassifizierungen, unvollständige Sperren und Funktionsbeeinträchtigungen sind möglich.

Dieses Projekt steht in keiner offiziellen Verbindung zu den genannten Quellen oder Unternehmen.
