from flask import Flask, request, render_template_string, make_response

app = Flask(__name__)
app.secret_key = "hardcoded-secret-key"

@app.route('/')
def home():
    return render_template_string("""
        <h1>Search</h1>
        <form action='/search' method='get'>
            <input name='q' placeholder='Type anything…'>
            <button type='submit'>Search</button>
        </form>
    """)

@app.route('/search')
def search():
    q = request.args.get("q", "")
    return render_template_string(f""" 
        <h1>Search Results</h1>
        <p>Your query was: <strong>{q}</strong></p>
        <a href='/'>Back</a>
    """)

@app.route('/login')
def login():
    resp = make_response("Logged in – insecure cookie set!")
    resp.set_cookie("session", "fake-session-token")
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
