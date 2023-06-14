from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/englishToFrench', methods=['POST', 'GET'])
def eng_to_french():
    if request.method == 'POST':
        text = request.form['text']
        fr_text = translator.english_to_french(text)
        return render_template('translate.html', text=fr_text)
    return render_template('translate.html')


@app.route('/frenchToEnglish', methods=['POST', 'GET'])
def french_to_eng():
    if request.method == 'POST':
        text = request.form['text']
        en_text = translator.french_to_english(text)
        return render_template('translate.html', text=en_text)
    return render_template('translate.html')