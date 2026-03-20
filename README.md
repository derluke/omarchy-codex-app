# Omarchy Codex App

Run the [OpenAI Codex app](https://openai.com/codex/) on Linux with Omarchy-focused polish.

The official Codex app is macOS/Windows-first. This fork provides an automated installer that converts the macOS `.dmg` into a working Linux application and adds Omarchy-specific desktop integration.

Forked from [`ilysenko/codex-desktop-linux`](https://github.com/ilysenko/codex-desktop-linux) and intentionally kept Omarchy-specific rather than generic.

## What This Fork Adds

- hides the default Electron menu bar on Linux
- adds optional Omarchy theme syncing when `~/.config/omarchy/current/theme/colors.toml` exists
- supports live theme reloads while the app is running
- installs a Linux desktop entry automatically in `~/.local/share/applications/codex.desktop`

## Quick Start

```bash
git clone https://github.com/derluke/omarchy-codex-app.git
cd omarchy-codex-app
./install.sh
```

If you are running Omarchy, the installed app will pick up the active Omarchy theme automatically.

## How it works

The installer:

1. Extracts the macOS `.dmg` (using `7z`)
2. Extracts `app.asar` (the Electron app bundle)
3. Rebuilds native Node.js modules (`node-pty`, `better-sqlite3`) for Linux
4. Removes macOS-only modules (`sparkle` auto-updater)
5. Downloads Linux Electron (same version as the app — v40)
6. Repacks everything and creates a launch script
7. Applies Linux UI patches for menu hiding and optional Omarchy theming

## Prerequisites

**Node.js 20+**, **npm**, **Python 3**, **7z**, **curl**, and **build tools** (gcc/g++/make).

### Debian/Ubuntu

```bash
sudo apt install nodejs npm python3 p7zip-full curl build-essential
```

### Fedora

```bash
sudo dnf install nodejs npm python3 p7zip curl
sudo dnf groupinstall 'Development Tools'
```

### Arch

```bash
sudo pacman -S nodejs npm python p7zip curl base-devel
```

You also need the **Codex CLI**:

```bash
npm i -g @openai/codex
```

## Installation

### Option A: Auto-download DMG

```bash
git clone https://github.com/derluke/omarchy-codex-app.git
cd omarchy-codex-app
chmod +x install.sh
./install.sh
```

### Option B: Provide your own DMG

Download `Codex.dmg` from [openai.com/codex](https://openai.com/codex/), then:

```bash
./install.sh /path/to/Codex.dmg
```

## Usage

The app is installed into `codex-app/` next to the install script:

`codex-app/start.sh`

The installer also creates a desktop launcher automatically, so Codex should appear in your application menu/dock after install.

Or add an alias to your shell:

```bash
echo 'alias codex-desktop="~/omarchy-codex-app/codex-app/start.sh"' >> ~/.bashrc
```

If Omarchy is installed, Codex will automatically read the active theme from `~/.config/omarchy/current/theme/colors.toml` and keep the app synced while it is running.

### Custom install directory

```bash
CODEX_INSTALL_DIR=/opt/codex ./install.sh
```

## How it works (technical details)

The macOS Codex app is an Electron application. The core code (`app.asar`) is platform-independent JavaScript, but it bundles:

- **Native modules** compiled for macOS (`node-pty` for terminal emulation, `better-sqlite3` for local storage, `sparkle` for auto-updates)
- **Electron binary** for macOS

The installer replaces the macOS Electron with a Linux build and recompiles the native modules using `@electron/rebuild`. The `sparkle` module (macOS-only auto-updater) is removed since it has no Linux equivalent.

A small Python HTTP server is used as a workaround: when `app.isPackaged` is `false` (which happens with extracted builds), the app tries to connect to a Vite dev server on `localhost:5175`. The HTTP server serves the static webview files on that port.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `Error: write EPIPE` | Make sure you're not piping the output — run `start.sh` directly |
| Blank window | Check that port 5175 is not in use: `lsof -i :5175` |
| `CODEX_CLI_PATH` error | Install CLI: `npm i -g @openai/codex` |
| GPU/rendering issues | Try: `./codex-app/start.sh --disable-gpu` |
| Sandbox errors | The `--no-sandbox` flag is already set in `start.sh` |
| Omarchy colors do not apply | Confirm `~/.config/omarchy/current/theme/colors.toml` exists, then restart Codex once |
| Launcher does not appear immediately | Log out/in once, or refresh your desktop environment's app menu cache |

## Disclaimer

This is an unofficial community fork. Codex is a product of OpenAI. This tool does not redistribute any OpenAI software — it automates the conversion process that users perform on their own copies.

## License

MIT
