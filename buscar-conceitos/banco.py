import sqlite3,os

path = os.path.join(os.path.dirname(__file__),'meu-banco.db')

conection = sqlite3.connect(path)
cursor = conection.cursor()

###########################################################

tbl_command = ''' CREATE TABLE IF NOT EXISTS Computador(
                id INTEGER NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                processador TEXT NOT NULL,
                memoria INTEGER NOT NULL,
                armazenamento INTEGER NOT NULL,
                monitor BOOLEAN NOT NULL,
                devicesI/O TEXT NOT NULL,

                PRIMARY KEY(id) AUTOINCREMENT
                );'''

insert_command = '''    INSERT INTO Computador
            VALUES(?,?,?,?,?,?,?);'''

###########################################################
cursor.execute(tbl_command)

cursor.execute(insert_command, (None,'Dell','Inspiron 15','Intel Core i7',16,512,True,'HDMI, USB-C'))   
conection.commit()

