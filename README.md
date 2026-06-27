# 🌐 Shri Abinaya S — Personal Portfolio

> **Live Portfolio:** [your-username.github.io/portfolio](https://your-username.github.io/portfolio) *(update with your actual link)*

A single-file personal portfolio website for **Shri Abinaya S**, ECE Engineer (2023–2027) at Sri Ramakrishna Institute of Technology, Coimbatore — specializing in Embedded Systems, Computer Vision, IoT, and AI/ML.

---

## ✨ Features

- **Animated Hero** — Dual canvas with live circuit trace and particle animations
- **Glassmorphism UI** — Dark deep-purple/coral-red theme with blur-glass cards
- **Fully Responsive** — Mobile navbar with hamburger menu, fluid grid layouts
- **Dynamic Content** — Projects, certifications, achievements, and competitions rendered from a JavaScript data layer (no backend required)
- **Project Modals** — Click any project card for a deep-dive: problem, solution, architecture, tech stack, features, and results
- **Marquee Competitions** — Auto-scrolling infinite carousel for competition history
- **Smooth Reveal Animations** — IntersectionObserver-driven section reveals on scroll
- **Custom Scrollbar** — Styled to match the theme

---

## 🗂️ Sections

| Section | Description |
|---|---|
| Hero | Name, role, tagline, animated background |
| About | Background, approach, keyword tags |
| Experience | BSNL Telecom Internship |
| Skills | Programming, Hardware/Embedded, AI/ML tools |
| Projects | 11 featured projects with modal deep-dives |
| Patents & Publications | Research papers and filed patents |
| Certifications | Category cards + 35+ MATLAB/Simulink badges |
| Leadership | ASME, HIVE, IEDC, NSS, Table Tennis |
| Competitions | Scrolling marquee of hackathons and challenges |
| Awards & Achievements | National-level recognitions with image cards |
| Gallery | Photo grid |
| Contact | Email, LinkedIn, GitHub links |

---

## 🚀 Projects Showcased

| Project | Stack | Highlight |
|---|---|---|
| **FreshScan** | YOLOv8, IoT, ESP8266 | 93.2% food spoilage detection accuracy |
| **Panel2Wire** | GNN, OCR, GenAI, Streamlit | 98% electrical symbol recognition |
| **DraftMind AI** | YOLOv8, scikit-learn, OCR | 82–88% manufacturability scoring |
| **G-Max** | Renewable Energy, BMS, IoT | MSME Idea Pitch Pre-Finalist |
| **AquaFlow** | ESP32, AWS IoT, React.js, LoRa | Smart rural water distribution |
| **Aurum** | NDT, Sensor Fusion, Embedded | Non-destructive gold purity testing |
| **Rover-X** | Arduino, ESP32, Robotics | Caterpillar Challenge Pre-Finals, IIT Madras |
| **SignalIQ** | YOLOv8, Arduino, PySerial | Ambulance-priority traffic management |
| **CropGuard XAI** | XAI (LIME/SHAP), Blockchain | 92% corn disease detection |
| **VulnSight AI** | FastAPI, NetworkX, scikit-learn | CVE attack path mapping |
| **Fan Health Diagnostic** | Embedded, Signal Processing | Predictive maintenance system |

---

## 🛠️ Tech Stack

**Languages:** HTML5, CSS3 (custom properties, grid, flexbox), Vanilla JavaScript

**Fonts:** [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) · [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono)

**External dependencies:** Google Fonts only — no frameworks, no build tools required.

---

## 📁 File Structure

```
portfolio/
├── portfolio_v7.html       # Main single-file portfolio
├── favicon.svg             # Site favicon
├── images/
│   ├── hero/
│   │   └── hero_profile.jpg
│   ├── about/
│   │   └── about_profile.jpg
│   ├── projects/           # Project cover images (named by project id)
│   ├── achievements/       # Award/recognition images
│   └── gallery/            # Gallery photos
└── README.md
```

---

## 🖥️ Running Locally

No build step required. Just open the HTML file:

```bash
# Clone the repo
git clone https://github.com/your-username/portfolio.git
cd portfolio

# Open directly in browser
open portfolio_v7.html
```

Or serve with a local server to avoid any browser CORS restrictions with local images:

```bash
# Python
python -m http.server 8000

# Node.js (npx)
npx serve .
```

Then visit `http://localhost:8000/portfolio_v7.html`.

---

## 🌍 Deployment (GitHub Pages)

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Set source to **main branch**, root folder `/`.
4. GitHub will publish at `https://your-username.github.io/portfolio/`.
5. Rename `portfolio_v7.html` to `index.html` for the root URL to work directly.

---

## 🏆 Achievements

- 🥇 **IEEE SPAVE 2K25** — 1st Prize
- 🏅 **L&T PIVOT Challenge** — Best Innovators Award (National)
- 🎖️ **ASME KRUU GRASP 2026 Hackathon** — Special Citation (India-level)
- 🏆 **Vishwakarma Awards 2025** — 13th Place (National)
- 🤖 **Caterpillar Autonomy Challenge** — Pre-Finals, IIT Madras
- 🌱 **MSME Idea Pitch** — Pre-Finals (G-Max Project)

---


<p align="center">Designed & built by Shri Abinaya S · 2025</p>
