from flask import Flask, render_template, request, redirect, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # In production: send email or save to DB
        print(f"Message from {name} ({email}): {message}")
        flash('Message sent! Thank you.')
        return redirect('/contact')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)