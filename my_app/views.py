from flask import render_template, Blueprint, request, redirect, url_for
from my_app.models import Conta
from my_app.db import get_connection

conta_bp = Blueprint('contas', __name__, url_prefix='/contas')

'''LISTA CONTAS'''
@conta_bp.route('/lista')
def lista_contas():
    connection = get_connection()

    sql = 'select * from contas'

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    contas = []
    for registro in resultado:
        conta = Conta(registro[1], registro[2], registro[3], registro[4], registro[0])
        contas.append(conta)

    connection.close()

    return render_template('lista.html', contas=contas)

'''FORM CONTAS'''
@conta_bp.route('/form')
def formulario():
    return render_template('form.html')

'''CRIA CONTAS'''
@conta_bp.route('/cria-conta', methods=['POST'])
def cria():
    numero = request.form.get('numero')
    titular = request.form.get('titular')
    saldo = float(request.form.get('saldo'))
    limite = float(request.form.get('limite'))

    conta = Conta(numero, titular, saldo, limite)

    connection = get_connection()

    sql = 'insert into contas (numero, titular, saldo, limite) values (%s, %s, %s, %s)'
    valores = (conta.numero, conta.titular, conta.saldo, conta.limite)

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return redirect(url_for('contas.lista_contas'))
