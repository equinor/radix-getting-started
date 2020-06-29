from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    user_id = request.headers.get('X-Forwarded-User')
    preferred_username = request.headers.get('X-Forwarded-Preferred-Username')
    email = request.headers.get('X-Forwarded-Email')
    return f"User ID: {user_id}<br />Preferred username: {preferred_username}<br />E-Mail: {email}"

try:
    app.run(host='0.0.0.0')
except InterruptedError:
    pass
