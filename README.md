# aktujo – brand kit

The look of aktujo. Every falkOSS project has its own name, logo, colours and look; falkOSS appears only as publisher.

- **Mark** – a document folder with a sheet in it and a keyhole in its front: *aktujo* is Esperanto for a container of
  documents, and the keyhole says they are kept private. The keyhole is cut out, so any background shows through. The
  small variant (16–48 px) has a heavier sheet and no keyhole.
- **Wordmark** – `aktujo`, set in **Space Mono Bold** and turned into outlines (no font needed where it is shown),
  with a block cursor in the accent.
- **Colours** – one accent, sealing-wax red: `#B3262B` on dark, `#9E1F24` on light. Near-black `#0D1117` as ground,
  `#E6EDF3` for text on dark, `#14202B` on light. On dark, the red is for areas, blocks and backgrounds (white text on
  it: about 6.8:1), not for small text.
- **Font** – Space Mono (SIL OFL 1.1) in `fonts/` with its licence; on the web never loaded from other servers.

Everything here is generated: edit `generate.py` (the drawing) – `brandkit.py` (the export) stays as it is – then run
`python3 generate.py` (needs `rsvg-convert` from Homebrew `librsvg` and `fontTools`: `pip install fonttools`). It writes `svg/`, `png/`, `web/` and `apps/`.

| Use | File |
|---|---|
| GitHub organisation avatar | `png/social/github-avatar-500.png` |
| GitHub social preview, link previews | `png/social/aktujo-social-1280x640.png` |
| Website head (copy to the website) | `web/` – favicon.svg (follows light/dark), favicon.ico, apple-touch-icon.png, icon-192/512.png, social.png, site.webmanifest |
| Headers, documents, profile | `svg/aktujo-lockup-on-dark.svg`, `-on-light.svg` (PNG: `png/lockup/`) |
| Wordmark alone | `svg/aktujo-wordmark-on-dark.svg`, `-on-light.svg` |
| Mark alone (transparent) | `svg/aktujo-mark-on-dark.svg`, `-on-light.svg`; one colour: `-black.svg`, `-white.svg` |
| App-like icon | `png/icon/` (rounded), `png/icon-square/` (edge to edge), `png/icon-small/` (16–48 px) |
| App icons (Flutter runners, see below) | `apps/` – macOS with Apple's margin (the small mark at 16 and 32 px), iOS full bleed without alpha, Android, Windows `.ico` |

## Where it is used

This repository is the brand's one source; the others carry copies of what they show and are updated by copying,
never edited there:

| Repository | Copies |
|---|---|
| `aktujo/website` | `web/`, the lockup and mark on dark (`assets/`) |
| `aktujo/.github` | the lockups in the organisation profile |
| `aktujo/aktujo` | `web/favicon.*` and the lockup on dark in `docs/assets/`; `web/favicon.svg` in the web app's `web/public/` (if there is one) |
| `aktujo/apps` | `apps/` – each file to the same name in the Flutter runners: `macos/Runner/Assets.xcassets/AppIcon.appiconset/`, `ios/Runner/Assets.xcassets/AppIcon.appiconset/`, `android/app/src/main/res/`, `windows/runner/resources/` |

## Rules for the real design (as for all falkOSS projects)

- One accent colour, near-black or a clear light ground; straight edges where it fits; no glow, neon or gradients
  unless the project's idea needs them.
- A small variant for 16–48 px that still reads.
- A wordmark as outlines (no font needed where it is shown); fonts only under a free licence (e.g. SIL OFL), never
  loaded from a font service – fonts go to `fonts/` with their licence, and into `REUSE.toml`.
- The name is always lowercase.

## Licences and rights

| Files | Licence |
|---|---|
| `generate.py`, `brandkit.py`, this README | [MIT](LICENSES/MIT.txt) |
| the artwork: `svg/`, `png/`, `web/`, `apps/` | [CC BY-ND 4.0](LICENSES/CC-BY-ND-4.0.txt) |
| `fonts/` (Space Mono) | [SIL Open Font License 1.1](LICENSES/OFL-1.1.txt), used unmodified |

The artwork may be copied and passed on – also in apps distributed through app stores and in other software – as it
is and naming falkOSS; changed versions may not be passed on. The licence covers the artwork's copyright, not the
name: aktujo's name and brand belong to falkOSS – Falcon Lake Open Source Software gUG (haftungsbeschränkt) i. G., the publisher of aktujo. They may be used to refer to aktujo,
not for other products or in a way that suggests endorsement. **OPEN**: trademark search and registration, and a
review of these terms by someone who knows the law.
