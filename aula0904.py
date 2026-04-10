
#aula0904:

import tkinter as tk
import sqlite3


connection = sqlite3.connect("ex.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Credenciais(usr TEXT, pwd TEXT)")
#cursor.execute("INSERT INTO Credenciais VALUES ('teste', '123')")
connection.commit()
def VerificaCredenciais():
    usr = username_entry.get()
    pwd = password_entry.get()
    
    res = cursor.execute("SELECT * FROM Credenciais WHERE usr = '"+usr+"' and pwd = '"+pwd+"'").fetchall()
    if res == []:
        print("Usuário não encontrado")
    else:
        print("Entrou")

def new_user():
    usr = userc_entry.get()
    pwd = passc_entry.get()
    
    if cursor.execute("INSERT INTO Credenciais VALUES (?,?)",(usr,pwd)):
        connection.commit()
        print("cadastrado")


parent = tk.Tk()
parent.title("Login Form")
TelaCadastro = tk.Tk()
TelaCadastro.title("Tela de cadastro")

username_label = tk.Label(parent, text="Userid:")
username_label.pack()

userc_label = tk.Label(TelaCadastro,text="new user:")
userc_label.pack()

userc_entry = tk.Entry(TelaCadastro)
userc_entry.pack()

passc_label = tk.Label(TelaCadastro, text="new senha:")
passc_label.pack()

passc_entry = tk.Entry(TelaCadastro)
passc_entry.pack()

cadastrar_button = tk.Button(TelaCadastro,text="cadastrar",command=new_user)
cadastrar_button.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

login_button = tk.Button(parent, text="Login", command=VerificaCredenciais)
login_button.pack()

parent.mainloop()
