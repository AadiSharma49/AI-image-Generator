from flask import Flask, request, render_template, send_from_directory
import os
from utils.generate_story_image import create_story_images

app = Flask(__name__, static_folder='static')

# Directory to store generated images
IMAGE_FOLDER = os.path.join(app.static_folder, 'assets')
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    topic = None
    filenames = []

    if request.method == 'POST':
        topic = request.form.get('topic')
        if topic:
            # Generate 3 different images and save to static/assets
            filenames = create_story_images(topic, output_dir=IMAGE_FOLDER, count=3)

    return render_template('index.html', topic=topic, filenames=filenames)

@app.route('/download/<filename>')
def download_file(filename):
    # Ensure safe file handling and valid path
    safe_path = os.path.join(IMAGE_FOLDER, filename)
    if os.path.exists(safe_path):
        return send_from_directory(IMAGE_FOLDER, filename, mimetype='image/jpeg', as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
