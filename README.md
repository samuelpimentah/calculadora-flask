# Calculadora Flask

Desenvolvi esse projeto simples com o intuito de me familiarizar com o backend em Python utilizando o Flask como framework. se trata de uma calculadora web simples e funcional desenvolvida com Python e Flask. O projeto foca em uma interface limpa e no processamento seguro de expressões matemáticas no backend.

## Funcionalidades

- **Operações Básicas**: Soma, subtração, multiplicação e divisão.

- **Operações Avançadas**: Raiz quadrada e potência ao quadrado (x²).

- **Tratamento de Decimais**: Suporte para vírgula (padrão brasileiro) e arredondamento automático para dízimas longas.

- **Persistência de Estado**: O visor não reseta ao realizar operações sequenciais, mas limpa automaticamente ao atualizar a página (F5) via JavaScript.

- **Segurança**: Uso da biblioteca simpleeval para evitar a execução de código arbitrário no servidor.

## Tecnologias

- **Backend**: Python 3.x com Flask.

- **Frontend**: HTML5, CSS3 e JavaScript.

## Instalação e Configuração

Para evitar conflitos com as bibliotecas globais do seu sistema, recomendo o uso de um ambiente virtual (.venv).

- Clone o repositório:

    ```
    git clone https://github.com/samuelpimentah/calculadora-flask.git

    cd calculadora-flask
    ```

- Crie e ative o ambiente virtual:

    - Windows:

        ```
        python -m venv venv
        .\venv\Scripts\activate
        ```

    - Linux/macOS:

        ```
        python3 -m venv venv
        source venv/bin/activate
        ```

- Instale as dependências:
    ```
    pip install flask simpleeval
    ```

- Execute a aplicação:

    ```
    python app.py
    ```
    Ou abra o arquivo app.py clique no botão ▶️(run) no seu editor de código

    Acesse no seu navegador: http://127.0.0.1:5000
