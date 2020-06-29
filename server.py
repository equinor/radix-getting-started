from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello, World!"

try:
    app.run(host='0.0.0.0')
except InterruptedError:
    pass
