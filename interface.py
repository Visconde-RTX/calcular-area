import tkinter as tk
from tkinter import ttk

from retangulo import Retangulo
from circulo import Circulo
from triangulo import Triangulo
from quadrado import Quadrado


def calcular():

    forma = forma_var.get()

    try:

        if forma == "Retangulo":
            base = float(entry1.get().replace(",","."))
            altura = float(entry2.get().replace(",","."))

            r = Retangulo(base, altura)
            #adcionar o calcular_perimetro dps e lebrar de muadar o 'resultado' por 'area' e 'perimetro'
            resultado = r.calcular_area()

        elif forma == "Circulo":
            raio = float(entry1.get().replace(",","."))

            c = Circulo(raio)
            resultado = c.area()

        elif forma == "Triangulo":
            base = float(entry1.get().replace(",","."))
            altura = float(entry2.get().replace(",","."))

            t = Triangulo(base, altura, 0)
            resultado = t.area()

        elif forma == "Quadrado":
            lado = float(entry1.get().replace(",","."))

            q = Quadrado(lado)
            resultado = q.area()

        label_resultado.config(text=f"Resultado: {resultado}")

    except Exception as erro:
        label_resultado.config(text=f"Erro: {erro}")


def atualizar_campos(event):

    forma = forma_var.get()

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

    if forma == "Retangulo":
        label1.config(text="Base")
        label2.config(text="Altura")
        label2.grid()
        entry2.grid()

    elif forma == "Triangulo":
        label1.config(text="Base")
        label2.config(text="Altura")
        label2.grid()
        entry2.grid()

    elif forma == "Circulo":
        label1.config(text="Raio")
        label2.grid_remove()
        entry2.grid_remove()

    elif forma == "Quadrado":
        label1.config(text="Lado")
        label2.grid_remove()
        entry2.grid_remove()


janela = tk.Tk()
janela.title("Calculadora de Área")
janela.geometry("300x250")

tk.Label(janela, text="Escolha a forma").grid(row=0, column=0, pady=10)

forma_var = tk.StringVar()

combo = ttk.Combobox(
    janela,
    textvariable=forma_var,
    values=["Retangulo", "Circulo", "Triangulo", "Quadrado"]
)

combo.grid(row=0, column=1)
combo.bind("<<ComboboxSelected>>", atualizar_campos)


label1 = tk.Label(janela, text="Valor 1")
label1.grid(row=1, column=0)

entry1 = tk.Entry(janela)
entry1.grid(row=1, column=1)


label2 = tk.Label(janela, text="Valor 2")
label2.grid(row=2, column=0)

entry2 = tk.Entry(janela)
entry2.grid(row=2, column=1)


botao = tk.Button(janela, text="Calcular", command=calcular)
botao.grid(row=3, column=0, columnspan=2, pady=15)


label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=4, column=0, columnspan=2)


janela.mainloop()
#adicionar  depois a opção de escolher a unidade de medida
#deixar o campo de selecionar forma obrigatorio(se possivel)
#adcionar o enter para pular de campo e tbm mostrar o resultado
#tentar esconder o 'valor 1' e o 2 quando n estiver selecionado a forma
#e tambem adcionar o perimetro das outras formas :)