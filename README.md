# 🔥 Thermal Camera Printer 🖨️  

A **Python** application that captures images using a **Raspberry Pi camera** and prints them on a **thermal printer** using **ESC/POS** commands. Designed for quick and stylish prints, perfect for DIY projects, instant photo booths, or creative experiments.

---

## ✨ Features

✅ Capture images using `libcamera-still`  
✅ Process images for optimal thermal printing  
✅ Convert images to ESC/POS format  
✅ Print directly to a thermal printer via **serial connection**  
✅ Simple and customizable  

---

## 🛠️ Requirements

🔹 Raspberry Pi with a **camera module**  
🔹 Compatible **thermal printer** (ESC/POS supported, serial interface)  
🔹 **Python 3.6+**  
🔹 Required Python packages (see `requirements.txt`)  

---

## 🚀 Installation

### 1️⃣ Clone this repository  
`git clone https://github.com/yourusername/thermal-camera-printer  
cd thermal-camera-printer`

### 2️⃣ Install dependencies  
`pip install -r requirements.txt`

### 3️⃣ Connect your thermal printer  
Ensure your printer is connected to the **serial port** (default: `/dev/serial0`).

---

## 🎯 Usage

Run the main script:  
`python -m camprint.camprint`

### What happens?  
1️⃣ Captures an image using the Raspberry Pi camera 📸  
2️⃣ Processes the image for **high-contrast thermal printing** 🏭  
3️⃣ Sends the processed image to the **thermal printer** 🎟️  

---

## ⚙️ Configuration

Modify default settings inside `camprint/camprint.py`:

| Setting        | Default Value     | Description |
|---------------|------------------|-------------|
| **Printer Port** | `/dev/serial0` | Serial port for communication |
| **Baud Rate**   | `9600`          | Printer communication speed |
| **Image Capture Size** | `640x480` | Camera image resolution |
| **Print Width** | `384px`         | Width of printed images |

---

## 🧪 Development & Testing

### Run Tests  
`python -m unittest discover tests`

---

## 📁 Project Structure

`
thermal-camera-printer/
├── LICENSE                # License information
├── README.md              # Project documentation (you are here!)
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files for Git
├── setup.py               # Package setup script
├── camprint/              # Main application logic
│   ├── __init__.py        # Module initialization
│   └── camprint.py        # Main image capture & print script
└── tests/                 # Unit tests
    └── test_camprint.py   # Tests for camprint module
`

---

## 🤝 Contributing

We love contributions! 🛠️ To contribute:  

1. **Fork** this repository  
2. **Create** your feature branch (`git checkout -b feature/amazing-feature`)  
3. **Commit** your changes (`git commit -m 'Added an amazing feature'`)  
4. **Push** to your branch (`git push origin feature/amazing-feature`)  
5. **Submit** a Pull Request  

---

## 📜 License

This project is **MIT Licensed** – see the `LICENSE` file for details.

---

🚀 **Get ready to print cool images in seconds!** 🎟️  

🔥 **Made with Raspberry Pi, Python, and Thermal Magic!** 💻🎨  