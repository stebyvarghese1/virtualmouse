<div align="center">

# ✋ Virtual Mouse  
### Control Your Computer with Hand Gestures

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">
<img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge">

<br>
Transform your webcam into a powerful touch-free mouse using AI-powered hand tracking.
<br><br>

</div>

---

## 🎬 Preview

<div align="center">
<img src="https://github.com/user-attachments/assets/c9a7a979-5735-4234-8d5b-2c924e0d346c" width="80%">
</div>

---

## 🚀 Overview

Virtual Mouse enables real-time cursor control using hand gestures.  
It detects finger positions, interprets gestures, and performs mouse actions — all without touching a physical device.

Perfect for:
- Human-Computer Interaction experiments
- Touchless systems
- Smart workspace setups
- AI/Computer Vision learning projects

---

## ✨ Core Features

| Feature | Description |
|----------|------------|
| 🎯 Cursor Control | Move mouse with index finger |
| 👆 Smart Clicks | Left, right & double-click gestures |
| ✊ Drag & Drop | Full-hand gesture control |
| 🔍 Zoom Support | Pinch-based zoom in/out |
| 🔃 Scrolling | Gesture-based scrolling |
| ⚡ Real-Time | Low-latency performance |

---

## 🧠 How It Works

1. Webcam captures video frames.
2. MediaPipe detects 21 hand landmarks.
3. Finger state logic determines gestures.
4. PyAutoGUI converts gestures into system mouse actions.
5. OpenCV handles video processing & visualization.

---

## 🛠️ Technology Stack

- **Python 3**
- **MediaPipe** (Hand Landmark Detection)
- **OpenCV** (Image Processing)
- **PyAutoGUI** (System Control Automation)

---

## 📂 Project Structure

```
.
├── mouse.py          # Main application
├── controller.py     # Gesture recognition logic
├── image.png         # Demo screenshot
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/stebyvarghese1/virtualmouse.git
cd virtualmouse
```

### 2️⃣ Install Dependencies
```bash
pip install opencv-python mediapipe pyautogui
```

### 3️⃣ Run Application
```bash
python mouse.py
```

Make sure your webcam is connected and enabled.

---

## 🎯 Gesture Control Guide

| Gesture | Action |
|----------|--------|
| Index finger up | Move cursor |
| Index + Thumb pinch | Left click |
| Middle + Thumb pinch | Right click |
| Ring + Thumb pinch | Double click |
| All fingers down | Drag |
| Index up + Thumb down | Freeze cursor |
| Index down + Pinky up | Scroll |
| Index + Middle pinch | Zoom |

---

## 📈 Future Enhancements

- Multi-hand support
- Custom gesture configuration
- Adjustable sensitivity
- GUI-based control panel
- Performance optimization
- Cross-platform gesture presets

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

- MediaPipe by Google
- OpenCV Community
- PyAutoGUI Contributors

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

Built with passion for AI & Computer Vision.

</div>
