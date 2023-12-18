# -*- coding: UTF-8 -*-
class Calculator():

    def __init__(self) -> None:
        # Inicializa o objeto Calculator com inputs vazios
        self.currentInput = ''
        self.result = ''

    def atualizaDisplay(self, valor) -> str:
        # Atualiza o display da calculadora ao adicionar um valor à expressão atual
        expressao = self.currentInput
        expressao += str(valor)
        self.currentInput = expressao
        return expressao
    
    def limpaDisplay(self) -> None:
        # Limpa os inputs da calculadora
        self.currentInput = ''
        self.result = ''
    
    def calcularExpressao(self) -> str:
        # Tenta avaliar a expressão atual e atualiza o resultado e a expressão atual
        try:
            self.result = eval(self.currentInput)
            self.currentInput = str(self.result)

        except SyntaxError:
            # Se ocorrer um erro de sintaxe, define o resultado como 'Erro' e limpa a expressão atual
            self.result = 'Erro'
            self.currentInput = ''
        
    def limpaTecla(self) -> str:
        # Remove o último caractere da expressão atual
        self.currentInput = self.currentInput[:-1]
        return self.currentInput