from flask import Flask, render_template, request
from textsummary import summarizer
from keywordextraction import keywordEx

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        rawTExt = request.form['rawtext']
        summary, original, len_orginal, len_summary = summarizer(rawTExt)
        keywords = keywordEx(rawTExt)
    return render_template('summary.html', summary=summary, original=original, len_orginal=len_orginal, len_summary=len_summary, keywords=keywords)

if __name__ == "__main__":
    app.run(debug=True)