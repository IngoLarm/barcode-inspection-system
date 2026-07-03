# Kombi-Inspektionssystem: Loch + Barcode

Automatisches Kamerasystem zur gleichzeitigen Loch- und Barcode-Verifikation auf laufenden Bahnen.

## Überblick

- **Bahnen:** 6–8 parallele Bahnen, synchron laufend
- **Geschwindigkeit:** 49 m/min (max. 120 m/min bei 50 µs LED-Blitz)
- **Barcodes:** 4× ITF (Interleaved 2/5) pro Bahn, 24,2 × 10,5 mm
- **Löcher:** 3 mm, Positions- und Größenkontrolle
- **Verifikation:** Barcode ↔ OCR-Klartext, Loch-Sequenz, Fehlende-Loch-Erkennung
- **Protokoll:** Zentrale SQLite-Datenbank auf Pi5 #5 via MQTT

## Systemarchitektur

```
Encoder (Bahnposition) ──► CM5 (Positionszähler)
                              │
OPB917 #1 (Loch-Trigger) ───►┤
OPB917 #2 (Barcode-Trigger) ►┤
                              │
                    ┌─────────▼─────────┐
                    │   CM5 #1..4       │
                    │                   │
  Kamera 1 (Loch) ──►  Loch-Auswertung │
  Kamera 2 (BC)   ──►  Barcode + OCR   │
                    │  Sequenzprüfung   │
                    └─────────┬─────────┘
                              │ LAN (MQTT)
                    ┌─────────▼─────────┐
                    │   Pi5 #5 Server   │
                    │   SQLite + SSD    │
                    └───────────────────┘
```

4 CM5-Einheiten, je 2 Bahnen → 8 Bahnen gesamt.

## Inspektionsfunktionen

| Funktion | Methode | Hardware |
|---------|---------|---------|
| Loch vorhanden? | Encoder + OPB917 #1 Fenster | OPB917 + Encoder |
| Lochposition | Encoder-Versatz zum Soll | Encoder |
| Lochgröße | Blob-Messung | Kamera 1 + OpenCV |
| Lochform / Qualität | Konturanalyse | Kamera 1 + OpenCV |
| Barcode lesen | pyzbar (ITF) | Kamera 2 |
| Klartext OCR | Tesseract (Arial, Ziffern) | Kamera 2 + Pi5 CPU |
| Barcode ↔ OCR Vergleich | String-Vergleich | Pi5 CPU |
| Sequenzprüfung | fortlaufende Nummer | Pi5 CPU |
| Protokollierung | MQTT → SQLite | Pi5 #5 Server |

## Hardware je Einheit (2 Bahnen)

| Komponente | Details |
|-----------|---------|
| Prozessor | Raspberry Pi CM5 Lite 4GB |
| Kamera 1 (Loch) | Innomaker OV9281 Global Shutter Mono, 309 fps |
| Kamera 2 (Barcode) | Innomaker OV9281 Global Shutter Mono, 309 fps |
| Loch-Trigger | OPB917BZ Lichtschranke #1 |
| Barcode-Trigger | OPB917BZ Lichtschranke #2 |
| Beleuchtung | LED-Blitz Eigenbau (IRLZ44N, 50 µs Pulse) |

## Gemeinsame Hardware

| Komponente | Menge | Details |
|-----------|-------|---------|
| Encoder | 1 | Bahnpositions-Referenz, gemeinsam |
| Pi5 #5 Server | 1 | MQTT-Broker + SQLite auf SSD |
| Gigabit-Switch | 1 | LAN alle Einheiten |

## Reserve

Hailo-8L AI HAT+ (4×, nachrüstbar) — falls Pi5 CPU für OCR nicht ausreicht. HAT-Stecker am CM5-Träger bleibt frei. Pi5 CPU verarbeitet ~12 ms / Label (4 Kerne parallel), bei 52,7 ms verfügbarer Zeit bei 49 m/min kein Engpass.

## Software-Stack

- **Bilderfassung:** libcamera / Picamera2
- **Barcode:** pyzbar (ITF)
- **OCR:** Tesseract (Arial-Whitelist, psm 7)
- **Loch-Auswertung:** OpenCV blob detection
- **Kommunikation:** MQTT (Mosquitto)
- **Datenbank:** SQLite

## Dokumentation

- [LED_Blitz_Barcode_Scanner.pdf](LED_Blitz_Barcode_Scanner.pdf) — Systemdokumentation (Schaltung, Architektur, Stückliste, Kombi-Kapitel)
- [EINKAUFSLISTE.md](EINKAUFSLISTE.md) — Stückliste mit Preisen

## Status

Konzeptphase — Planung abgeschlossen, Implementierung ausstehend.
