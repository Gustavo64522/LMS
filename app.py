from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

user = os.environ.get("DB_USER")
pwd = os.environ.get("DB_PASS")
app = Flask(__name__)
# para fora da impacta: 200.49.54.234
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pymssql://{user}:{pwd}@sql.salas.aulas/fit_alunos"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.metadata.reflect(db.engine)

from lms.views import lms
app.register_blueprint(lms)

from curriculo.views import curriculo
app.register_blueprint(curriculo)