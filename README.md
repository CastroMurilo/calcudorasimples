# Calculadora Simples em Tkinter

Este é um código simples em Python utilizando a biblioteca Tkinter para criar uma interface gráfica de uma calculadora. A calculadora realiza operações básicas de adição, subtração, multiplicação e divisão.

## Funcionalidades

### Atualizar Display
A função `atualizar_display(valor)` é responsável por adicionar o valor clicado na calculadora ao display.

### Calcular Resultado
A função `calcular()` utiliza a expressão presente no display e realiza o cálculo. O resultado é exibido no display. Em caso de erro durante o cálculo, a mensagem "Erro" é exibida.

### Limpar Display
A função `limpar_display()` limpa o conteúdo do display.

## Interface Gráfica
A janela principal da interface possui um display para mostrar a expressão e o resultado, além de botões para os dígitos de 0 a 9, operadores (+, -, *, /), ponto decimal, e um botão de igual para calcular o resultado. Há também um botão "C" para limpar o display.

## Como Utilizar
1. Execute o código em um ambiente Python.
2. A interface da calculadora será exibida.
3. Clique nos botões numéricos e operadores para formar a expressão desejada.
4. Clique no botão "=" para calcular o resultado.
5. Para limpar o display, clique no botão "C".
6. Também é possível clicar na tecla ← para deletar apenas um caractere da expressão.

## Observações
- Este código utiliza a função `eval()`. Embora seja uma solução simples, é importante considerar questões de segurança ao lidar com expressões avaliadas dinamicamente.
- Caso ocorra um erro durante o cálculo, a mensagem "Erro" será exibida no display.

Sinta-se à vontade para explorar e modificar o código conforme necessário!