import tkinter as tk
from tkinter import ttk

from retangulo import Retangulo
from circulo import Circulo
from triangulo import Triangulo
from quadrado import Quadrado

def verificar(event, campo_atual, proximo_campo):

    valor = campo_atual.get().strip()

    if valor == "":
        label_resultado.config(text="O campo num pode ficar vazio não, meu nobre")
        return "break"
    
    try:
        float(valor.replace(",", "."))
        label_resultado.config(text="")
        proximo_campo.focus()
    except:
        label_resultado.config(text="Digite apenas números, lil bro")
        return "break"


def calcular():

    forma = forma_var.get()

    if entry1.get().strip() == "":
        label_resultado.config(text="Preencha o primeiro campo.")
        return

    if entry2.winfo_ismapped() and entry2.get().strip() == "":
        label_resultado.config(text="Preencha o segundo campo.")
        return

    try:

        if forma == "Retangulo":
            base = float(entry1.get().replace(",","."))
            altura = float(entry2.get().replace(",","."))

            r = Retangulo(base, altura)
            resultado = r.calcular_area()
            resultado2 = r.calcular_perimetro()

        elif forma == "Circulo":
            raio = float(entry1.get().replace(",","."))

            c = Circulo(raio)
            resultado = c.calcular_areaC()
            resultado2 = c.calcular_perimetroC()

        elif forma == "Triangulo":
            base = float(entry1.get().replace(",","."))
            altura = float(entry2.get().replace(",","."))

            t = Triangulo(base, altura, 0)
            resultado = t.calcular_areaT()
            resultado2 = None

        elif forma == "Quadrado":
            lado = float(entry1.get().replace(",","."))

            q = Quadrado(lado)
            resultado = q.calcular_areaQ()
            resultado2 = q.calcular_perimetroQ()

        label_resultado.config(text=f"Área: {resultado:.2f}" )

        if resultado2 is not None:
            label_resultado2.config(text=f"Perímetro: {resultado2:.2f}")
        else:
             label_resultado2.config(text="Ninguém consegue calcular  perimetro do \n triangulo com dois valores, com exeção, é claro, \n de Satoru Gojo")

    except Exception as erro:
        label_resultado.config(text=f"Erro: {erro}")


def atualizar_campos(event):

    forma = forma_var.get()
    label_resultado.config(text="")

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

    if forma == "Retangulo":
        label1.config(text="Base")
        label2.config(text="Altura")

        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()

    elif forma == "Triangulo":
        label1.config(text="Base")
        label2.config(text="Altura")

        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()

    elif forma == "Circulo":
        label1.config(text="Raio")

        label1.grid()
        entry1.grid()
        label2.grid_remove()
        entry2.grid_remove()

    elif forma == "Quadrado":
        label1.config(text="Lado")

        label1.grid()
        entry1.grid()
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

entry1.bind("<Return>", lambda e:  calcular() if not entry2.winfo_ismapped() else verificar(e, entry1, entry2))
entry2.bind("<Return>", lambda e: calcular())

entry1.grid_remove()
label1.grid_remove()
entry2.grid_remove()
label2.grid_remove()


botao = tk.Button(janela, text="Calcular", command=calcular)
botao.grid(row=3, column=0, columnspan=2, pady=15)


label_resultado = tk.Label(janela, text="Escolha uma forma para começar")
label_resultado.grid(row=4, column=0, columnspan=2)

label_resultado2 = tk.Label(janela, text="")
label_resultado2.grid(row=5, columnspan=2)


janela.mainloop()
#adicionar  depois a opção de escolher a unidade de medida
#todas as metas foram compridas, com exeção é klaro de adicionar a unidade de medida