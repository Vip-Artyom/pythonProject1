from flask import Flask
from utils1 import *

app = Flask(__name__)


@app.route("/")
def page_main():
    return get_candidate(all_candidates)


@app.route("/candidate/<id>")
def page_candidate(id):
    return get_candidate_id(id, all_candidates)


@app.route("/skills/<skill>")
def page_skills(skill):
    return get_candidate_skills(skill, all_candidates)


app.run()
