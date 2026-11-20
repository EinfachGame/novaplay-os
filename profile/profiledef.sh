#!/usr/bin/env bash
# shellcheck disable=SC2034
# NovaPlay OS – Bauprofil (basiert auf dem offiziellen archiso-Profil "releng")

iso_name="novaplay"
iso_label="NOVAPLAY_$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y%m)"
iso_publisher="NovaPlay OS"
iso_application="NovaPlay OS Live/Installer"
iso_version="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux'
           'uefi.systemd-boot')
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd' '-Xcompression-level' '15' '-b' '1M')
bootstrap_tarball_compression=('zstd' '-c' '-T0' '--long' '-19')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/sudoers.d/10-novaplay-live"]="0:0:440"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/root/.gnupg"]="0:0:700"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
  ["/usr/local/bin/novaplay-install"]="0:0:755"
  ["/usr/local/bin/novaplay-firstlogin"]="0:0:755"
  ["/usr/local/bin/novaplay-steam-session"]="0:0:755"
  ["/usr/local/bin/novaplay-live-user"]="0:0:755"
  ["/usr/local/bin/novaplay-firstboot"]="0:0:755"
  ["/usr/local/bin/novaplay-center"]="0:0:755"
  ["/usr/local/bin/novaplay-installer"]="0:0:755"
  ["/usr/local/bin/novaplay-proton"]="0:0:755"
  ["/usr/local/bin/novaplay-settings"]="0:0:755"
  ["/usr/local/bin/novaplay-settings-helper"]="0:0:755"
  ["/usr/local/bin/novaplay-app-installer"]="0:0:755"
  ["/usr/local/bin/novaplay-games"]="0:0:755"
  ["/usr/local/bin/novaplay-notes"]="0:0:755"
  ["/usr/local/bin/novaplay-fetch-proton-ge"]="0:0:755"
)
