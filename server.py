from flask import Flask

PORT = 8000
MESSAGE = "Devops Training batch completed with success - project_1\n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
