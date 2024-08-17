import tkinter as tk

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura_cm = float(entrada_altura.get())
        altura_m = altura_cm / 100
        
        if peso <= 0 or altura_m <= 0:
            tk.messagebox.showerror("Erro", "Peso e altura devem ser maiores que zero.")
            return
        
        imc = peso / (altura_m ** 2)
        resultado = f"Seu IMC é: {imc:.2f}"
        
        if imc < 18.5:
            resultado += " (Abaixo do peso)"
        elif 18.5 <= imc < 24.9:
            resultado += " (Peso normal)"
        elif 25 <= imc < 29.9:
            resultado += " (Sobrepeso)"
        else:
            resultado += " (Obesidade)"
        
        label_resultado.config(text=resultado)
    
    except ValueError:
        tk.messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("300x200")

# Altera a cor de fundo da janela principal
root.configure(bg='lightblue')  # Define a cor de fundo para 'lightblue'

# Configuração do campo de entrada de peso
label_peso = tk.Label(root, text="Peso (kg):", bg='lightblue')  # Define a cor de fundo do label
label_peso.pack(pady=5)

entrada_peso = tk.Entry(root)
entrada_peso.pack(pady=5)

# Configuração do campo de entrada de altura
label_altura = tk.Label(root, text="Altura (cm):", bg='lightblue')  # Define a cor de fundo do label
label_altura.pack(pady=5)

entrada_altura = tk.Entry(root)
entrada_altura.pack(pady=5)

# Botão para calcular o IMC
botao_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="", bg='lightblue')  # Define a cor de fundo do label
label_resultado.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()
