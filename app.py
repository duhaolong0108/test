"""
main
"""
from flask import Flask

app = Flask(__name__)
data = [
    "https://www.highcpmrevenuegate.com/gwkjvcb1wj?key=e28919d1426ebddccd7c2d31236cd8f7",
    "https://www.highcpmrevenuegate.com/qd444zjnkq?key=391f508d664a93afc7596ae17e4c24c1",
    "https://www.highcpmrevenuegate.com/r2ff725r?key=d7c95194cd63fdcb145387a6b4cc2fdd",
    "https://www.highcpmrevenuegate.com/s3sfqwmq?key=041648b8dbf80bcea606bb5ded17dd0a",
    "https://www.highcpmrevenuegate.com/ayrpeihbe2?key=7c703d2eba1c206f68872e4b02ec4b12",
    "https://www.highcpmrevenuegate.com/g18w8rbww?key=e0fb37daeedb5b2f46a42c7eed5d2bff"
]
global dar
dar = -1


@app.route("/")
def main():
    """
    main
    """
    global dar
    a = open("./ad.html", "r", encoding="utf-8").read().split("$0$")
    dar = dar + 1
    return a[0] + data[dar] + a[1] + str(dar) + a[2]


app.run()
