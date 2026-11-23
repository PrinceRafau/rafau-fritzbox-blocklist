# Rafau FRITZ!Box DNS Blocklist

Kostenlose, automatisch aktualisierte DNS-Filterlisten für die FRITZ!Box.

Das Projekt kombiniert verschiedene DNS-Blocklisten und unterteilt diese in acht separat nutzbare Filtergruppen.

## Verfügbare Filterlisten

| Filterliste | Beschreibung |
|---|---|
| [malware.txt](malware.txt) | Malware, Phishing und Internetbedrohungen |
| [fakeshops.txt](fakeshops.txt) | Fakeshops, betrügerische Webseiten und Abofallen |
| [nsfw.txt](nsfw.txt) | Pornografie und XXX-Inhalte |
| [firetv.txt](firetv.txt) | Amazon-Fire-TV-Tracking und Telemetrie |
| [gambling.txt](gambling.txt) | Glücksspiel und Online-Casinos |
| [social_media.txt](social_media.txt) | Ausgewählte Social-Media-Tracker |
| [ads_tracking.txt](ads_tracking.txt) | Werbung und Tracking |
| [aggressive.txt](aggressive.txt) | Erweiterter, aggressiver Zusatzfilter |

## Direkte Download-Adressen

**Malware und Phishing**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/malware.txt

**Fakeshops**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/fakeshops.txt

**Pornografie und XXX**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/nsfw.txt

**Amazon Fire TV**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/firetv.txt

**Glücksspiel**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/gambling.txt

**Social Media**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/social_media.txt

**Werbung und Tracking**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/ads_tracking.txt

**Aggressiver Zusatzfilter**

https://raw.githubusercontent.com/PrinceRafau/rafau-fritzbox-blocklist/main/aggressive.txt

## Funktionen

- Automatische Aktualisierung über GitHub Actions
- Acht getrennte Filtergruppen
- Bereinigung ungültiger Einträge
- Gruppenübergreifende Duplikatbereinigung
- Berücksichtigung übergeordneter Domains
- Individuelle Ausnahmen über allowlist.txt
- Eigene Sperreinträge über eigene_blacklist.txt
- Keine zusätzlichen Python-Pakete erforderlich
- Kein eigener Webserver erforderlich

## Automatische Aktualisierung

Die Filterlisten werden regelmäßig über GitHub Actions aktualisiert.

Eine manuelle Aktualisierung ist ebenfalls über GitHub Actions möglich.

Das Aktualisierungsintervall der FRITZ!Box ist davon unabhängig.

## Empfohlene Verwendung

Die Filtergruppen sollten einzeln eingebunden und getestet werden.

Der aggressive Zusatzfilter ist optional und kann die Funktion einzelner Webseiten und Apps beeinträchtigen.

Der Social-Media-Filter soll Tracking reduzieren, ohne soziale Netzwerke pauschal zu sperren.

Durch die gruppenübergreifende Bereinigung können einzelne Gruppen bei alleiniger Verwendung einen geringeren Schutzumfang bieten.

## Quellen und Lizenzen

Dieses Projekt verwendet Filterlisten von HaGeZi und Perflyst sowie eine kleine, manuell zusammengestellte Social-Media-Liste.

Weitere Informationen:

- [Quellen und Lizenzinformationen](SOURCES.md)
- [GPL-3.0-Lizenz](LICENSE)
- [MIT-Lizenz von Perflyst](LICENSES/MIT-Perflyst.txt)

Die ursprünglichen Urheberrechte bleiben bestehen. Die veröffentlichten Filterlisten sind bearbeitete Zusammenstellungen der verwendeten Quellen.

## Haftungshinweis

Die Bereitstellung erfolgt ohne Gewähr.

Fehlerhafte Sperren und Einschränkungen einzelner Webseiten oder Dienste sind möglich.

Ein DNS-Filter bietet keinen vollständigen Schutz vor Schadsoftware, Betrug, unerwünschten Inhalten oder Tracking.

Dieses Projekt ist unabhängig und steht in keiner offiziellen Verbindung zu AVM, HaGeZi oder Perflyst.
