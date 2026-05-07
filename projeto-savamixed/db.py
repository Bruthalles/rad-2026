import sqlite3,os
from classes.Classes import Pessoa, Veiculo, Marca
######################################################################
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

insert_pessoa_command = '''INSERT INTO Pessoa 
            VALUES(:id,:cpf,:nome,:nascimento,:usa_oculos);'''

insert_carro_command = '''INSERT INTO Veiculo
            VALUES(:placa,:ano,:cor,:motor,:proprietario,:marca);'''

insert_marca_command = '''INSERT INTO Marca
            VALUES(:id,:nome,:sigla);'''

########################################################################

pessoa = Pessoa(id=11,cpf=11231111,nome='sonaldo',nascimento='2005-04-02',usa_oculos=False)

carro = Veiculo(placa='vTv-2009',ano=2010,cor='branco',motor=5.0,proprietario=44332211,marca=4)

marca1 = Marca(id=4,nome="ferrari",sigla="FR")

########################################################################
try:

    path = os.path.join(os.path.dirname(__file__),'meu-banco.db')

    conection = sqlite3.connect(path)

    cursor = conection.cursor()

    # cursor.execute(tbl_pessoa_command)
    # cursor.execute(tbl_veiculo_command)
    # cursor.execute(tbl_marca_command)

    cursor.execute(insert_pessoa_command, vars(pessoa))
    # print("pessoa em dicionario: ",vars(pessoa))    
    # print("\npessoa normal: ",pessoa)
    cursor.execute(insert_carro_command, vars(carro))
    cursor.execute(insert_marca_command, vars(marca1))
    
    conection.commit()

except sqlite3.DatabaseError as err:
    print("Erro com banco de dados.", err)

finally:

    if conection:

        cursor.close()
        conection.close()