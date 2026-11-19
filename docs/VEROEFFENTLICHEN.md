# Neue Versionen veröffentlichen

Das ISO wird **automatisch auf GitHub gebaut** und zu **SourceForge** hochgeladen.
Du musst dafür nichts auf deinem PC bauen.

## Einmalige Einrichtung (schon erledigt, nur zur Info)

In GitHub unter **Settings → Secrets and variables → Actions**:

| Art | Name | Inhalt |
|---|---|---|
| Secret | `SF_SSH_KEY` | privater SSH-Schlüssel (der passende öffentliche Schlüssel ist bei SourceForge unter *Account Settings → SSH Settings* eingetragen) |
| Secret | `SF_USER` | dein SourceForge-Benutzername |
| Variable | `SF_PROJECT` | Projektname auf SourceForge, z. B. `novaplay-os` |

Fehlen diese Einträge, baut GitHub das ISO trotzdem, lädt es aber nicht hoch.

## Neue Version veröffentlichen

**Variante A – per Klick (am einfachsten):**
1. Auf GitHub ins Projekt → Reiter **Actions** → links **„ISO bauen“**.
2. Rechts **„Run workflow“** → grüner Knopf **„Run workflow“**.
3. Nach ca. 30–60 Minuten liegt das neue ISO auf SourceForge in einem Ordner mit dem Datum.

**Variante B – mit Versionsnummer:**
1. `CHANGELOG.md` ergänzen.
2. Auf GitHub → **Releases → Draft a new release** → Tag z. B. `v1.1` → *Publish*.
   Der Bau startet automatisch.

Zusätzlich baut GitHub jeden Monat (am 1.) automatisch ein frisches ISO.

## Neueste Version als Standard-Download auf SourceForge

Damit der große grüne Download-Knopf auf SourceForge das neue ISO anbietet:
SourceForge → **Files** → beim neuen ISO auf das **ⓘ**-Symbol → **„Default Download For“**
alle Systeme anhaken → *Save*.

## Wenn der Bau fehlschlägt

GitHub → **Actions** → den roten Lauf anklicken → den roten Schritt öffnen.
Meist ist ein Paket umbenannt oder entfernt worden – dann den Namen in
`profile/packages.x86_64` und `profile/airootfs/usr/share/novaplay/packages-install.txt`
anpassen (aktuelle Namen: <https://archlinux.org/packages/>).
