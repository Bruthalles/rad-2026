class Pessoa:
    def __init__(self,id,cpf,nome,nascimento,usa_oculos):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.usa_oculos = usa_oculos

    def __str__(self):
        return f"Id:{self.id}, CPF:{self.cpf}, Nome:{self.nome}, Nascimento:{self.nascimento}, Usa oculos: {self.usa_oculos}"

class Veiculo:
    def __init__(self,placa,ano,cor,motor,proprietario,marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.proprietario = proprietario
        self.marca = marca

class Marca:
    def __init__(self,id,nome,sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla