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

'''PEGA CONTA NO BD'''
@conta_bp.route('/form/<int:id>/edit', methods=['GET'])
def get_update(id):

    update = True

    connection = get_connection()

    sql = 'select * from contas where id={}'.format(int(id))

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    id = resultado[0][0]
    numero = resultado[0][1]
    titular = resultado[0][2]
    saldo = resultado[0][3]
    limite = resultado[0][4]

    connection.close()

    return render_template('form.html',
                           id=id,
                           numero=numero,
                           titular=titular,
                           saldo=saldo,
                           limite=limite,
                           update=update)

'''ATUALIZACAO DA CONTA'''
@conta_bp.route('/<int:id>/edit', methods=['POST'])
def update(id):

    connection = get_connection()

    numero = request.form.get('numero')
    titular = request.form.get('titular')
    saldo = float(request.form.get('saldo'))
    limite = float(request.form.get('limite'))

    sql = 'update contas set numero=%s, titular=%s, saldo=%s, limite=%s where id=%s;'
    valores = (numero, titular, saldo, limite, int(id))

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return redirect(url_for('contas.lista_contas'))

'''DELETA CONTA'''
@conta_bp.route('/<int:id>/remove')
def remove(id):

    connection = get_connection()

    sql = 'delete from contas where id={}'.format(int(id))

    cursor = connection.cursor()
    cursor.execute(sql)

    connection.commit()
    connection.close()

    return redirect(url_for('contas.lista_contas'))
