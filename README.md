
# ✋ AI Virtual Mouse using Hand Gestures

This project uses computer vision and hand tracking to turn your hand into a virtual mouse! With just a webcam and your hand, you can move the cursor, click, scroll, drag, and even zoom — completely touch-free.
---

## 🚀 Features

- 📹 Real-time hand tracking using MediaPipe
- 🖱️ Move cursor with index finger
- 👆 Click, right-click, and double-click using finger gestures
- 🖱️ Drag and drop using all fingers
- 🔍 Zoom in/out using pinch gestures
- 🔃 Scroll using specific finger poses

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

---

## 📁 Project Structure

```
.
├── mouse.py            # Main app for virtual mouse
├── controller.py       # Gesture controller logic
├── image.png           # Screenshot of app in action
```

---

## 🎯 Gestures Guide

| Gesture                            | Action             |
|------------------------------------|--------------------|
| Index finger up                    | Move cursor        |
| Index + Thumb pinch                | Left click         |
| Middle + Thumb pinch               | Right click        |
| Ring + Thumb pinch                 | Double click       |
| All fingers down                   | Drag               |
| Index up + Thumb down              | Freeze cursor      |
| Index down + Pinky up              | Scroll up/down     |
| Pinch index + middle fingers       | Zoom in/out        |

---

## 📸 Screenshot

![Hand Tracking Demo](https://github.com/user-attachments/assets/c9a7a979-5735-4234-8d5b-2c924e0d346c)


---

## 📄 License

This project is licensed under the **MIT License** 

MIT License

Copyright (c) 2024 Steby Varghese

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---

## 💡 Credits

- Powered by [Google MediaPipe](https://google.github.io/mediapipe/)
- Inspired by human-computer interaction via gestures
