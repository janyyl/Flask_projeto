from flask import Flask, render_template, request, redirect, url_for
import random
from validate_docbr import CPF, CNPJ

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/geradordecpf")
def gerador_de_cpf():
    cpf = CPF()
    roleta_russa = random.randint(0, 1)
    if roleta_russa == 0:
        cpf = random.randint(11111111111, 99999999999)
        return render_template("gerador_de_cpf.html", cpf = str(cpf))
    else:
        cpf = cpf.generate(True)
        return render_template("gerador_de_cpf_valido.html", cpf = cpf)

@app.route("/geradordecnpj")
def gerador_de_cnpj():
    cnpj = CNPJ()
    roleta_russa = random.randint(0, 1)
    if roleta_russa == 0:
        cnpj = random.randint(11111111111111, 99999999999999)
        return render_template("gerador_de_cnpj.html", cnpj = str(cnpj))
    else:
        cnpj = cnpj.generate(True)
        return render_template("gerador_de_cnpj_valido.html", cnpj = cnpj)

@app.route("/validadordecpf")
def validador_de_cpf():
    return render_template("validar_cpf.html")

@app.route("/validadordecnpj")
def validador_de_cnpj():
    return render_template("validar_cnpj.html")

# POST
@app.route("/verificacao_cpf", methods=["POST"])
def verificar_cpf():
    cpf = CPF()
    cpf_usuario = request.form["cpf"]
    if cpf.validate(cpf_usuario):
        return render_template("verificacao_cpf.html", link = "/validadordecpf", validador = "Valido", cpf = str(cpf.mask(cpf_usuario)) )
    else:
        return render_template("verificacao_cpf.html", link = "/validadordecpf", validador = "Invalido", cpf = "")
    
@app.route("/verificacao_cnpj", methods=["POST"])
def verificar_cnpj():
    cnpj = CNPJ()
    cnpj_usuario = request.form["cnpj"]
    if cnpj.validate(cnpj_usuario):
        return render_template("verificacao_cnpj.html", link = "/validadordecnpj", validador = "Valido", cnpj = str(cnpj.mask(cnpj_usuario)) )
    else:
        return render_template("verificacao_cnpj.html", link = "/validadordecnpj", validador = "Invalido", cnpj = "")
    
app.run()