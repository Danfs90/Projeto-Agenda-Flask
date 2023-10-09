import sqlite3
from flask import Flask, render_template, request, jsonify
from projeto_agenda.models.events import Events
from projeto_agenda.models.procedures import Procedures
from projeto_agenda.models.clients import Clients
from datetime import datetime, timedelta
from sqlalchemy import and_
from projeto_agenda import session
from datetime import datetime
app = Flask(__name__)

app.secret_key = "danilo.dev"


@app.route('/')
def index():
    calendar = session.query(Events).all()
    
    return render_template('index.html', calendar = calendar)

@app.route("/insert",methods=["POST","GET"])
def insert():
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']

        event = Events()
        event.title = title
        event.start_event = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        event.end_event = datetime.strptime(end,"%Y-%m-%d %H:%M:%S")
        session.add(event)
        msg = 'success'

    
    return jsonify(msg)

@app.route("/update",methods=["POST","GET"])
def update():
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        id = request.form['id']
        print(title) 
        print(start) 

        msg = 'success'
    return jsonify(msg) 

@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():
    if request.method == 'POST':
        
        getid = session.query(Events).get(request.form['id'])
        session.delete(getid)
        msg = 'Record deleted successfully'
    return jsonify(msg) 

@app.route("/procedures",methods=["GET"])
def get_procedures():
    if request.method == 'GET':
        procedures = session.query(Procedures).all()

        result = []
        for f_proc in procedures:
            proc_values ={
                "id": f_proc.id,
                "name_procedures": f_proc.name_procedures,
                "time": f_proc.time    
            }
            
            result.append(proc_values)
    
    return jsonify(result)

@app.route("/events/<string:data_escolhida>/<string:id_procedimentos>", methods=["GET"])
def get_events(data_escolhida, id_procedimentos):
    try:
        # Converte a data escolhida da string para um objeto datetime
        data_escolhida = datetime.strptime(data_escolhida, '%Y-%m-%dT%H:%M:%S.%fZ')

        # Define o horário de trabalho
        hora_inicio = datetime.strptime('09:00', '%H:%M')
        hora_fim = datetime.strptime('22:00', '%H:%M')

        # Calcula a duração total em minutos
        duracao_total = (hora_fim - hora_inicio).seconds // 60

        # Lista de IDs de procedimentos selecionados
        id_procedimentos = id_procedimentos.split(',')

        # Consulta o banco de dados para obter todos os eventos agendados para a data escolhida e os procedimentos selecionados
        eventos_agendados = session.query(Events).filter(
            Events.start_event >= data_escolhida,
            Events.start_event < data_escolhida + timedelta(days=1),
            Events.procedure_id.in_(id_procedimentos)
        ).all()

        # Duração de cada procedimento em minutos
        duracao_procedimentos = {
            1: 45,
            2: 75,
            3: 60,
            4: 15,
            5: 90
        }

        # Calcula a quantidade de cada procedimento já agendado
        procedimentos_disponiveis = {id_procedimento: 0 for id_procedimento in id_procedimentos}

        # Calcula a duração total dos procedimentos selecionados
        duracao_total_selecionada = sum(duracao_procedimentos.get(int(id), 0) for id in id_procedimentos)

        # Calcula a quantidade de procedimentos disponíveis com base no horário de trabalho e na seleção
        quantidade_disponivel = duracao_total // duracao_total_selecionada

        # Calcula os horários disponíveis para a seleção de procedimentos
        horarios_disponiveis = []
        horario_atual = hora_inicio
        for _ in range(quantidade_disponivel):
            horarios_disponiveis.append(horario_atual.strftime('%H:%M'))
            horario_atual += timedelta(minutes=duracao_total_selecionada)

        return jsonify({
            "horarios_disponiveis": horarios_disponiveis,
            "quantidade_agendada": procedimentos_disponiveis,
            "quantidade_disponivel": quantidade_disponivel
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)