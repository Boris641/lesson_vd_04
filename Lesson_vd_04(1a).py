from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Date and Time</title>
    </head>
    <body>
        <h1>Текущая дата и время</h1>
        <p>{{ current_time }}</p>
    </body>
    </html>
    """, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
