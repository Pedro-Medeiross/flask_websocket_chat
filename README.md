# Chat com Flask e WebSocket

Este é um projeto simples de chat em tempo real desenvolvido com Flask e Flask-SocketIO. Os usuários podem se conectar, enviar mensagens e excluí-las, com todas as interações sendo transmitidas em tempo real para todos os usuários conectados.

## Funcionalidades

- Entrada de nome do usuário antes de acessar o chat.
- Envio de mensagens em tempo real usando WebSockets.
- Transmissão de mensagens para todos os usuários conectados.
- Possibilidade de exclusão de mensagens (somente no lado do servidor).
- Interface simples e intuitiva.

## Tecnologias utilizadas

- **Flask**: Framework de microserviço Python utilizado para gerenciar rotas e a lógica do backend.
- **Flask-SocketIO**: Extensão usada para habilitar comunicação em tempo real via WebSockets.
- **HTML/CSS**: Interface simples para envio e exibição de mensagens.
- **Socket.IO**: Biblioteca utilizada para comunicação em tempo real no lado do cliente.

## Instalação e execução

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/chat-flask-socketio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd chat-flask-socketio
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux ou MacOS
    venv\Scripts\activate     # Windows
    ```

4. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute o servidor Flask:

    ```bash
    flask run
    ```

6. Acesse o chat no navegador em `http://127.0.0.1:5000`.

## Estrutura do projeto

/templates - Pasta de templates pra utilizar
main.py - Arquivo principal do projeto


## Como utilizar

1. Ao acessar a página inicial, o usuário deve inserir um nome.
2. Após a inserção do nome, o usuário será direcionado para a interface do chat.
3. As mensagens enviadas pelo formulário serão exibidas na tela e transmitidas em tempo real para todos os usuários conectados.
4. Mensagens podem ser excluídas (no lado do servidor), e a exclusão será refletida em todos os clientes.

## Requisitos

- Python 3.x
- Flask
- Flask-SocketIO

## Próximos passos

- Implementar autenticação de usuários.
- Permitir exclusão de mensagens pelos próprios usuários.
- Melhorar a interface visual do chat.

## Contribuições

Sinta-se à vontade para contribuir com melhorias, abrir issues ou enviar pull requests.