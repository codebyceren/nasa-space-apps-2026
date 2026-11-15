# 🚀 Mission Mars — Explore Before You Build

**NASA Space Apps Challenge 2026** · Challenge: *Build a Junior Astronaut Mission Trainer*
**Team BagBang:** Ceren Günhan · Zehra Lülü · Muslima Mamajonova

▶ **Play now:** https://codebyceren.github.io/nasa-space-apps-2026/

Mission Mars is a 3D browser game where students live and work on Mars as astronauts. Players choose a real landing site and a crew role, run a Martian base for six sols, explore with a rover and finally fly back to Earth. Power, water, oxygen, food and radiation must stay in balance, and every choice has a cost. More than 25 mini-games turn each task into hands-on science, built on real NASA data.

## Features
- 4 real landing sites (Jezero, Gale, Elysium Planitia, Arcadia Planitia) on a 3D Mars globe
- 3 crew roles with different tasks: Power Engineer, Water Hunter, Radiation Scientist
- Daily crew routine: eat, exercise, system checks, expeditions, report to Earth, sleep
- Random events (dust storms, solar particle events, equipment faults) with A/B decisions
- 25+ science mini-games, each ending with a sourced fact
- Pressurized rover, discovery sites, rock samples, service pad
- Live NASA space-weather data (DONKI) with archived fallback
- Explorer mode (ages 7–12) and Engineer mode (older students and adults)
- 8 languages: English, Türkçe, Русский, Italiano, Français, Español, العربية, 日本語
- Works offline after the first visit and can be installed as an app (PWA)

## Repository structure
```
index.html               ← the game GitHub Pages serves (built, self-contained)
sw.js                    ← service worker (offline play)
manifest.webmanifest     ← PWA manifest
icons/                   ← app icons
.nojekyll                ← serve files as-is on GitHub Pages
src/
  mission-mars.src.html  ← full game source (HTML + CSS + JavaScript, ES modules)
  textures/              ← Mars and Earth textures (embedded at build time)
  pwa-head.html          ← PWA meta tags added to index.html
  pwa-tail.html          ← service-worker registration added to index.html
  sw.template.js         ← service-worker template
tools/build.py           ← build script
package.json             ← build dependencies (three 0.160.0, esbuild)
```

## Run locally
The built game is a single file: open `index.html` in a modern browser (Chrome, Edge, Firefox, Safari).
To test the service worker too, serve the folder:
```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Build from source
Requirements: Node.js 18+ and Python 3.
```bash
npm install
npm run build
```
The build:
1. embeds the textures from `src/textures/` into the page,
2. bundles the game code and Three.js with esbuild into one offline file (`dist/mission-mars-offline.html`),
3. adds the PWA tags and writes `index.html` and `sw.js` to the repository root.

`dist/mission-mars-dev.html` is an unbundled version that loads Three.js from the jsDelivr CDN (needs internet).

## Technology
HTML5 · CSS · JavaScript (ES modules) · [Three.js](https://threejs.org) r160 (WebGL) · Progressive Web App · [esbuild](https://esbuild.github.io) · Python · [Playwright](https://playwright.dev) for automated play-testing.
We used [Claude](https://claude.ai) (Anthropic) as an AI coding and writing assistant.

## NASA data and other sources
- NASA DONKI Space Weather Database — https://kauai.ccmc.gsfc.nasa.gov/DONKI/ · API: https://api.nasa.gov/
- Curiosity RAD surface radiation — https://doi.org/10.1126/science.1244797
- Curiosity RAD, May 2024 solar storm — https://www.nasa.gov/solar-system/planets/mars/nasa-watches-mars-light-up-during-epic-solar-storm/
- NASA OSDR (OSD-804, 488, 326, 343, 615, 658) — https://osdr.nasa.gov/bio/
- NASA Mars Trek — https://trek.nasa.gov/mars/
- MRO CRISM spectral library — https://pds-geosciences.wustl.edu/missions/mro/crism.htm
- Curiosity REMS weather — https://science.nasa.gov/photojournal/steady-temperatures-at-mars-gale-crater
- NASA 3D Resources (Viking colour Mars texture) — https://science.nasa.gov/3d-resources/
- APOD and NASA Image and Video Library — https://apod.nasa.gov/apod/ · https://images.nasa.gov/
- ISS exercise countermeasures (CEVIS, ARED, T2) — https://ntrs.nasa.gov/citations/20160012791
- Canadian Space Agency — Deep Space Food Challenge — https://asc-csa.gc.ca/eng/sciences/food-production/deep-space-food-challenge.asp
- USGS Spectral Library — https://www.usgs.gov/labs/spectroscopy-lab/science/spectral-library
- Earth textures — Solar System Scope (CC BY 4.0) — https://www.solarsystemscope.com/textures/

Every number in the game is labelled **MEASURED**, **DERIVED** or **GAME ASSUMPTION**.
