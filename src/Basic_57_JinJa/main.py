from flask import Flask, render_template


app = Flask(__name__)
block_url = "https://api.npoint.io/7011753364ea871e8b36"

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/post/<int:index>')
def create_blog(index):
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
