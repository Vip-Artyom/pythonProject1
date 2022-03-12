from flask import Flask
from utils1 import get_candidate

app = Flask(__name__)

@app.route("/")
def page_index():
   for candidate in get_candidate():
      return f'<pre>Имя кандидата - {candidate["name"]}\n' \
             f'Позиция кандидата - {candidate["position"]}\n' \
             f'Навыки через запятую - {candidate["skills"]}</pre>'

app.run()