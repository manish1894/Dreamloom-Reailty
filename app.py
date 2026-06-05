from flask import Flask, render_template, request
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('pine.html')
@app.route('/login', methods=['POST'])
def login():
    u= request.form.get('username')
    p= request.form.get('password')

    if u == 'admin' and p == '1234':
        return render_template('dashboard.html')
    else:
        return "<h3>Invalid Username or Password!</h3><a href='/'>Again</a>"
@app.route('/logout')
def logout():
    return render_template('pine.html')
if __name__ == '__main__':
    app.run(debug=True)

