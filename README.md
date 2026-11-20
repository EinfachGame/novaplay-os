# NovaPlay OS 🎮

**Ein Gaming-Betriebssystem auf Basis von Arch Linux** – mit KDE Plasma, Steam,
Treibern für AMD/Intel/NVIDIA, Gaming-Optimierungen, Neon-Design, eigenem
Installer und dem NovaPlay Center.

🇬🇧 [English version](README.en.md) · 📥 [Download (SourceForge)](https://sourceforge.net/projects/novaplay-os/files/) · 📝 [Neuerungen](CHANGELOG.md)

> NovaPlay OS ist ein Hobby-Projekt und steht in keiner Verbindung zu Arch Linux,
> Valve oder anderen genannten Firmen.

---

## Was ist drin?

| Bereich | Inhalt |
|---|---|
| Oberfläche | KDE Plasma 6, NovaPlay-Farbschema (Neon-Lila/Cyan), Papirus-Icons, Firefox, Dolphin |
| NovaPlay Center | Willkommens-App: Spiele-Launcher, Updates, Backups, Firewall, Drucker, Hilfe – alles mit einem Klick |
| NovaPlay Einstellungen | Eigenes, einfaches Einstellungsmenü (Gaming, Anzeige & Ton, Energie, Aussehen, Apps, Sicherheit …) |
| NovaPlay Spiele | Spielebibliothek für Steam, Epic, GOG und Lutris – wie die Xbox-App |
| NovaPlay App-Installer | Heruntergeladene Programme per Doppelklick installieren (.exe, .msi, .AppImage, .flatpakref) |
| Windows-Ersatz-Apps | Paint (KolourPaint), Notizen, Uhr & Wecker, Wetter, Kamera, Musik, Videoschnitt, Malen, Mail & Kalender, Sprachrekorder, Rechner, Solitär, Minesweeper, Mahjongg, Sudoku |
| Gaming | Steam (Proton), Lutris, Wine (+ Mono/Gecko), Winetricks, Protontricks, umu-launcher, GameMode, MangoHud, GOverlay, gamescope, CoreCtrl |
| Proton ab Werk | Neuestes GE-Proton vorinstalliert, „Steam Play für alle Spiele“ automatisch an |
| Weitere Launcher | Heroic (Epic + GOG), ProtonUp-Qt und Discord – werden nach der Installation automatisch nachgeladen |
| Konsolen-Modus | Steam Big Picture im Vollbild, wie auf dem Steam Deck |
| Kompatibilität | 32-Bit-Bibliotheken, VKD3D (DirectX 12), NTSync, Controller-Regeln (Xbox, PlayStation, Steam) |
| Treiber | Mesa + Vulkan (AMD/Intel), NVIDIA-Treiber (nvidia-open, ab GTX 16xx/RTX 20xx) – NVIDIA wird automatisch erkannt |
| Office | LibreOffice auf Deutsch (Writer, Impress, Calc), Okular (PDF) |
| Medien | Haruna (Videos), alle wichtigen Video-/Audio-Codecs, OBS Studio |
| Sicherheit | Firewall (ufw, an), Backups mit Timeshift, Schutz bei vollem Arbeitsspeicher (systemd-oomd) |
| Alltag | Drucker & Scanner (CUPS, automatische Netzwerk-Erkennung), KDE Connect (Handy-Verbindung), Windows-Laufwerke (NTFS, exFAT), 7-Zip, Rechner, Speicherplatz-Anzeige |
| Wartung | Automatische Wahl schneller Download-Server, automatische Bereinigung alter Pakete, Updates über Discover |
| Optimierungen | `vm.max_map_count` wie SteamOS, keine Split-Lock-Bremse, zram, größerer Shader-Cache |
| Design | Neon-Bootanimation, 3 Hintergründe, gestylter Anmelde- und Sperrbildschirm, Neon-Terminal mit Logo, FPS-Overlay im NovaPlay-Look |
| Sprache | Deutsch, deutsche Tastatur, Zeitzone Berlin |

## Systemanforderungen

- 64-Bit-PC mit **UEFI** (alle PCs der letzten ~10 Jahre), **Secure Boot aus**
- mind. 8 GB RAM (16 GB empfohlen), mind. 64 GB SSD
- Grafik: AMD (ab RX 400), Intel (ab HD 600 / Arc) oder NVIDIA (ab GTX 16xx / RTX 20xx)
- Internet für die Installation

## Installieren

1. **ISO herunterladen** von [SourceForge](https://sourceforge.net/projects/novaplay-os/files/)
   und die Prüfsumme kontrollieren (optional, siehe unten).
2. **USB-Stick erstellen** (mind. 8 GB, wird gelöscht): unter Windows mit
   [Rufus](https://rufus.ie) – bei Nachfrage **„DD-Image-Modus“** wählen.
3. **Vom Stick starten**: PC neu starten, Boot-Menü öffnen (meist **F12**, **F11**,
   **F8** oder **Esc**), den USB-Stick (UEFI) wählen.
4. Du landest im Live-Desktop (Benutzer `gamer`, Passwort `gamer`). Hier kannst du
   alles gefahrlos ausprobieren.
5. Mit dem Internet verbinden und auf **„NovaPlay installieren“** klicken (Desktop oder NovaPlay Center).
   Der Installer führt dich in 5 Schritten durch: Festplatte anklicken, Name und Passwort eingeben,
   bestätigen, fertig. ⚠️ **Die gewählte Festplatte wird komplett gelöscht.**
6. Nach 10–40 Minuten: USB-Stick abziehen, neu starten – fertig.

Beim ersten Start richtet sich das System im Hintergrund noch kurz ein
(Firewall, schnelle Server, Heroic/ProtonUp-Qt/Discord). Das braucht Internet und
dauert ein paar Minuten.

**Prüfsumme kontrollieren** (zeigt, dass der Download vollständig ist):
- Windows (PowerShell): `Get-FileHash .\novaplay-*.iso` → mit der `.sha256`-Datei vergleichen
- Linux: `sha256sum -c novaplay-*.iso.sha256`

## Nach der Installation

- **Steam**: anmelden → *Steam → Einstellungen → Kompatibilität → „Steam Play für alle anderen Titel“*.
- **FPS-Anzeige**: in Steam beim Spiel *Eigenschaften → Startoptionen*: `mangohud gamemoderun %command%`.
  Im Spiel ein-/ausblenden mit **Rechte Umschalttaste + F12**.
- **Konsolen-Modus**: beim Anmeldebildschirm unten links „NovaPlay Konsolen-Modus (Steam)“ wählen.
- **Backups**: NovaPlay Center → *Backups* → Timeshift einmal einrichten (z. B. wöchentlich).
- **Updates**: NovaPlay Center → *Updates* (oder im Terminal `sudo pacman -Syu`).
- **Proton-GE** (für Problem-Spiele): ProtonUp-Qt → *Add version* → GE-Proton → Steam neu starten.

## Programme aus dem Internet installieren

Datei herunterladen und **doppelklicken** – der NovaPlay App-Installer kümmert sich um den Rest:

| Datei | Was passiert |
|---|---|
| `.exe`, `.msi` | Windows-Programm wird mit Wine installiert und erscheint im Startmenü |
| `.AppImage` | Wird in „Anwendungen“ abgelegt, mit Startmenü-Eintrag |
| `.flatpakref`, `.flatpak` | Wird über den App-Store installiert |
| `.deb`, `.rpm` | Passt nicht zu NovaPlay → NovaPlay sucht dieselbe App im App-Store |

Noch einfacher: Fast alles gibt es direkt im **App-Store** (NovaPlay Center → App-Store).

## Was nicht läuft (ehrlich gesagt)

Die meisten Steam-Spiele laufen über Proton. **Nicht** laufen Spiele, deren Anti-Cheat
Linux bewusst blockiert – z. B. *Fortnite, Valorant, League of Legends, Call of Duty
(Warzone/MW), Rainbow Six Siege, Battlefield 2042/6, GTA Online*. Prüfen kannst du das
auf [protondb.com](https://www.protondb.com) und [areweanticheatyet.com](https://areweanticheatyet.com).

Außerdem (noch) nicht eingebaut: Dual-Boot neben Windows auf derselben Festplatte,
alte BIOS-PCs ohne UEFI, Festplatten-Verschlüsselung.

---

## Selbst bauen

Du brauchst Linux (Arch direkt oder ein anderes mit Docker) und ca. 25 GB Platz.

```bash
git clone https://github.com/EinfachGame/novaplay-os.git
cd novaplay-os
sudo ./build.sh
```

Das ISO liegt danach in `out/`. Unter Windows: Docker Desktop + WSL2 installieren und
die Befehle in WSL ausführen.

**Automatisch auf GitHub:** Der Workflow `.github/workflows/build-iso.yml` baut das ISO
monatlich, bei neuen Versions-Tags (`v…`) oder per Klick unter *Actions → ISO bauen →
Run workflow* – und lädt es zu SourceForge hoch (siehe [docs/VEROEFFENTLICHEN.md](docs/VEROEFFENTLICHEN.md)).

## Projektaufbau

```
novaplay-os/
├── build.sh                    ← baut das ISO
├── tools/make-graphics.py      ← erzeugt alle Grafiken (Farben oben änderbar)
├── .github/workflows/          ← automatischer Bau + Upload
├── docs/VEROEFFENTLICHEN.md    ← neue Versionen veröffentlichen
└── profile/                    ← Bauprofil (archiso, basiert auf "releng")
    ├── packages.x86_64         ← Programme im Live-System
    ├── profiledef.sh           ← Name, Version, Dateirechte
    ├── pacman.conf             ← Paketquellen (multilib für Steam)
    ├── efiboot/ syslinux/ grub/   ← Bootmenü
    └── airootfs/               ← Dateien, die 1:1 ins System kommen
        ├── usr/local/bin/novaplay-install    ← Installer
        ├── usr/local/bin/novaplay-center     ← NovaPlay Center (Python/Qt)
        ├── usr/local/bin/novaplay-firstboot  ← Einrichtung beim ersten Start
        ├── usr/local/bin/novaplay-firstlogin ← Design bei der ersten Anmeldung
        ├── usr/share/novaplay/packages-install.txt ← Programme fürs installierte System
        └── …                                 ← Design, Einstellungen, Dienste
```

## Mitmachen

Fehler gefunden oder Idee? Gerne ein [Issue](https://github.com/EinfachGame/novaplay-os/issues) öffnen.

## Lizenz

Die Skripte und Einstellungen von NovaPlay OS stehen unter der
[GPL-3.0-or-later](LICENSE) (wie das zugrunde liegende archiso-Profil).
Die enthaltenen Programme haben ihre eigenen Lizenzen; Steam und die NVIDIA-Treiber
stammen unverändert aus den offiziellen Arch-Linux-Paketquellen.
