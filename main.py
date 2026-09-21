import tkinter as tk
from pydoc import text
from tkinter import LabelFrame,Button,Label,PhotoImage
import random

def escolheu_pedra():
  jokenpo(escolha_usuario = 'pedra')

def escolheu_papel():
   jokenpo(escolha_usuario = 'papel')

def escolheu_tesoura():
   jokenpo(escolha_usuario = 'tesoura')

def jokenpo(escolha_usuario):
   escolha_computador = random.choice(['pedra','papel','tesoura'])

   if escolha_usuario == escolha_computador:
       menssagem = f"""
           Voce: {escolha_usuario.upper()}
           Eu: {escolha_computador.upper()}
           
           Resultado: EMPATE!
        """
   elif (
           (escolha_usuario == "pedra" and escolha_computador == "tesoura")
           or (escolha_usuario == "papel" and escolha_computador == "pedra")
           or (escolha_usuario == "tesoura" and escolha_computador == "papel")
   ):  # Correção na regra da tesoura (tesoura ganha de papel)
       menssagem = f"""
           Voce: {escolha_usuario.upper()}
           Eu: {escolha_computador.upper()}
           
           Resultado: VOCÊ GANHOU!
         """
   else:
       menssagem = f"""
            Voce: {escolha_usuario.upper()}
            Eu: {escolha_computador.upper()}
            
            Resultado: EU VENCI!
         """

   resultado.config(text = menssagem)

janela = tk.Tk()

Frame = LabelFrame (janela, text= 'Qual você escolhe?', padx=10 , pady=10)
Frame.pack()

icone_pedra = PhotoImage(file='png/pedra.png.png')
icone_tesoura = PhotoImage(file='png/tesoura.png.png')
icone_papel = PhotoImage(file='png/papel.png.png')

Button(Frame, text='pedra', command=escolheu_pedra,image=icone_pedra, compound=tk.LEFT).grid(column=1, row=1)
Button(Frame, text='papel', command=escolheu_papel,image=icone_papel,compound=tk.LEFT).grid(column=2, row=1)
Button(Frame, text='tesoura',command=escolheu_tesoura,image=icone_tesoura,compound=tk.LEFT).grid(column=3, row=1)

resultado = Label(Frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=3)

janela.title('pedra,papel,tesoura')
janela.geometry('500x200+700+200')
janela.mainloop()

