from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('user-signup.html')

@app.route("/feedback", methods=['POST'])
def feedback():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    u_error = ''
    p_error = ''
    v_error = ''
    e_error = ''

    email_chars = list(email)
    username_chars = list(username)
    
    at_symbol = email_chars.count("@")
    dot_symbol = email_chars.count('.')

    if username == '':
        u_error += "Username can not be left blank. "
    elif 20 > len(username) < 3:
        u_error += "Username must be between 3 and 20 characters. "
    if " " in username_chars:
        u_error += "Username can not contain spaces. "

    if password == '':
        p_error += "Password can not be left blank. "
    
    if verify == '':
        v_error += "Verify password can not be left blank. "
    elif verify != password:
        v_error += "Passwords do not match."

    if at_symbol != 1 or dot_symbol != 1 or " " in email_chars:
        e_error += "Not a valid email address. "
    elif 20 > len(email) < 3:
        e_error += "Email should be between 3 and 20 characters. "

    if email == '':
        e_error = ''

    if u_error == '' and p_error == '' and v_error == '' and e_error == '':
        return redirect("/welcome?username={0}".format(username))

    return render_template('user-signup.html', username_error = u_error, password_error = p_error, verify_error = v_error, email_error = e_error, email_val = email, user_val = username)

@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    username = request.args.get("username")
    return render_template('welcome.html', new_username = username)

if __name__ == "__main__":
    app.run()