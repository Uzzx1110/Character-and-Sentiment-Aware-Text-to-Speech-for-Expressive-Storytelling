from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
AUDIO_FILE = 'static/GeneratedNarration.mp3'  # replace with your system-stored audio file

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload_textfile', methods=['POST'])
def upload_textfile():
    if 'textfile' in request.files:
        file = request.files['textfile']
        if file and file.filename.endswith('.txt'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                text_content = f.read()

            text_content = '''Narrator(Neutral): In a small town named Mathville, lived two best friends, Algy and Sammy. They loved solving puzzles and riddles together. One sunny day, they found a mysterious note on their favorite park bench. It read,
Sammy(Curiuous): Solve -1147 = -11*a - 1213 for ‘a’. What is the answer?
Narrator(Neutral): Algy, being good at numbers, decided to take up the challenge. He explained to Sammy,
Algy: First, we need to get ‘a’ alone. To do that, let’s add 1213 to both sides of the equation.
Narrator(Neutral): So, they added 1213 to -1147, making it 66.

Next, Algy said,
Algy: Now, we simplify both sides to make our work easier!
Narrator(Neutral): And voila! Both sides became 66. Excitedly, he shared his next step with Sammy:
Algy: Let’s divide both sides by -11 now, so we can finally see what ‘a’ equals!
Narrator(Neutral): A little confused, Sammy asked,
Sammy: But won’t negative divided by negative give us positive? Why would we want to use minus here?
Narrator(Neutral): With a smile, Algy replied,
Algy: Great question, Sammy! Yes, usually, negative divided by negative gives us positive. But when you divide a number by itself – no matter its sign – the result will always be 1 or, in this case, -1 since we have a negative number. That way, we maintain balance between the left and right side of the equation.
Narrator(Neutral): After dividing, they discovered that 'a' was equal to -6.'''
            #Business logic for tts

            return jsonify({"text_content": text_content, "audio_ready": True})
    return jsonify({"error": "Invalid file uploaded."}), 400

@app.route('/api/generate_story', methods=['POST'])
def generate_story():
    data = request.get_json()
    keywords = data.get('keywords', '')

    #Business logic for tts and generate story
    keywords = '''Narrator(Neutral): In a small town named Mathville, lived two best friends, Algy and Sammy. They loved solving puzzles and riddles together. One sunny day, they found a mysterious note on their favorite park bench. It read,
Sammy(Curiuous): Solve -1147 = -11*a - 1213 for ‘a’. What is the answer?
Narrator(Neutral): Algy, being good at numbers, decided to take up the challenge. He explained to Sammy,
Algy: First, we need to get ‘a’ alone. To do that, let’s add 1213 to both sides of the equation.
Narrator(Neutral): So, they added 1213 to -1147, making it 66.

Next, Algy said,
Algy: Now, we simplify both sides to make our work easier!
Narrator(Neutral): And voila! Both sides became 66. Excitedly, he shared his next step with Sammy:
Algy: Let’s divide both sides by -11 now, so we can finally see what ‘a’ equals!
Narrator(Neutral): A little confused, Sammy asked,
Sammy: But won’t negative divided by negative give us positive? Why would we want to use minus here?
Narrator(Neutral): With a smile, Algy replied,
Algy: Great question, Sammy! Yes, usually, negative divided by negative gives us positive. But when you divide a number by itself – no matter its sign – the result will always be 1 or, in this case, -1 since we have a negative number. That way, we maintain balance between the left and right side of the equation.
Narrator(Neutral): After dividing, they discovered that 'a' was equal to -6.'''
    if keywords:
        story = f"{keywords}"  # mock response
        return jsonify({"story": story, "audio_ready": True})
    return jsonify({"error": "No keywords provided."}), 400

@app.route('/play_audio')
def play_audio():
    return send_file(AUDIO_FILE, as_attachment=False)

@app.route('/download_audio')
def download_audio():
    return send_file(AUDIO_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)