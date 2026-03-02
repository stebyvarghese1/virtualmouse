<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,30&height=240&section=header&text=Virtual%20Mouse&fontSize=78&fontColor=ffffff&fontAlignY=42&desc=Control%20your%20computer%20with%20nothing%20but%20your%20hand.&descAlignY=63&descSize=17&descColor=94a3b8&animation=fadeIn" width="100%"/>

</div>

<br>

<div align="center">

```
   AI-Powered  ·  Real-Time  ·  Touch-Free  ·  Open Source
```

</div>

<br>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand_Tracking-FF6F00?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev)
[![OpenCV](https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automation-22c55e?style=for-the-badge&logo=python&logoColor=white)](https://pyautogui.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-fbbf24?style=for-the-badge)](LICENSE)

<br>

[![Stars](https://img.shields.io/github/stars/stebyvarghese1/virtualmouse?style=flat-square&color=fbbf24&label=⭐%20Stars)](https://github.com/stebyvarghese1/virtualmouse/stargazers)
&nbsp;
[![Forks](https://img.shields.io/github/forks/stebyvarghese1/virtualmouse?style=flat-square&color=38bdf8&label=Forks)](https://github.com/stebyvarghese1/virtualmouse/forks)
&nbsp;
[![Built by](https://img.shields.io/badge/by-Steby%20Varghese-a78bfa?style=flat-square)](https://github.com/stebyvarghese1)

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 01 `&nbsp;&nbsp; THE DEMO

</div>

<br>

<div align="center">

<img src="https://github.com/user-attachments/assets/c9a7a979-5735-4234-8d5b-2c924e0d346c" width="82%"/>

<br><br>

> *Your hand is the mouse. No hardware. No drivers. Just a webcam.*

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 02 `&nbsp;&nbsp; THE IDEA

</div>

<br>

> ### *"What if you never had to touch a mouse again?"*

<br>

**Virtual Mouse** uses your webcam to track **21 hand landmarks** in real time, interprets finger positions as gestures, and translates them into native system mouse actions — clicks, scrolls, drags, zooms, all of it.

Built for anyone pushing the boundaries of human-computer interaction, accessibility, or just learning what modern AI can do with a $10 webcam.

**Perfect for**

```
  ┌──────────────────────────────────────────────────────────┐
  │  🧪  HCI experiments & research                          │
  │  ♿  Touchless & accessibility systems                    │
  │  🖥️  Smart, futuristic workspace setups                  │
  │  📚  AI & Computer Vision learning projects              │
  └──────────────────────────────────────────────────────────┘
```

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 03 `&nbsp;&nbsp; FEATURES

</div>

<br>

<div align="center">

| &nbsp; | Feature | What it does |
|--------|---------|-------------|
| 🎯 | **Cursor Control** | Move the mouse pointer with your index finger |
| 👆 | **Smart Clicks** | Left, right, and double-click via finger gestures |
| ✊ | **Drag & Drop** | Full drag-mode with a closed-hand gesture |
| 🔍 | **Pinch Zoom** | Zoom in and out with a pinch motion |
| 🔃 | **Scrolling** | Scroll pages with a dedicated gesture |
| ⚡ | **Real-Time** | Low-latency processing — smooth, responsive control |

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 04 `&nbsp;&nbsp; HOW IT WORKS

</div>

<br>

<div align="center">

```
  ┌─────────────┐     ┌──────────────────┐     ┌───────────────────┐
  │   Webcam    │────▶│    MediaPipe      │────▶│  Gesture Logic    │
  │  captures   │     │  detects 21 hand │     │  reads finger     │
  │   frames    │     │    landmarks      │     │  state & motion   │
  └─────────────┘     └──────────────────┘     └────────┬──────────┘
                                                         │
                       ┌─────────────────────────────────▼──────────┐
                       │              PyAutoGUI                      │
                       │   translates gestures → mouse actions       │
                       │   click · scroll · drag · zoom · move       │
                       └─────────────────────────────────────────────┘
                                         ▲
                       ┌─────────────────┘
                       │  OpenCV handles video capture + visualization
                       └──────────────────────────────────────────────
```

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 05 `&nbsp;&nbsp; GESTURE GUIDE

</div>

<br>

<div align="center">

```
  ┌────────────────────────────────┬──────────────────────────┐
  │  GESTURE                       │  ACTION                  │
  ├────────────────────────────────┼──────────────────────────┤
  │  Index finger up               │  🖱️  Move cursor          │
  │  Index + Thumb pinch           │  🖱️  Left click           │
  │  Middle + Thumb pinch          │  🖱️  Right click          │
  │  Ring + Thumb pinch            │  🖱️  Double click         │
  │  All fingers down              │  ✊  Drag mode            │
  │  Index up + Thumb down         │  🧊  Freeze cursor        │
  │  Index down + Pinky up         │  🔃  Scroll               │
  │  Index + Middle pinch          │  🔍  Zoom                 │
  └────────────────────────────────┴──────────────────────────┘
```

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 06 `&nbsp;&nbsp; TECH STACK

</div>

<br>

<div align="center">

| Library | Role |
|---------|------|
| 🐍 **Python 3** | Core language |
| 🤲 **MediaPipe** | Real-time hand landmark detection (21 points) |
| 👁️ **OpenCV** | Frame capture, video processing & visualization |
| 🖱️ **PyAutoGUI** | System-level mouse action automation |

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 07 `&nbsp;&nbsp; GETTING STARTED

</div>

<br>

**Prerequisites** — a connected webcam, Python 3.x

<br>

**Step 1 — Clone**
```bash
git clone https://github.com/stebyvarghese1/virtualmouse.git
cd virtualmouse
```

**Step 2 — Install dependencies**
```bash
pip install opencv-python mediapipe pyautogui
```

**Step 3 — Run**
```bash
python mouse.py
```

<div align="center">

> 🟢 &nbsp;Your webcam activates. Your hand takes control.

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 08 `&nbsp;&nbsp; PROJECT STRUCTURE

</div>

<br>

```
virtualmouse/
│
├── mouse.py          ← Main application entrypoint
├── controller.py     ← Gesture recognition & mapping logic
├── image.png         ← Demo screenshot
└── README.md
```

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 09 `&nbsp;&nbsp; WHAT'S NEXT

</div>

<br>

<div align="center">

```
  🔲  Multi-hand support
  🔲  Custom gesture configuration
  🔲  Adjustable sensitivity settings
  🔲  GUI-based control panel
  🔲  Cross-platform gesture presets
  🔲  Performance & latency optimizations
```

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 10 `&nbsp;&nbsp; ACKNOWLEDGEMENTS

</div>

<br>

<div align="center">

Built on the shoulders of giants.

| Project | By |
|---------|----|
| [MediaPipe](https://mediapipe.dev) | Google |
| [OpenCV](https://opencv.org) | OpenCV Community |
| [PyAutoGUI](https://pyautogui.readthedocs.io) | Al Sweigart & Contributors |

</div>

<br>
<br>

---

<br>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,30&height=130&section=footer&animation=fadeIn" width="100%"/>

### Built with ❤️ for AI & Computer Vision by [Steby Varghese](https://github.com/stebyvarghese1)

[![GitHub](https://img.shields.io/badge/GitHub-stebyvarghese1-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/stebyvarghese1)
&nbsp;
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-a78bfa?style=flat-square&logo=firefox&logoColor=white)](https://portfolio-v3ia.onrender.com/)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/steby-varghese)

<br>

**⭐ Star this repo if it impressed you — it keeps the vibes going!**

</div>
