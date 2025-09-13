#Arquivo para o GUI

import tkinter as tk
from tkinter import ttk
from conversor import principal

"""Aqui eu crio a janela principal, fixo o tamanho dela, crio o título e bloqueio
para redimensionamento"""
root = tk.Tk()
root.geometry('600x600+300+300')
root.title("Conversor de temperatura")
root.resizable(False, False)

#Aqui eu crio o painel onde será mostrado o resultado
painel = ttk.LabelFrame(root, text="Veja aqui a conversão")
painel.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

#Aqui eu crio a variável para armazenar a informação do Label
temp_var = tk.StringVar()

#Aqui eu crio o Label que vai mostrar o resultado
mostrador = tk.Label(painel, textvariable=temp_var,font=('Arial', 48), fg='lime',
                     bg='black')
mostrador.grid(row=0, column=0, sticky='snew', padx=20, pady=20)

#Aqui eu crio um painel para colocar a entrada de dados
painel_entrada = ttk.LabelFrame(root, text='Digite aqui a temperatura para ' \
'conversão')
painel_entrada.grid(row=1, column=0, sticky='snew', padx=20, pady=20)

#Aqui eu crio a variável de controle para armazenar o número digitado pelo usuário
digt_var = tk.DoubleVar()

#Aqui eu crio a entrada de números para digitar a temperatura desejada
entrada = ttk.Entry(painel_entrada, textvariable=digt_var)
entrada.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

#Aqui eu crio um painel para colocar os radiobuttons das opções
opções = ttk.LabelFrame(root, text='Escolha uma opção:')
opções.grid(row=2, column=0, sticky='nsew', padx=20, pady=20)

#Aqui eu crio uma variável de controle para os radiobuttons
opc_cels_faren = tk.BooleanVar()

#Aqui eu crio o radiobutton para opção celsius-farenheit
cels_faren = ttk.Radiobutton(opções, text="Conversão de Celsius para Farenheit",
                             variable=opc_cels_faren, value=True)
cels_faren.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

#Aqui eu crio o radiobutton para opção farenheit-celsius
faren_cels = ttk.Radiobutton(opções, text="Conversão de Farenheit para Celsius",
                             variable=opc_cels_faren, value=False)
faren_cels.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

#Aqui eu crio e fixo o botão para realizar a operação de conversão
botão = ttk.Button(root, text='Converter', command=lambda: 
                   principal(opc_cels_faren, digt_var, temp_var))
botão.grid(row=5, column=0, sticky='nsew', padx=20, pady=20)

root.mainloop()