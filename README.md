# ASCII / Unicode Art Converter

A browser-based image, video, and webcam to ASCII/Unicode art converter. Runs entirely client-side — no server needed. Built with Astro, deployable to Cloudflare Pages.

**Live demo:** [your-domain.pages.dev](https://your-domain.pages.dev)

## Features

**Input**
- Drag & drop or browse for images and videos
- Paste from clipboard
- Live webcam feed
- Load from URL

**Character modes**
- Block characters `░▒▓█`
- Dense ASCII (69 levels)
- Simple ASCII
- Braille patterns `⣿` (2×4 dot cells)
- Unicode — density-sorted from ~2000 symbols across 18 Unicode blocks
- Emoji mosaic — nearest-color emoji matched via O(1) lookup table
- Custom — type your own character sequence (sparse → dense)

**Effects**
- Full-color or monochrome with custom fg/bg color pickers
- Invert (dark bg / light bg)
- Brightness and contrast sliders
- Dithering — Floyd-Steinberg, Atkinson, Ordered/Bayer
- Edge detection — Sobel operator → directional chars `─ │ ╱ ╲`
- Drift mode — particle flow along iso-luminance contours

**Export**
- Copy as plain text
- Download PNG, JPG, SVG, TXT
- Webcam snapshot (freezes frame, then export as above)
- Record video as WebM (live canvas capture)

## Tech stack

- [Astro](https://astro.build) — static site, single page, zero JS frameworks
- Canvas API — offscreen sampler canvas + output canvas, `requestAnimationFrame` loop
- `MediaRecorder` API — video recording
- Cloudflare Pages — hosting

## Local development

```bash
npm install
npm run dev
```

## Build & deploy

```bash
npm run build   # outputs to dist/
```

**Cloudflare Pages settings:**
- Build command: `npm run build`
- Build output directory: `dist`
- Node version: 18+

## License

MIT
