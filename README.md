# ✨ AI Image Generator

A simple web app to generate beautiful, topic-based story images using the [Pexels API](https://www.pexels.com/api/). Just enter a keyword like "Ferrari", "Anime", or "Sunset", and get multiple AI-enhanced images with overlaid text — optimized for mobile stories or desktop wallpapers.

### 🌐 Live Demo
👉 [ai-image-generator-pzl1.onrender.com](https://ai-image-generator-pzl1.onrender.com/)

---

## 🚀 Features

- 🔎 Search any topic (e.g. cars, cities, anime, etc.)
- 🖼️ Generates multiple high-quality images from Pexels
- 📝 Overlays the topic text beautifully on each image
- 📲 Mobile responsive and desktop-friendly layout
- 📥 Download each image with one click

---

## 🛠️ Built With

- [Flask](https://flask.palletsprojects.com/) - Python backend
- [Pillow (PIL)](https://python-pillow.org/) - Image processing
- [Pexels API](https://www.pexels.com/api/) - Image source
- [HTML/CSS (responsive UI)](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries)

---

## 🔧 Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- A free [Pexels API Key](https://www.pexels.com/api/)

---

### 📦 Installation

```bash
# 1. Clone the repository
https://github.com/AadiSharma49/AI-image-Generator.git
cd ai-image-generator

# 2. Create virtual environment and activate it
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your secrets.env file
mkdir config
echo "PEXELS_API_KEY=your_api_key_here" > config/secrets.env

# 5. Run the server
python server.py
