"""
main
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    """
    main
    """
    return open("./ad.html","r",encoding="utf-8").read()

app.run()
