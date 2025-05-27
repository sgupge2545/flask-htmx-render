from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def hello():
    return (
        '<img src="/image.png" alt="画像" style="max-width:400px; margin-top:20px;" />'
    )


@app.route("/image.png")
def image():
    return send_file("image.png", mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
