from flask import Flask
from flask import render_template
import pymysql

app = Flask(__name__,template_folder='template') # Inicializa a aplicação

mydatabase = pymysql.connect(host='localhost',
                       user='bia2',
                       passwd='Oneeminem30@',
                       db='consultaCpf',
                       charset='utf8')

cursor = mydatabase .cursor()


@app.route('/<int:cpf>',methods = ['GET', 'POST'])
def buscando_dados_cpf(cpf):
  cursor.execute("SELECT cpf FROM consultar")

  myresult = cursor.fetchall()

  for c in myresult:

    if cpf == c[0]:
      cursor.execute("SELECT nome FROM consultar where cpf = {}".format(cpf))
      nome = cursor.fetchall()
      cursor.execute("SELECT data_nascimento FROM consultar where cpf = {}".format(cpf))
      data = cursor.fetchall()
      texto = 'nome {} data nascimento {}'.format(nome[0][0],data[0][0])

  return render_template('index.html',texto=texto)

if __name__ == '__main__':
  app.run(debug=True,port=3030,host="0.0.0.0")