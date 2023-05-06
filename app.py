from flask import Flask, render_template , request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.debug = True

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    prompt = story.prompts 
    return render_template("madlib.html", prop = prompt)

@app.route('/mad')
def stories(): 
    text = story.generate(request.args)
    return render_template("madlib_stories.html", text = text)