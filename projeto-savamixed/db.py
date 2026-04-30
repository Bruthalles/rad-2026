import sqlite3

tbl_pessoa_command = ''' CREATE TABLE Pessoa(
                id INTEGER NOT NULL,
                cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf)
               );
                '''

tbl_veiculo_command = ''' CREATE TABLE Veiculo(
                placa CHAR(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                motor REAL NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY(placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id) 
               );
                '''

tbl_marca_command = ''' CREATE TABLE Marca(
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY (id)
               );
                '''

class Pessoa:
    def __init__(self,id,cpf,nome,nascimento,usa_oculos):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.usa_oculos = usa_oculos
        
    def __str__(self):
        return f"Id:{self.id}, CPF:{self.cpf}, Nome:{self.nome}, Nascimento:{self.nascimento}, Usa oculos: {self.usa_oculos}"


pessoa = Pessoa(9,19344594,'thalles','2005-04-02',True)


command = '''INSERT INTO Pessoa 
            VALUES(:id,:cpf,:nome,:nascimento,:usa_oculos);'''

try:
    conection = sqlite3.connect("meu-banco.db")

    cursor = conection.cursor()
    cursor.execute(command, vars(pessoa))
    print("pessoa em dicionario: ",vars(pessoa))    
    print("\npessoa normal: ",pessoa)
    
    
    conection.commit()

except sqlite3.DatabaseError as err:
    print("Erro com banco de dados.", err)

finally:

    if conection:

        cursor.close()
        conection.close()