import tkinter as tk

home = tk.Tk()
home.title("SavaMixed")
home.geometry("400x300")

usuario = tk.Entry(home,textvariable="usuario")
usuario.pack()

senha = tk.Entry(home,textvariable="senha", show="*")
senha.pack()

botao_login = tk.Button(home, text="Login")
botao_login.pack()

home.mainloop()