# NovaPlay OS 🎮

**A gaming operating system based on Arch Linux** – with KDE Plasma, Steam, drivers for
AMD/Intel/NVIDIA, gaming tweaks, a neon design, its own installer and the NovaPlay Center.

🇩🇪 [Deutsche Version](README.md) · 📥 [Download (SourceForge)](https://sourceforge.net/projects/novaplay-os/files/) · 📝 [Changelog](CHANGELOG.md)

> NovaPlay OS is a hobby project and is not affiliated with Arch Linux, Valve or any
> other company mentioned. The system language is **German** by default
> (change it in *System Settings → Region & Language*).

## Features

- **Desktop:** KDE Plasma 6 with a custom neon colour scheme, Papirus icons, Firefox
- **NovaPlay Center:** welcome app with one-click access to launchers, updates, backups, firewall, printers and help
- **Gaming:** Steam (Proton), Lutris, Wine, Winetricks, Protontricks, umu-launcher, GameMode, MangoHud, GOverlay, gamescope, CoreCtrl
- **Auto-installed after setup:** Heroic (Epic/GOG), ProtonUp-Qt (Proton-GE), Discord (Flatpak)
- **Console mode:** Steam Big Picture fullscreen session, like the Steam Deck
- **Compatibility:** 32-bit libraries, VKD3D (DirectX 12), NTSync, controller rules
- **Drivers:** Mesa/Vulkan for AMD and Intel, NVIDIA (nvidia-open, GTX 16xx/RTX 20xx and newer) detected automatically
- **Office & media:** LibreOffice, Okular, Haruna, full codecs, OBS Studio
- **Security & maintenance:** ufw firewall (enabled), Timeshift backups, systemd-oomd, automatic mirror ranking, package cache cleanup
- **Everyday:** printing & scanning (CUPS + network discovery), KDE Connect, NTFS/exFAT, 7-Zip
- **Tweaks:** SteamOS-like `vm.max_map_count`, split-lock mitigation off, zram, larger shader cache

## Requirements

64-bit **UEFI** PC (Secure Boot off), 8 GB RAM (16 GB recommended), 64 GB SSD,
AMD RX 400+ / Intel HD 600+ / NVIDIA GTX 16xx+, internet connection for installation.

## Install

1. Download the ISO from [SourceForge](https://sourceforge.net/projects/novaplay-os/files/).
2. Write it to a USB stick (8 GB+) with [Rufus](https://rufus.ie) (choose **DD image mode**) or balenaEtcher.
3. Boot from the stick (UEFI). The live session logs in automatically (user `gamer`, password `gamer`).
4. Connect to the internet and click **"NovaPlay installieren"** in the NovaPlay Center.
   ⚠️ **The selected disk will be erased completely.**

## Known limitations

Games whose anti-cheat blocks Linux (e.g. Fortnite, Valorant, League of Legends,
Call of Duty, Rainbow Six Siege, GTA Online) will not work. Check
[protondb.com](https://www.protondb.com). No dual-boot on the same disk, no legacy BIOS,
no disk encryption yet.

## Build it yourself

```bash
git clone https://github.com/EinfachGame/novaplay-os.git
cd novaplay-os
sudo ./build.sh        # needs Arch Linux (archiso) or Docker, ~25 GB free space
```

## License

NovaPlay OS scripts and configuration: [GPL-3.0-or-later](LICENSE).
Bundled software keeps its own licenses.
