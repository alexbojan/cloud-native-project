
from flask import Flask, render_template_string
import os

app = Flask(__name__)
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

@app.route('/score')
def score_server():
    try:
        # Read the score from the Scores.txt file
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                score = file.read().strip()
        else:
            score = "0"
        # Return the HTML with the score
        return render_template_string(f'''
        <html>
         <head>
         <title>Scores Game</title>
         </head>
         <body>
         <h1>The score is <div id="score">{score}</div></h1>
         </body>
        </html>
        ''')
    except Exception as e:
        # Return error HTML
        return render_template_string(f'''
        <html>
         <head>
         <title>Scores Game</title>
         </head>
         <body>
         <h1><div id="score" style="color:red">ERROR: {e}</div></h1>
         </body>
        </html>
        ''')

if __name__ == '__main__':
    app.run(debug=True)
