# Einkaufsliste — 8-Bahn Kombi-Inspektionssystem (Loch + Barcode)

Gesamtsystem: 4 CM5-Einheiten (je 2 Bahnen) + 1 Protokoll-Server

---

## Hauptkomponenten

| Pos | Bezeichnung | Menge | Stückpreis | Gesamt | Bezug |
|-----|-------------|-------|-----------|--------|-------|
| 1 | Raspberry Pi CM5 Lite 4GB | 4 | 45,00 € | 180,00 € | Reichelt / RS Components |
| 2 | Innomaker OV9281 Global Shutter Kamera | 8 | 30,00 € | 240,00 € | Amazon |
| 3 | Raspberry Pi 5 (8GB, Protokoll-Server) | 1 | 80,00 € | 80,00 € | Reichelt |
| 4 | SSD 256GB USB3 (z.B. Samsung T7) | 1 | 35,00 € | 35,00 € | Amazon |
| 5 | Gigabit-Switch 5-Port | 1 | 20,00 € | 20,00 € | Amazon |
| 6 | CM5-IO-Board oder Trägerplatine | 4 | 25,00 € | 100,00 € | Raspberry Pi |
| | **Zwischensumme Hauptkomponenten** | | | **655,00 €** | |

> **Kein Hailo-8L nötig:** Pi 5 CPU (4× Cortex-A76) verarbeitet alle 8 Barcodes + OCR
> parallel in ~12 ms — bei 52,7 ms verfügbarer Zeit bleibt 40 ms Reserve.
>
> **Hailo-8L in der Hinterhand:** Der HAT-Stecker am CM5 bleibt frei. Falls Tesseract
> in der Praxis zu langsam sein sollte, kann der Hailo-8L ohne Hardware-Umbau
> aufgesteckt und die OCR-Pipeline auf CRNN umgestellt werden.

---

## Optik (M12-Objektive)

Je nach gewünschtem Arbeitsabstand — nur eine Variante wählen:

| Pos | Brennweite | Arbeitsabstand | Menge | Stückpreis | Gesamt | Bezug |
|-----|-----------|---------------|-------|-----------|--------|-------|
| 8a | M12 Objektiv 4mm f/2.0 | 42 mm | 8 | 8,00 € | 64,00 € | AliExpress / Amazon |
| 8b | M12 Objektiv 6mm f/2.0 | 63 mm | 8 | 8,00 € | 64,00 € | AliExpress / Amazon |
| 8c | M12 Objektiv 8mm f/2.0 | 83 mm | 8 | 8,00 € | 64,00 € | AliExpress / Amazon |

---

## LED-Blitz (je CM5-Einheit × 4)

| Pos | Bezeichnung | Menge | Stückpreis | Gesamt | Bezug |
|-----|-------------|-------|-----------|--------|-------|
| 9 | 3W High-Power LED weiß (Star PCB) | 16 | 1,00 € | 16,00 € | Reichelt / Amazon |
| 10 | Kühlkörper für Star-LED (40×40mm) | 16 | 0,80 € | 12,80 € | Amazon / Conrad |
| 11 | IRLZ44N MOSFET (Logic-Level) | 4 | 0,60 € | 2,40 € | Reichelt |
| 12 | Elko 1000µF / 25V | 4 | 0,40 € | 1,60 € | Reichelt |
| 13 | Widerstand 10 Ω / 0,25W (Gate) | 4 | 0,10 € | 0,40 € | Reichelt |
| 14 | Widerstand 2,2 Ω / 2W (Strom, je Strang) | 8 | 0,30 € | 2,40 € | Reichelt |
| 15 | Diode 1N4007 | 4 | 0,10 € | 0,40 € | Reichelt |
| | **Zwischensumme LED-Blitz** | | | **36,00 €** | |

> **Pos. 14 auf 8 Stück:** 4 LEDs in Reihe bei 12V hätten kaum Spannungsreserve für den
> Vorwiderstand (Vf-Summe zu nah an 12V → Strom driftet unkontrolliert). Stattdessen
> **2 Stränge à 2 LEDs in Reihe, parallel**, jeder Strang mit eigenem 2,2Ω-Widerstand
> (Details siehe unten). Ein gemeinsamer IRLZ44N schaltet beide Stränge (4,2A Pulsstrom
> gesamt — für den MOSFET unkritisch).

---

## Trigger-Schaltung & Encoder

| Pos | Bezeichnung | Menge | Stückpreis | Gesamt | Bezug |
|-----|-------------|-------|-----------|--------|-------|
| 16 | OPB917BZ Lichtschranke #1 (Loch-Trigger) | 1 | 5,00 € | 5,00 € | Mouser / DigiKey |
| 17 | OPB917BZ Lichtschranke #2 (Barcode-Trigger) | 1 | 5,00 € | 5,00 € | Mouser / DigiKey |
| 18 | Inkremental-Encoder (gemeinsam) | 1 | 15,00 € | 15,00 € | Reichelt / Conrad |
| 19 | BC849 NPN-Transistor (SOT-23) | 5 | 0,10 € | 0,50 € | Reichelt |
| 20 | Widerstand 560 Ω / 0603 | 5 | 0,05 € | 0,25 € | Reichelt |
| 21 | Widerstand 100 kΩ / 0603 | 5 | 0,05 € | 0,25 € | Reichelt |
| 22 | Widerstand 10 kΩ / 0603 | 5 | 0,05 € | 0,25 € | Reichelt |
| | **Zwischensumme Trigger + Encoder** | | | **26,25 €** | |

