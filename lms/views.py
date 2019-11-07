from flask import Blueprint, render_template


lms = Blueprint('lms', __name__,
                static_folder='static',
                template_folder='templates',
                static_url_path='/lms/static')


@lms.route('/')
def index():
    return render_template('index.html', user=None)


@lms.route('/contato')
def contato():
    return "tem que fazer a pagina"