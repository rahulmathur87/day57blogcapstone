from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_endpoint = 'https://api.npoint.io/982b6858478d3009210b'
response = requests.get(blog_endpoint)
response.raise_for_status()
blogs = response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)
