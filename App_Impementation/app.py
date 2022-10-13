from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)