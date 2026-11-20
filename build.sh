#!/bin/bash
# =====================================================================
#  NovaPlay OS – ISO bauen
#  Aufruf im Projektordner:   sudo ./build.sh
#  Ergebnis:                  out/novaplay-JJJJ.MM.TT-x86_64.iso
#
#  Läuft entweder direkt auf Arch Linux (mit Paket "archiso")
#  oder auf jedem anderen Linux mit Docker.
#  Braucht ca. 25 GB freien Speicher und eine gute Internetverbindung.
# =====================================================================
set -euo pipefail
cd "$(dirname "$0")"
PROJ="$(pwd)"
mkdir -p out work

[ "$(id -u)" -eq 0 ] || { echo "Bitte mit sudo starten: sudo ./build.sh"; exit 1; }

echo "==> Lade neuestes GE-Proton (wird bei der Installation vorinstalliert) ..."
if ! bash profile/airootfs/usr/local/bin/novaplay-fetch-proton-ge download \
        profile/airootfs/usr/share/novaplay/proton-ge; then
    echo "   WARNUNG: GE-Proton konnte nicht geladen werden – es wird dann beim ersten Start nachgeladen."
fi

if command -v mkarchiso >/dev/null 2>&1; then
    echo "==> Baue direkt mit mkarchiso ..."
    rm -rf work/*
    mkarchiso -v -r -w "$PROJ/work" -o "$PROJ/out" "$PROJ/profile"
elif command -v docker >/dev/null 2>&1; then
    IMAGE="${NOVAPLAY_BUILDER:-novaplay-builder}"
    if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
        echo "==> Erstelle Bau-Container (einmalig) ..."
        printf 'FROM archlinux:latest\nRUN pacman -Syu --noconfirm archiso && pacman -Scc --noconfirm\n' \
            | docker build -t "$IMAGE" -
    fi
    echo "==> Baue im Docker-Container ..."
    docker run --rm --privileged \
        -v "$PROJ/profile:/profile:ro" \
        -v "$PROJ/work:/work" \
        -v "$PROJ/out:/out" \
        -v novaplay-pkgcache:/var/cache/pacman/pkg \
        "$IMAGE" bash -c 'pacman -Sy --noconfirm --needed archiso >/dev/null && rm -rf /work/* && mkarchiso -v -r -w /work -o /out /profile'
else
    echo "Weder mkarchiso noch docker gefunden."
    echo "Auf Arch:   sudo pacman -S archiso"
    echo "Sonst:      Docker installieren (https://docs.docker.com/engine/install/)"
    exit 1
fi

echo
echo "==> Fertig! Dein ISO:"
ls -lh out/*.iso
