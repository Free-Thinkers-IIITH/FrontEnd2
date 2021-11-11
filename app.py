from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/ans', methods =['POST','GET'])
def login_ans():
    name = request.form['username']
    pwd = request.form['password']
    if name == "sourabh" and pwd == "1234":
        return render_template('ans.html', info="Welcome to organization Page!")
    else:
        return render_template('login.html', info="Invalid Username/Password")

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/register/ans', methods =['POST','GET'])
def register_ans():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    department = request.form['department']
    #write code to store this in database
    return render_template('registration.html', info="Registered successfully !!!!")

@app.route('/search', methods=['POST','GET'])
def search():
    query = request.form['search_query']
    return render_template('ans.html', info=query)

if __name__ == "__main__":
    app.run(debug=True)