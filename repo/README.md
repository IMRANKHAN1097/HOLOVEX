# HOLOVEX — Research & Innovation Lab

<p align="center"><img src="assets/holovex-logo.svg" width="112" alt="HOLOVEX logo"></p>
<p align="center"><strong>Reconstructing Light. Redefining Vision.</strong></p>
<p align="center">Holography · Computational Imaging · AI for Optics · Photonics</p>

HOLOVEX is a research-oriented digital workspace for interactive holography consoles, computational imaging experiments, methods notes, and reproducible project development.

## Flagship research direction

**HVX-001 — Computational Holography**  
A staged research project covering numerical wave propagation, phase retrieval, phase-only hologram synthesis, reconstruction analysis, and reproducibility. See [`projects/HVX-001.md`](projects/HVX-001.md).

## What the website contains

- **Research profile:** background, research experience, methods, and skills page retained from the supplied project.
- **HVX Project 01 — Liquid mixing:** interactive digital-holography console and research visualisations.
- **HVX Project 02 — Spray droplets:** interactive spray-droplet holography console and dataset visualisations.
- **HVX-001 — Computational holography:** Gerchberg–Saxton, gradient-descent hologram optimisation, and Takeda phase-recovery demonstrations.

The supplied scientific pages, images, datasets, methods notes, and reference material have been retained. The public-facing identity and navigation have been updated to HOLOVEX.

## Interface features

- Dark, light, and system-following appearance modes.
- Six accent palettes: Aurora, Ocean, Sunset, Emerald, Royal, and Mono.
- Font and text-size controls.
- Animated navigation and ambient background motion.
- Responsive layout for desktop and mobile.
- Reduced-motion accessibility support.

Theme preferences are stored locally in the visitor's browser. No account or backend is required for the static website.

## Run locally

No build step is needed to view the published static website.

1. Download or clone this repository.
2. Open `index.html` in a modern browser.

For the optional scientific-console rebuild and verification scripts, install Python dependencies and run:

```bash
python -m pip install -r requirements.txt
python tools/verify.py
python tools/build.py
```

## Publish free with GitHub Pages

1. Create a GitHub repository named **`holovex-lab`** under your account.
2. Upload the contents of this repository (the files inside this folder, not the outer ZIP folder).
3. Commit the files to the `main` branch.
4. Open **Settings → Pages** and select **GitHub Actions** as the build and deployment source.
5. The included workflow at `.github/workflows/pages.yml` will verify, build, and deploy the site after a push to `main`.

Expected URL for the account `IMRANKHAN1097`:

`https://imrankhan1097.github.io/holovex-lab/`

GitHub Pages availability and URL activation are controlled by GitHub; the repository must first be created and pushed.

## Repository structure

```text
.
├── index.html
├── assets/
│   ├── holovex-logo.svg
│   └── scientific image assets
├── computational_console.html
├── internship_console.html
├── mixing_console.html
├── spray_console.html
├── projects/
│   └── HVX-001.md
├── data/
├── docs/
├── tools/
└── .github/workflows/pages.yml
```

## Scientific references and attribution

The original project documentation, methods, references, datasets, and source material are retained in `docs/`, `data/`, and `assets/`. Review those materials before reusing experimental datasets or making scientific claims. The repository is released under the license in [`LICENSE`](LICENSE).

## Citation

See [`CITATION.cff`](CITATION.cff) for software citation metadata.
