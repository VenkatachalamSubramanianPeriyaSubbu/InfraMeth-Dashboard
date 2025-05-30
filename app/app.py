from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/map')
def about():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)