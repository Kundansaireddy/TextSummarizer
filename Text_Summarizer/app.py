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
    res = []
    res.append(long_text)
    res.append(len(long_text))
    res.append(summary)
    res.append(len(summary))
    return render_template("index.html", prediction=res)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
