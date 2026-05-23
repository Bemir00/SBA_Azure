from flask import Flask, send_from_directory
import os

# Flask is the application framework that holds the Python logic and routes.
# On Azure, Gunicorn (the production WSGI server, listed in requirements.txt)
# runs this app to serve the frontend.
app = Flask(__name__, static_folder=".")


@app.route("/")
def index():
    # Serve the single-page geometry calculator UI.
    return send_from_directory(".", "index.html")


if __name__ == "__main__":
    app.run()
