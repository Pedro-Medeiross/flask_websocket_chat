from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configura a chave secreta usada pelo Flask para coisas como sessões e segurança
app.config['SECRET_KEY'] = 'secret!'

# Inicializa o SocketIO com o aplicativo Flask
socketio = SocketIO(app)

# Armazena todas as mensagens enviadas pelos usuários
messages = []

# Rota principal que renderiza a página 'index.html'
@app.route('/')
def index():
    return render_template('index.html')

# Evento que trata quando um usuário se conecta ao servidor via SocketIO
@socketio.on('connect')
def handle_connect():
    print(f"Connected")  # Exibe no console quando um usuário se conecta

# Evento que trata quando uma mensagem é recebida do cliente
@socketio.on('message')
def handle_message(data):
    # Extrai o nome do usuário e a mensagem enviada dos dados recebidos
    name = data.get('name')
    message = data.get('message')
    
    # Gera um ID único para a mensagem baseado no comprimento da lista de mensagens
    msg_id = str(len(messages))  # ID simples baseado na contagem de mensagens
    
    # Adiciona a nova mensagem na lista de mensagens armazenadas
    messages.append({'name': name, 'message': message, 'id': msg_id})
    
    # Envia a mensagem para todos os clientes conectados (broadcast)
    send({'name': name, 'message': message, 'id': msg_id}, broadcast=True)

# Evento que trata a exclusão de uma mensagem
@socketio.on('delete')
def handle_delete(msg_id):
    global messages
    # Filtra a lista de mensagens para remover a que tem o ID fornecido
    messages = [msg for msg in messages if msg['id'] != msg_id]
    
    # Emite um evento para todos os clientes notificando que a mensagem foi deletada
    emit('delete_message', msg_id, broadcast=True)

# Inicia o servidor Flask com SocketIO
if __name__ == '__main__':
    socketio.run(app, debug=True)