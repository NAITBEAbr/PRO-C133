# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():
    nome = "Carlos Eduardo" 
    idade = "16" 

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai():
    nome_pai = "Lynce Luciano Reis Ferreira" 
    idade_pai = "38" 
    return render_template('pai.html', nome_pai=nome_pai, idade_pai=idade_pai)


# defina a rota para a página da mãe
@app.route("/mae")
def mae():
    nome_mae = "Mayara Pereira Viana"  
    idade_mae = "34"  
    return render_template('mae.html', nome_mae=nome_mae, idade_mae=idade_mae)


# defina a rota para a página do amigo
@app.route("/amigo")
def amigo():
    nome_amigo = "Marcus Antonio Folador"  
    idade_amigo = "15"  
    return render_template('amigo.html', nome_amigo=nome_amigo, idade_amigo=idade_amigo)

# adicione outras rotas, se você quiser

# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
