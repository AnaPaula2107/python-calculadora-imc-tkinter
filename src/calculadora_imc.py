# ctrl + ; = comentário

#Tkinter é a biblioteca padrão do Python para criar interfaces gráficas de usuário (GUIs).
# pip install tkinter
import tkinter as tk
from tkinter import messagebox

# Função para calcuçlar IMC

def calcular_imc(): #defina a função
    try: #tente fazer alguma coisa  
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc= peso / (altura**2)
        if imc < 18.5:
            resultado = f'IMC: {imc: .2f} Abaixo do peso' #não precisa concatenar e nem fazer str, o que está na chaves {} é a variável
        elif imc < 24.9:
            resultado = f'IMC: {imc: .2f} Peso normal'
        elif imc < 29.9:
            resultado = f'IMC: {imc: .2f} Sobre peso'
        elif imc < 34.9:
            resultado = f'IMC: {imc: .2f} Obesidade grau 1'
        elif imc < 39.9:
            resultado = f'IMC: {imc: .2f} Obesidade grau 2'
        else:
            resultado = f'IMC: {imc: .2f} Obesidade grau 3'
        
        #Exibir o resultgado    
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror('Erro!', 'Insira valores numéricos')

# Fim da função
# Configurar da janela principal
janela = tk.Tk()
janela.title('Calculadora de IMC') #título
janela.geometry('400x300') #tamanho da janela
janela.resizable(False,False) #não pode minimizar a tela

# Labels e entradas
label_titulo = tk.Label(janela, text='Calculadora de IMC', font=('arial',14, 'bold')) #título
label_titulo.pack(pady=10) #espaço entre as linhas px

# Label e entradas
label_peso = tk.Label(janela, text= 'Peso (kg): ')
label_peso.pack()
entry_peso= tk.Entry(janela)
entry_peso.pack()

# Label e entradas
label_altura = tk.Label(janela, text= 'Altura (m): ')
label_altura.pack()
entry_altura= tk.Entry(janela)
entry_altura.pack()

# Botão para calcular
botao_calcular=tk.Button(janela, text='Calcular IMC', command=calcular_imc)
botao_calcular.pack(pady=10)

# Label resultado
label_resultado = tk.Label(janela, text= '', font=('arial',12, 'bold'))
label_resultado.pack(pady=10)

# iniciar a janela
janela.mainloop()