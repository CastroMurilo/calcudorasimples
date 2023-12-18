import tkinter as tk

# Função para atualizar a expressão na tela
def atualizar_display(valor):
    expressao = display_var.get()
    expressao += str(valor)
    display_var.set(expressao)

# Função para calcular o resultado
def calcular():
    try:
        expressao = display_var.get()
        resultado = eval(expressao)
        display_var.set(resultado)
    except Exception as e:
        display_var.set("Erro")

# Função para limpar o display
def limpar_display():
    display_var.set("")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("800x1000")

# Variável para armazenar a expressão
display_var = tk.StringVar()

# Display da calculadora
display = tk.Entry(janela, textvariable=display_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (texto, linha, coluna) in botoes:
    tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 18), command=lambda t=texto: atualizar_display(t) if t != '=' else calcular()).grid(row=linha, column=coluna)

# Botão "C" para limpar o display
tk.Button(janela, text='C', padx=20, pady=20, font=("Arial", 18), command=limpar_display).grid(row=5, column=0)

janela.mainloop()

