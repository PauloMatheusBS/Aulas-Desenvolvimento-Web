import tkinter as tk
from tkinter import messagebox
import math

class Calculadora:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora")
        self.raiz.geometry("400x600")
        
        self.e_cientifica = False
        self.e_ligada = True
        self.entrada_atual = ""
        self.criar_widgets()

    def criar_widgets(self):
        
        self.exibicao = tk.Entry(self.raiz, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, bg="#FADCD9", fg="#D36C6C")
        self.exibicao.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        
        self.frame_basico = tk.Frame(self.raiz, bg="#FADCD9")
        self.frame_basico.grid(row=1, column=0, columnspan=4, padx=10, pady=5)
        
        self.frame_cientifico = tk.Frame(self.raiz, bg="#FADCD9")
        self.frame_cientifico.grid(row=1, column=0, columnspan=4, padx=10, pady=5)
        self.frame_cientifico.grid_forget() 
        
        
        self.criar_botoes_basicos()
        self.criar_botoes_cientificos()
        
        
        self.botao_ligar_desligar = tk.Button(self.raiz, text="Off", command=self.alternar_calculadora, width=12, bg="#D36C6C", fg="white")
        self.botao_ligar_desligar.grid(row=2, column=3, padx=5, pady=5)
        
        self.botao_cientifico = tk.Button(self.raiz, text="Científico", command=self.alternar_modo_cientifico, width=12, bg="#D36C6C", fg="white")
        self.botao_cientifico.grid(row=2, column=2, padx=5, pady=5)

    def criar_botoes_basicos(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3),
            ('=', 5, 0, 1, 4)  
        ]

        for botao_info in botoes:
            texto = botao_info[0]
            linha = botao_info[1]
            coluna = botao_info[2]
            rowspan = botao_info[3] if len(botao_info) > 3 else 1
            colspan = botao_info[4] if len(botao_info) > 4 else 1
            acao = self.limpar if texto == 'C' else self.calcular if texto == '=' else lambda x=texto: self.adicionar_a_expressao(x)
            botao = tk.Button(self.frame_basico, text=texto, command=acao, width=5, height=2, bg="#FADCD9", fg="#D36C6C")
            botao.grid(row=linha, column=coluna, rowspan=rowspan, columnspan=colspan, padx=5, pady=5, sticky="nsew")

        
        for i in range(4):
            self.frame_basico.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.frame_basico.grid_rowconfigure(i, weight=1)

    def criar_botoes_cientificos(self):
        botoes = {
            'sqrt': (0, 0), 'pow': (0, 1), 'log': (0, 2), 'tan': (0, 3),
            'cos': (1, 0), 'sin': (1, 1), 'exp': (1, 2), '(': (1, 3), ')': (1, 4)
        }

        for texto, (linha, coluna) in botoes.items():
            botao = tk.Button(self.frame_cientifico, text=texto, command=lambda x=texto: self.adicionar_a_expressao(x), width=5, height=2, bg="#FADCD9", fg="#D36C6C")
            botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

        
        for i in range(5):
            self.frame_cientifico.grid_columnconfigure(i, weight=1)
        for i in range(2):
            self.frame_cientifico.grid_rowconfigure(i, weight=1)

    def alternar_calculadora(self):
        self.e_ligada = not self.e_ligada
        if self.e_ligada:
            self.raiz.title("Calculadora")
            self.exibicao.config(state='normal')
            self.botao_ligar_desligar.config(text="Off")
        else:
            self.raiz.title("Calculadora (Desligada)")
            self.exibicao.config(state='disabled')
            self.botao_ligar_desligar.config(text="On")
            self.exibicao.delete(0, tk.END)

    def alternar_modo_cientifico(self):
        self.e_cientifica = not self.e_cientifica
        if self.e_cientifica:
            self.frame_cientifico.grid()
            self.botao_cientifico.config(text="Básico")
        else:
            self.frame_cientifico.grid_forget()
            self.botao_cientifico.config(text="Científico")

    def adicionar_a_expressao(self, caractere):
        if self.e_ligada:
            self.entrada_atual += str(caractere)
            self.exibicao.delete(0, tk.END)
            self.exibicao.insert(tk.END, self.entrada_atual)

    def limpar(self):
        if self.e_ligada:
            self.entrada_atual = ""
            self.exibicao.delete(0, tk.END)

    def calcular(self):
        if self.e_ligada:
            try:
                resultado = eval(self.entrada_atual, {"__builtins__": None}, {"sqrt": math.sqrt, "pow": math.pow, "log": math.log, "tan": math.tan, "cos": math.cos, "sin": math.sin, "exp": math.exp})
                self.exibicao.delete(0, tk.END)
                self.exibicao.insert(tk.END, str(resultado))
                self.entrada_atual = str(resultado)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao calcular: {e}")
                self.limpar()

    def tecla_press(self, evento):
        if self.e_ligada:
            if evento.char.isdigit() or evento.char in "+-*/.()":
                self.adicionar_a_expressao(evento.char)
            elif evento.keysym == 'Return':
                self.calcular()
            elif evento.keysym == 'BackSpace':
                self.entrada_atual = self.entrada_atual[:-1]
                self.exibicao.delete(0, tk.END)
                self.exibicao.insert(tk.END, self.entrada_atual)

def main():
    raiz = tk.Tk()
    calculadora = Calculadora(raiz)
    raiz.bind("<Key>", calculadora.tecla_press)
    raiz.mainloop()


main()