> **OPB917 #1** — Loch-Trigger: direkt an den 3mm Löchern, löst Kamera 1 + LED-Blitz aus.
> **OPB917 #2** — Barcode-Trigger: vor dem Barcodefeld, löst Kamera 2 + LED-Blitz aus.
> **Encoder** — liefert Bahnposition für Fehlende-Loch-Erkennung (Toleranzfenster ±0,5mm).

---

## Netzwerk & Stromversorgung

| Pos | Bezeichnung | Menge | Stückpreis | Gesamt | Bezug |
|-----|-------------|-------|-----------|--------|-------|
| 21 | Netzkabel CAT6 (2m) | 6 | 3,00 € | 18,00 € | Amazon |
| 22 | Netzteil 12V / 5A (LED-Versorgung) | 4 | 12,00 € | 48,00 € | Amazon |
| 23 | USB-C Netzteil 27W (Pi5 / CM5) | 5 | 10,00 € | 50,00 € | Reichelt |
| | **Zwischensumme Versorgung** | | | **116,00 €** | |

---

## Gesamtkosten

| Kategorie | Betrag |
|-----------|--------|
| Hauptkomponenten (ohne Hailo) | 655,00 € |
| Optik (z.B. 6mm) | 64,00 € |
| LED-Blitz | 36,00 € |
| Trigger + Encoder | 26,25 € |
| Netzwerk & Strom | 116,00 € |
| **Gesamt (ca.)** | **~897,25 €** |
| Reserve +15% | **~1.032,00 €** |

> Preise sind Richtwerte (Stand 2026). CM5-Trägerplatine je nach Eigendesign oder Fertigplatine.
> **Hailo-8L aktuell nicht verbaut** (280 € gespart) — Pi 5 CPU reicht für Arial-Ziffern-OCR.
> **In der Hinterhand:** HAT-Stecker bleibt frei — Hailo-8L nachrüstbar ohne Hardware-Umbau.

---

## Beleuchtungsberechnung

### LED-Anordnung je CM5-Einheit

```
        Kamera
          │
  LED ────┼──── LED    ← 2 LEDs links/rechts, 30° zur Senkrechten
          │
      Barcode-Bereich
      (50mm × 25mm)
```

Alternativ (besser bei engem Einbauraum):

```
  ┌─────────────────────┐
  │  LED  LED  LED  LED │  ← 4 LEDs in einer Reihe über der Kamera
  │        Kamera       │
  └─────────────────────┘
```

**Variante C (empfohlen): Ring direkt um das M12-Objektiv**

```
              LED
               │
      LED ── [ M12-Tubus ] ── LED     ← 4 LEDs im Kreis um das Objektiv,
               │                        dicht an der optischen Achse →
              LED                       kaum Schattenwurf, sehr kompakt
```

Elektrisch weiterhin als **2 Stränge à 2 LEDs in Reihe, parallel** (siehe Pos. 14):
z.B. oben+unten ein Strang, links+rechts der andere — welche zwei LEDs galvanisch
zusammenhängen ist für die Beleuchtung egal, da alle 4 gleichzeitig zünden.

```
12V ── Elko 1000µF ──┬── R1 (2,2Ω) ── LED ── LED ──┐
                      │                              ├── Drain │ IRLZ44N
                      └── R2 (2,2Ω) ── LED ── LED ──┘        Source → GND
```

> **Mechanischer Punkt (noch offen):** M12-Objektive haben ~14–16mm Tubusdurchmesser.
> 4× 20mm-Star-PCBs mit 40×40mm-Kühlkörper (Pos. 10) passen nicht überlappungsfrei
> direkt im Ring darum. Optionen: kleinere Kühlkörper (z.B. 20×20mm) dicht am Tubus,
> oder ein eigens gefertigter Ring-Kühlkörper (wie bei Kamera-Ringlichtern üblich).
> Noch nicht final entschieden — vor Bestellung der Kühlkörper klären.

### Berechnung (3W LED, 50mm Abstand, 30° Winkel, 3× Pulsstrom)


| Parameter | Wert |
|-----------|------|
| Nennlichtstrom je LED | 120 lm @ 700 mA |
| Pulsstrom (3× Overdrive) | 2100 mA |
| Lichtstrom im Puls | ~360 lm |
| Beleuchtungsstärke je LED | 39696 lux |
| 4 LEDs gesamt | **158783 lux** |
| Effektive Belichtung (50 µs) | 7939.14 mlux·s |
| Leuchtfleck-Radius (60° HWB) | 87 mm |

Zum Vergleich: Sonnenlicht = ~100.000 lux, gut beleuchtetes Büro = ~500 lux.
**158783 lux** mit 4 LEDs ist für die kurze Belichtungszeit ausgezeichnet.

---

*Erstellt: 2026-07-03 | Projekt: barcode-inspection-system*
