from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=["POST"])
def translate():
    userinput = request.form.get('inputText')
    appendtext = "ay"
    translatedtext = ""

    wordlist = userinput.split(" ")
    for word in wordlist:
        sliced = word[1:len(word)]
        flipped = sliced + word[0] + appendtext

        translatedtext = translatedtext + " " + flipped

    return render_template("index.html", pigLatinText=translatedtext)


if __name__ == '__main__':
    app.run(debug=True)

