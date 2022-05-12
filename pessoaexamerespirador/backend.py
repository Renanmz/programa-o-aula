from config import *
from modelo import Pessoa, ExameRealizado, Respirador, Exame
from datetime import date

@app.route("/")
def inicio():
    return 'Sistema de cadastro. '+\
        '<a href="/listar_exames">Operação listar</a>'


@app.route("/listar_exames")
def listar_exames():
    exames = db.session.query(ExameRealizado).all()
    exames_em_json = [ x.json() for x in exames ]
    resposta = jsonify(exames_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/incluir_exame", methods=['post'])
def incluir_exame():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    partes = dados['date'].split("-")
    dados['data'] = date(int(partes[0]), int(partes[1]), int(partes[2]))
    try:
      nova = ExameRealizado(**dados)
      db.session.add(nova)
      db.session.commit() 
    except Exception as e: 

      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/listar_respiradores")
def listar_respiradores():
    respiradores = db.session.query(Respirador).all()
    respiradores_em_json = [ x.json() for x in respiradores ]
    resposta = jsonify(respiradores_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/incluir_respirador", methods=['post'])
def incluir_respirador():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    partes = dados['data_aquisicao'].split("-")
    dados['data_aquisicao'] = date(int(partes[0]), int(partes[1]), int(partes[2]))
    partes2 = dados['data_emprestimo'].split("-")
    dados['data_emprestimo'] = date(int(partes2[0]), int(partes2[1]), int(partes2[2]))
    try:
      nova = Respirador(**dados)
      db.session.add(nova)
      db.session.commit() 
    except Exception as e: 

      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 