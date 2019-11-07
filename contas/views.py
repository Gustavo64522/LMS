from flask import Blueprint, render_template, url_for, redirect
from contas.forms import FormRegistro


contas = Blueprint('contas', __name__,
                   url_prefix='/contas',
                   template_folder='templates',
                   static_folder='static')


@contas.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form_registro = FormRegistro()
    if form_registro.validate_on_submit():
        # criar o usuario
        print('Criei o usuario')
        return redirect(url_for('lms.index'))
    return render_template('registrar.html', user=None, form=form_registro)