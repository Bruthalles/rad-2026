#fazer uma interface com dois botoes
#1- uma funçao lambda
#2- funcao nomeada
#funcao lambda conta ate n e prints
# funcao nomeada aumenta n em 1
#n começa = 10

import tkinter as tk
x =0
n = 10
def incrementa_n(x):
    x += 1

def ligaled():
    print("liga led")

def exemplo():
    root = tk.Tk()
    root.title("ola mundo")
    root.resizable(True,True)

    contagem = tk.Button(root, text="contar ate 10")
    contagem['command'] = lambda : print(x+1)
    contagem.pack() 
    #test = tk.Button(root, title="Ligaled")
    #test['command'] = ligaled
    #test.pack()

    root.mainloop()

if __name__ == '__main__':
    exemplo()