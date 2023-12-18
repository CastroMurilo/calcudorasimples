# -*- coding: UTF-8 -*- 
import tkinter as tk
from calculator import Calculator

class CalculatorApp:
    def __init__(self, janela):
        # Inicializa a instância da calculadora
        self.calculadora = Calculator()

        # Configurações da janela principal
        janela.title("Calculadora")
        janela.geometry("300x490")

        # Variável para armazenar a expressão a ser exibida no display
        self.display_var = tk.StringVar()

        # Configuração e criação do display da calculadora
        display = tk.Entry(janela, textvariable=self.display_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, justify='right')
        display.grid(row=0, column=0, columnspan=4)

        # Definição dos botões da calculadora
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Criação dos botões e associação com funções correspondentes
        for (texto, linha, coluna) in botoes:
            tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 18), command=lambda t=texto: self.atualizar_display(t) if t != '=' else self.calcular()).grid(row=linha, column=coluna)

        # Botão "C" para limpar o display
        tk.Button(janela, text='C', padx=20, pady=20, font=("Arial", 18), command=self.limpar_display).grid(row=5, column=0)

        # Botão para backspace
        tk.Button(janela, text='←', padx=20, pady=20, font=("Arial", 18), command=self.limpar_tecla).grid(row=5, column=1)

    def atualizar_display(self, valor):
        # Atualiza o display com o valor fornecido pela interação com os botões
        expressao = self.calculadora.atualizaDisplay(valor)
        self.display_var.set(expressao)

    def calcular(self):
        # Calcula a expressão atual e atualiza o display
        self.calculadora.calcularExpressao()
        self.display_var.set(self.calculadora.currentInput)

    def limpar_display(self):
        # Limpar todo o display
        self.calculadora.limpaDisplay()
        self.display_var.set("")

    def limpar_tecla(self):
        # Limpa o último caractere da expressao
        currentInput = self.calculadora.limpaTecla()
        self.display_var.set(currentInput)

if __name__ == "__main__":
    # Cria e inicia a aplicação
    janela = tk.Tk()
    app = CalculatorApp(janela)
    janela.mainloop()