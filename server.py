from flask import Flask, render_template, request
from morse_converter import MorseConverter

app = Flask(__name__)

# Create an instance of MorseConverter
morse_converter = MorseConverter()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        plain_text = get_plain()
        morse_code = encrypt_plain(plain_text)
        return display_morse(morse_code)
    return render_template("index.html")


def get_plain():
    # Retrieve the plain text from the form
    return request.form.get("message", "")


def encrypt_plain(plain_text):
    # Convert the plain text to Morse code using the MorseConverter class
    return morse_converter.encrypt(plain_text)


def display_morse(morse_code):
    # Render the template with the Morse code
    return render_template("index.html", morse_code=morse_code)


if __name__ == "__main__":
    app.run(debug=True)
