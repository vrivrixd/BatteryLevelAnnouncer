# Batteriestandsankündiger
## Von Vitor Bruski
Der **Batteriestandsankündiger** ist ein Add-on für NVDA, das den Batteriestand in konfigurierbaren Intervallen mit Ton und/oder Sprache ankündigt. Es bietet flexible Optionen zur Anpassung der Ankündigungen.
## Funktionen
- Konfigurierbare Ankündigungsintervalle;
- Ankündigungsmodi;
- Anpassbares Prüfintervall der Batterie;
- Unterstützung für benutzerdefinierte Töne für jeden Prozentsatz.
## Verwendung
Nach der Installation konfigurieren Sie das Add-on über das Menü **NVDA > Einstellungen > Einstellungen > Batteriestandsankündiger**. Die verfügbaren Optionen sind:
- **Prüfintervall der Batterie (Sekunden):** Legen Sie fest, wie viele Sekunden das Add-on zwischen jeder Überprüfung des Batteriestands wartet. Je kleiner der Wert, desto höher der CPU-Verbrauch.
- **Ankündigungsintervall:** Wählen Sie zwischen:
  - Deaktiviert; Keine Ankündigungen.
  - 5 % (kündigt bei 5 %, 10 %, 15 %, usw. an)
  - 10 % (kündigt bei 10 %, 20 %, 30 %, usw. an)
  - 20 % (kündigt bei 20 %, 40 %, 60 %, usw. an)
  - 25 % (kündigt bei 25 %, 50 %, 75 %, 100 % an)
  - 50 % (kündigt bei 50 %, 100 % an)
  - Nur wenn der Akku voll ist (kündigt nur bei 100 % an)
- **Ankündigungsmodus:** Wählen Sie zwischen:
  - Nur Sprache;
  - Nur Ton;
  - Ton und Sprache.
- **Ankündigungston auswählen:** Wählen Sie eine WAV-Datei aus dem Ordner `sounds\` für Ankündigungen.
- **Benutzerdefinierte Töne für jeden Prozentsatz verwenden:** Aktivieren Sie diese Option, um spezifische WAV-Dateien (z. B. 5.wav, 10.wav) im Ordner `sounds\custom\` zu verwenden, entsprechend dem gewählten Intervall.
- **Tonordner öffnen:** Öffnet den Ordner `sounds\` im Datei-Explorer, damit Sie Ihre eigenen Töne verwenden können.
- **Benutzerdefinierten Tonordner öffnen:** Öffnet den Ordner `sounds\custom\`.
## Anforderungen
- NVDA-Version 2019.3 oder höher.
- Windows-Betriebssystem mit Batterieunterstützung (z. B. Laptops).
## Lizenz
Lizenziert unter der [GNU General Public License v2 (GPLv2)](https:\\www.gnu.org\licenses\gpl-2.0.html).