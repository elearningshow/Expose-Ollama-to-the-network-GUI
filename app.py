from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

def call_ollama(message: str, model: str = "llama2") -> str:
    try:
        process = subprocess.run(
            ['ollama', 'run', model],
            input=message,
            capture_output=True,
            text=True,
            timeout=120,  # increased timeout to 2 minutes
        )
        if process.returncode != 0:
            return f"Error calling Ollama: {process.stderr.strip()}"
        return process.stdout.strip()
    except Exception as e:
        return f"Exception calling Ollama: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    user_message = data['message'].strip()
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400

    bot_response = call_ollama(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
