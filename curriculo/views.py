from flask import Blueprint
from curriculo.curso import Curso


curriculo = Blueprint('curriculo', __name__,
                      url_prefix='/cursos',
                      static_folder='static',
                      template_folder='templates')

@curriculo.route('/<sigla>')
def curso(sigla):
    return sigla

@curriculo.app_context_processor
def lista_curso():
    return {"cursos_menu": Curso.query.all()}