# System-Konzept: Vollständige Produktionsinspektion

Ideensammlung für ein komplettes Inspektions- und Drucksystem.
Wird laufend ergänzt — noch nicht vollständig implementiert.

---

## Modul 1: Kombi-Inspektion (Loch + Barcode)

Bereits vollständig konzipiert → siehe [README.md](README.md) und [LED_Blitz_Barcode_Scanner.pdf](LED_Blitz_Barcode_Scanner.pdf)

**Kurzzusammenfassung:**
- 4× CM5-Einheit, je 2 Bahnen (8 Bahnen gesamt)
- Je Bahn: Kamera 1 (Loch) + Kamera 2 (Barcode/OCR)
- OPB917 #1 → Loch-Trigger, OPB917 #2 → Barcode-Trigger
- Inkremental-Encoder → Fehlende-Loch-Erkennung
- MQTT → Pi5 Server → SQLite

---

## Modul 2: Druckkopf-Registerkorrektur

### Problem
Tintenstrahldrucker (Fremdgerät) soll Nummern in ein vorgedrucktes Feld drucken.
Das Feld sitzt nicht immer an gleicher Stelle — Produktionsschwankungen in Y.
Zugriff auf Druckdaten des Fremddruckers nicht möglich.

### Lösung
Kamera erkennt Feldposition → Schrittmotor verschiebt gesamten Drucker in Y.

### Rahmenbedingungen
- Maschinengeschwindigkeit: ~25 m/min
- Ticket-Takt: alle 1,5 Sekunden (~625 mm Abstand)
- Kamera 300 mm vor Drucker → 720 ms verfügbar
- Korrekturweg: typisch ±2–3 mm

### Felderkennung (OV9281 + OpenCV)
Ticket hat weißen vorgedruckten Balken → horizontale Helligkeits-Projektion:

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
proj = np.mean(gray, axis=1)          # Mittelwert je Zeile
zeilen = np.where(proj > 200)[0]      # Weißer Bereich
y_mitte = int(np.mean(zeilen))        # Y-Schwerpunkt
delta_mm = (y_mitte - y_soll) / px_pro_mm
```

Laufzeit: <1 ms. Kein Training, kein Template.

### Mechanik
- Drucker komplett auf Linearschlitten (Y-Achse)
- Nema-17 + Spindel 2 mm/U → 1600 Schritte/mm bei 1/16-Stepping

### Steuerung
- Treiber: **TMC5160** (bereits im System vorhanden)
- Interface: **rohe SPI-Register, RP Pico**
- CM5 → Pico: UART `"Y+1300\n"` (Versatz in µm)
- Pico → TMC5160: XTARGET-Register → Motor fährt selbstständig

```
CM5 (Erkennung)  →UART→  Pico  →SPI→  TMC5160  →  Nema-17
```

### Protokoll-Integration
- δy wird per MQTT mitgeloggt
- Kein Druck wenn kein Feld erkannt (Sicherheit)

---

## Offene Ideen

*Werden hier eingetragen sobald besprochen.*

---

*Stand: 2026-07-03*
