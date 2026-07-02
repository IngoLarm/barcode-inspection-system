# 8-Bahn Barcode-Inspektionssystem

Automatisches Kamerasystem zur Erfassung und Verifikation von Interleaved-2/5-Barcodes auf laufenden Bahnen.

## Überblick

- **Bahnen:** 6–8 parallele Bahnen, synchron laufend
- **Geschwindigkeit:** 49 m/min
- **Barcodes:** 4× ITF (Interleaved 2/5) pro Bahn, 24,2 × 10,5 mm
- **Verifikation:** Barcode-Inhalt wird mit aufgedrucktem Klartext (OCR) verglichen
- **Protokoll:** Zentrale SQLite-Datenbank auf Pi5 #5 via MQTT

## Hardware

| Komponente | Details |
|-----------|---------|
| Kamera-Einheit | Raspberry Pi CM5 + Hailo-8L AI HAT+ (13 TOPS) |
| Kamera | 2× Raspberry Pi Global Shutter Camera (IMX296) |
| Trigger | OPB917BZ Lichtschranke |
| Beleuchtung | LED-Blitz Eigenbau (IRLZ44N, 50–100 µs) |
| Server | Raspberry Pi 5 + SSD |
| Netzwerk | Gigabit-Switch (5-Port) |

## Systemarchitektur

```
OPB917BZ (gemeinsamer Trigger)
    │
    ├── CM5 #1  (Bahn 1 + 2)  ──┐
    ├── CM5 #2  (Bahn 3 + 4)  ──┤
    ├── CM5 #3  (Bahn 5 + 6)  ──┤── LAN-Switch ── Pi5 #5 (Server + SSD)
    └── CM5 #4  (Bahn 7 + 8)  ──┘
```

## Software-Stack

- **Bilderfassung:** libcamera / Picamera2
- **Barcode:** pyzbar (ITF)
- **OCR:** CRNN / PaddleOCR auf Hailo-8L
- **Kommunikation:** MQTT (Mosquitto)
- **Datenbank:** SQLite

## Dokumentation

- [LED_Blitz_Barcode_Scanner.pdf](LED_Blitz_Barcode_Scanner.pdf) — Systemdokumentation (Schaltung, Architektur, Stückliste)

## Status

Konzeptphase — Planung abgeschlossen, Implementierung ausstehend.
