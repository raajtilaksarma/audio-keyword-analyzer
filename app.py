from flask import Flask, render_template, request, url_for
from speechy import KeywordCounter
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    counts = []
    transcription = ''
    if request.method=='POST':
        f = request.files['audiofile']
        f.save(secure_filename(f.filename))
        audioFileName = f.filename
        f = request.files['keywordfile']
        f.save(secure_filename(f.filename))
        keywordFileName = f.filename
        kw = KeywordCounter(audioFileName,keywordFileName)
        counts = kw.getResult()
        transcription = kw.transcription
        #print(counts)
    return render_template('index.html',counts=counts, transcription=transcription)

if __name__ == "__main__":
    app.run(host="0.0.0.0")