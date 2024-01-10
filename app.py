"""A simple Flask app for generating Madlibs"""

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)

@app.route("/")
def show_form():
    """Show a form prompting user for content to fill in the Madlib"""
    return render_template("index.html",prompt_list=story.prompts)

@app.route("/story")
def show_story():
    """Display the user-generated story on the page"""
    args = {}
    for arg in request.args:
        args[arg] = request.args.get(arg)
    story_text = story.generate(args)
    return render_template("/story.html",story=story_text)