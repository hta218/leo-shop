from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<category>')
def category(category):
    return render_template('productgrid.html')

if __name__ == '__main__':
  app.run(debug=True)
