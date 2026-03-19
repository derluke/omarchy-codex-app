#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys
import time


APP_DIR = Path(__file__).resolve().parent
WEBVIEW_ASSETS = APP_DIR / "content" / "webview" / "assets"
CSS_FILE = WEBVIEW_ASSETS / "omarchy-theme.css"
THEME_DIR = Path.home() / ".config" / "omarchy" / "current" / "theme"
COLORS_TOML = THEME_DIR / "colors.toml"
LIGHT_MODE = THEME_DIR / "light.mode"


def parse_colors(path: Path) -> dict[str, str]:
    colors: dict[str, str] = {}
    if not path.exists():
        return colors
    pattern = re.compile(r'^([A-Za-z0-9_]+)\s*=\s*"([^"]+)"\s*$')
    for line in path.read_text().splitlines():
        match = pattern.match(line.strip())
        if match:
            colors[match.group(1)] = match.group(2)
    return colors


def render_css(colors: dict[str, str], mode: str) -> str:
    accent = colors.get("accent", "#81a1c1")
    foreground = colors.get("foreground", "#d8dee9")
    background = colors.get("background", "#2e3440")
    selection_fg = colors.get("selection_foreground", foreground)
    selection_bg = colors.get("selection_background", "#4c566a")
    color0 = colors.get("color0", "#3b4252")
    color1 = colors.get("color1", "#bf616a")
    color2 = colors.get("color2", "#a3be8c")
    color3 = colors.get("color3", "#ebcb8b")
    color4 = colors.get("color4", accent)
    color5 = colors.get("color5", "#b48ead")
    color6 = colors.get("color6", "#88c0d0")
    color7 = colors.get("color7", "#e5e9f0")
    color8 = colors.get("color8", selection_bg)
    color9 = colors.get("color9", color1)
    color10 = colors.get("color10", color2)
    color11 = colors.get("color11", color3)
    color12 = colors.get("color12", accent)
    color13 = colors.get("color13", color5)
    color14 = colors.get("color14", "#8fbcbb")
    color15 = colors.get("color15", "#eceff4")

    return f""":root,
:host,
.electron-dark,
.electron-light {{
  --vscode-foreground: {foreground};
  --vscode-disabledForeground: {color8};
  --vscode-descriptionForeground: {color7};
  --vscode-icon-foreground: {foreground};

  --vscode-sideBar-background: {background};
  --color-background-surface-under: {background};
  --color-background-elevated-primary: {background};
  --color-background-elevated-secondary: {selection_bg};
  --color-background-surface: {color0};
  --vscode-editor-background: {background};
  --vscode-editor-foreground: {foreground};
  --vscode-input-background: {color0};
  --vscode-input-foreground: {foreground};
  --vscode-dropdown-background: {color0};
  --vscode-menu-background: {color0};

  --vscode-focusBorder: {accent};
  --vscode-button-background: {accent};
  --vscode-button-foreground: {background};
  --vscode-button-border: {accent};
  --vscode-button-secondaryHoverBackground: {color6};
  --vscode-textLink-foreground: {accent};
  --vscode-textLink-activeForeground: {color6};
  --vscode-list-activeSelectionBackground: {selection_bg};
  --vscode-list-activeSelectionForeground: {selection_fg};
  --vscode-list-activeSelectionIconForeground: {accent};
  --vscode-list-hoverBackground: {color8};
  --vscode-toolbar-hoverBackground: {color8};
  --vscode-scrollbarSlider-background: color-mix(in srgb, {accent} 25%, transparent);
  --vscode-scrollbarSlider-hoverBackground: color-mix(in srgb, {accent} 45%, transparent);
  --vscode-scrollbarSlider-activeBackground: color-mix(in srgb, {accent} 60%, transparent);

  --vscode-input-border: {color8};
  --vscode-checkbox-background: {accent};
  --vscode-checkbox-border: {accent};
  --vscode-checkbox-foreground: {background};
  --vscode-radio-activeForeground: {accent};

  --vscode-badge-background: {accent};
  --vscode-badge-foreground: {background};
  --vscode-editorGroup-dropBackground: color-mix(in srgb, {accent} 20%, transparent);
  --vscode-editorGroup-dropIntoPromptBackground: color-mix(in srgb, {accent} 22%, transparent);
  --vscode-editorGroup-dropIntoPromptForeground: {foreground};

  --vscode-errorForeground: {color1};
  --vscode-editorError-foreground: {color1};
  --vscode-inputValidation-errorBackground: color-mix(in srgb, {color1} 14%, transparent);
  --vscode-inputValidation-errorBorder: {color1};
  --vscode-editorWarning-foreground: {color3};
  --vscode-inputValidation-warningBackground: color-mix(in srgb, {color3} 14%, transparent);
  --vscode-inputValidation-warningBorder: {color3};
  --vscode-inputValidation-infoBackground: color-mix(in srgb, {accent} 14%, transparent);

  --vscode-terminal-background: {background};
  --vscode-terminal-foreground: {foreground};
  --vscode-terminal-border: {color8};
  --vscode-terminal-selectionBackground: {selection_bg};
  --vscode-terminal-inactiveSelectionBackground: color-mix(in srgb, {selection_bg} 65%, transparent);
  --vscode-terminal-ansi-black: {color0};
  --vscode-terminal-ansi-red: {color1};
  --vscode-terminal-ansi-green: {color2};
  --vscode-terminal-ansi-yellow: {color3};
  --vscode-terminal-ansi-blue: {color4};
  --vscode-terminal-ansi-magenta: {color5};
  --vscode-terminal-ansi-cyan: {color6};
  --vscode-terminal-ansi-white: {color7};
  --vscode-terminal-ansi-bright-black: {color8};
  --vscode-terminal-ansi-bright-red: {color9};
  --vscode-terminal-ansi-bright-green: {color10};
  --vscode-terminal-ansi-bright-yellow: {color11};
  --vscode-terminal-ansi-bright-blue: {color12};
  --vscode-terminal-ansi-bright-magenta: {color13};
  --vscode-terminal-ansi-bright-cyan: {color14};
  --vscode-terminal-ansi-bright-white: {color15};

  --vscode-gitDecoration-addedResourceForeground: {color2};
  --vscode-gitDecoration-deletedResourceForeground: {color1};
  --vscode-charts-blue: {color4};
  --vscode-charts-green: {color2};
  --vscode-charts-orange: {color3};
  --vscode-charts-purple: {color5};
  --vscode-charts-red: {color1};
  --vscode-charts-yellow: {color3};
  color-scheme: {mode};
}}

.bg-\\[\\#1e1e1e\\],
.bg-\\[var\\(--vscode-editor-background\\)\\],
.main-surface {{
  background-color: {background} !important;
}}

.window-fx-sidebar-surface,
.app-header-tint {{
  background-color: color-mix(in srgb, {background} 92%, transparent) !important;
}}

.window-fx-sidebar-surface [data-state='active'],
.window-fx-sidebar-surface .bg-token-list-hover-background {{
  background-color: {selection_bg} !important;
}}

.window-fx-sidebar-surface [data-state='active'],
.window-fx-sidebar-surface [data-state='active'] *,
.window-fx-sidebar-surface .bg-token-list-hover-background,
.window-fx-sidebar-surface .bg-token-list-hover-background * {{
  color: {selection_fg} !important;
}}
"""


def write_css() -> None:
    if not COLORS_TOML.exists():
        return
    WEBVIEW_ASSETS.mkdir(parents=True, exist_ok=True)
    mode = "light" if LIGHT_MODE.exists() else "dark"
    css = render_css(parse_colors(COLORS_TOML), mode)
    CSS_FILE.write_text(css)


def watch() -> int:
    last_state = None
    while True:
        state = (
            COLORS_TOML.exists(),
            COLORS_TOML.stat().st_mtime_ns if COLORS_TOML.exists() else None,
            LIGHT_MODE.exists(),
            LIGHT_MODE.stat().st_mtime_ns if LIGHT_MODE.exists() else None,
        )
        if state != last_state:
            write_css()
            last_state = state
        time.sleep(1.5)


def main(argv: list[str]) -> int:
    if "--watch" in argv:
        return watch()
    write_css()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
