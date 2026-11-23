# Quellen und Lizenzen

Dieses Projekt erstellt eine automatisch aktualisierte DNS-Blockliste für FRITZ!Box-Router.

## Verwendete Filterlisten

### HaGeZi DNS Blocklists
- Projekt: https://github.com/hagezi/dns-blocklists
- Lizenz: GPL-3.0
- Listen: Ultimate, TIF Medium, NSFW

### OISD
- Projekt: https://oisd.nl/
- Liste: NSFW
- Lizenz: GPL-3.0 gemäß den Angaben des Projekts

### Perflyst PiHoleBlocklist
- Projekt: https://github.com/Perflyst/PiHoleBlocklist
- Liste: AmazonFireTV.txt
- Lizenz: MIT
- Lizenztext: [MIT-Perflyst.txt](LICENSES/MIT-Perflyst.txt)

## Verarbeitung

Die Listen werden automatisch heruntergeladen und zusammengeführt.

Dabei werden:
- Doppelte Domains entfernt
- Ungültige Einträge verworfen
- Redundante Subdomains entfernt

Die erzeugte Liste ist eine veränderte Zusammenstellung der genannten Quellen.

## Lizenzhinweise

Die ursprünglichen Urheberrechte bleiben bestehen.

Die GPL-3.0-Lizenz ist in [LICENSE](LICENSE) dokumentiert. Der MIT-Lizenztext von Perflyst befindet sich unter [LICENSES/MIT-Perflyst.txt](LICENSES/MIT-Perflyst.txt).

Die Nutzung und Weiterverbreitung unterliegen den jeweiligen Lizenzbedingungen.
