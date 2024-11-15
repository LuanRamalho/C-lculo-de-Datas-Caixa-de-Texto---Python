import tkinter as tk
from tkinter import ttk
from datetime import datetime

def calcular_diferenca():
    # Obtendo as datas das entradas
    data1_str = entry_data1.get()
    data2_str = entry_data2.get()

    # Convertendo as strings para objetos de data
    try:
        data1 = datetime.strptime(data1_str, "%Y-%m-%d")
        data2 = datetime.strptime(data2_str, "%Y-%m-%d")
        
        # Calculando a diferença
        diferenca = abs(data2 - data1)
        anos = diferenca.days // 365
        meses = (diferenca.days % 365) // 30
        dias = (diferenca.days % 365) % 30

        # Atualizando o rótulo de resultado
        resultado_var.set(f"Diferença: {anos} anos, {meses} meses e {dias} dias")
    except ValueError:
        resultado_var.set("Formato de data inválido. Use YYYY-MM-DD.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Diferença entre Datas")
root.geometry("400x300")
root.configure(bg="#F0F8FF")  # Cor de fundo suave

# Criando os widgets com estilos
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), background="#F0F8FF")
style.configure("TEntry", font=("Helvetica", 12), padding=5)

# Criando os rótulos e campos de entrada
label_data1 = ttk.Label(root, text="Data 1 (YYYY-MM-DD):")
label_data1.pack(pady=10)

entry_data1 = ttk.Entry(root)
entry_data1.pack(pady=5)

label_data2 = ttk.Label(root, text="Data 2 (YYYY-MM-DD):")
label_data2.pack(pady=10)

entry_data2 = ttk.Entry(root)
entry_data2.pack(pady=5)

# Criando o botão para calcular
botao_calcular = tk.Button(root, text="Calcular Diferença", command=calcular_diferenca, font=("Helvetica", 12, "bold"), foreground="white", background="darkgreen")
botao_calcular.pack(pady=15)

# Variável para exibir o resultado
resultado_var = tk.StringVar()
label_resultado = ttk.Label(root, textvariable=resultado_var)
label_resultado.pack(pady=10)

# Iniciando o loop da interface gráfica
root.mainloop()
