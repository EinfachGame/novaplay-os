# Neuerungen

## 1.1 – November 2026

**Neu: Grafischer Installer** – Festplatte per Klick wählen, Name und Passwort in normale Felder,
Fortschrittsbalken, am Ende „Neu starten“. Kein Terminal mehr nötig.

**Neu: NovaPlay Einstellungen** – übersichtliches Einstellungsmenü: Gaming (Steam Play, Konsolen-Modus,
FPS-Anzeige, Leistungsmodus, Controller), Anzeige & Ton (mit Lautstärkeregler), Netzwerk & Geräte,
Aussehen (Hintergründe, hell/dunkel), Energie & Sperre, Apps & Updates, Konto & Sicherheit, System.

**Neu: Proton ab Werk** – das neueste GE-Proton wird bei der Installation vorinstalliert (oder beim ersten
Start nachgeladen), und „Steam Play für alle Spiele“ ist automatisch eingeschaltet.

**Neu: Programme aus dem Internet per Doppelklick installieren** – der NovaPlay App-Installer erkennt
.exe/.msi (Wine), .AppImage, .flatpakref/.flatpak und schlägt bei .deb/.rpm die passende App im App-Store vor.
Bekannte Windows-Installer (Steam, Epic, Discord, Minecraft …) leitet er auf den besseren Linux-Weg um.

**Neue eigene Apps**
- NovaPlay Spiele – alle Spiele aus Steam, Epic, GOG (Heroic) und Lutris an einem Ort
- NovaPlay Notizen – schnelle Notizen wie die Windows-Kurznotizen

**Mehr Apps wie bei Windows**: KolourPaint (Paint), Uhr & Wecker, Wetter, Kamera, Elisa (Musik),
Kdenlive (Videoschnitt), Krita (Malen), Thunderbird (Mail & Kalender), Sprachrekorder, Rechner,
Zeichentabelle, Remotedesktop, Scanner, Solitär, Minesweeper, Mahjongg, Sudoku.

**Kleinigkeiten**: Fenster öffnen sich in der Bildschirmmitte; die Ersteinrichtung installiert Heroic, ProtonUp-Qt
und Discord auch dann, wenn der GE-Proton-Download gerade nicht klappt (neuer Versuch beim nächsten Start).


## 1.0.1 – November 2026

**Fehlerbehebungen**
- Sperrbildschirm: In virtuellen Maschinen (VMware, VirtualBox) blieb der Bildschirm nach der automatischen Sperre schwarz bzw. ohne Passwortfeld. Live-System sperrt jetzt nicht mehr automatisch und schaltet den Bildschirm nicht ab; das installierte System sperrt nicht mehr automatisch (manuell mit Win + L) und schaltet den Bildschirm erst nach 15 Minuten ab.
- Kein automatischer Ruhezustand am Netzstrom mehr (lange Spiele-Downloads brechen nicht ab).
- NovaPlay Center: Discord-Kachel zeigt jetzt ein Symbol, auch bevor Discord installiert ist.

## 1.0 – November 2026

Erste öffentliche Version.

**Gaming**
- Steam mit Proton, Konsolen-Modus (Steam Big Picture im Vollbild)
- Lutris, Wine (+ Mono/Gecko), Winetricks, Protontricks, umu-launcher
- GameMode, MangoHud (FPS-Overlay im NovaPlay-Look), GOverlay, gamescope, CoreCtrl
- Heroic, ProtonUp-Qt und Discord werden nach der Installation automatisch als Flatpak nachgeladen
- 32-Bit-Bibliotheken, VKD3D, NTSync, Controller-Regeln
- Treiber für AMD, Intel und NVIDIA (automatische Erkennung im Installer)
- Optimierungen: vm.max_map_count, Split-Lock, zram, Shader-Cache

**System & Alltag**
- NovaPlay Center (Willkommens- und Steuerzentrum)
- Firewall (ufw) mit freien Ports für Steam Remote Play und KDE Connect
- Backups mit Timeshift, Schutz bei vollem Arbeitsspeicher (systemd-oomd)
- Drucker und Scanner mit automatischer Netzwerk-Erkennung
- LibreOffice, Okular, Haruna, Video-Codecs, OBS Studio, KDE Connect
- NTFS/exFAT, 7-Zip, Rechner, Speicherplatz-Anzeige
- Automatische Wahl schneller Server, automatische Paket-Bereinigung

**Design**
- Neon-Bootanimation, NovaPlay-Farbschema, Papirus-Icons
- 3 Hintergrundbilder, gestylter Anmelde- und Sperrbildschirm
- Neon-Terminal mit NovaPlay-Logo

**Installer**
- Geführte Installation (UEFI, systemd-boot), automatische Anmeldung und Konsolen-Modus wählbar
