from flask import Flask, render_template, request
from simpleeval import simple_eval
import re
from math import sqrt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    visor = ''

    if request.method == 'POST':
        memoria = request.form.get('memoria', '')
        botao = request.form.get('botao')

        if botao == 'C':
            visor = ''
        elif botao == 'X':
            visor = memoria[:-1]
        elif botao == '=':
            conta = memoria
            conta = conta.replace('•', '*').replace('÷', '/').replace('²', '**2').replace('...', '').replace(',', '.')
            conta = re.sub(r'√([\d.]+)', r'sqrt(\1)', conta)

            try:
                resultado = simple_eval(conta, functions={"sqrt": sqrt})
                visor = str(resultado)

                if isinstance(resultado, float):
                    if '.' in visor and len(visor.split('.')[1]) > 5:
                        visor = f'{resultado:.5f}...'
            except:
                visor = 'Erro'
        else:
            visor = memoria + botao
    
    return render_template('index.html', resultado=visor)

if __name__ == '__main__':
    app.run(debug=True)
