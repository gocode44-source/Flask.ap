from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page 🏠"
    return render_template('index.html')


@app.route('/about')
def about():
    return "About Page ℹ️"

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name} 🔥"
    return "Direct access not allowed 😅"


if __name__ == '__main__':
    app.run(debug=True)
