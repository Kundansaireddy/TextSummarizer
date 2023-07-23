from flask import Flask, render_template, request
from transformers import pipeline
app = Flask(__name__)


def summarize_text(text, max_length=100):
    summarizer = pipeline("summarization")
    result = summarizer(text, max_length=max_length,
                        min_length=30, do_sample=False)
    summary = result[0]['summary_text']
    return summary


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    long_text = request.form['text']
    summary = summarize_text(long_text)
    return render_template("index.html", prediction=summary)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
