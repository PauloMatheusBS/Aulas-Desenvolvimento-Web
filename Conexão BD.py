# CREATE DATABASE sistema_login;

# USE sistema_login;

# CREATE TABLE usuarios (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     usuario VARCHAR(50) UNIQUE NOT NULL,
#     senha VARCHAR(255) NOT NULL,
#     tipo_acesso ENUM('Tipo1', 'Tipo2', 'Tipo3', 'Tipo4', 'Tipo5') NOT NULL,
#     texto TEXT
# );


#pip install mysql-connector-python


# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
# from mysql.connector import Error

# # Função para conectar ao banco de dados
# def conectar_banco():
#     try:
#         conexao = mysql.connector.connect(
#             host='localhost',
#             user='seu_usuario',
#             password='sua_senha',
#             database='sistema_login'
#         )
#         return conexao
#     except Error as e:
#         print(f"Erro: {e}")
#         return None

# # Função para exibir a tela baseada no tipo de acesso
# def mostrar_tela(tipo_acesso):
#     if tipo_acesso == 'Tipo1':
#         messagebox.showinfo("Tela Tipo1", "Bem-vindo à tela Tipo1!")
#     elif tipo_acesso == 'Tipo2':
#         messagebox.showinfo("Tela Tipo2", "Bem-vindo à tela Tipo2!")
#     elif tipo_acesso == 'Tipo3':
#         messagebox.showinfo("Tela Tipo3", "Bem-vindo à tela Tipo3!")
#     elif tipo_acesso == 'Tipo4':
#         messagebox.showinfo("Tela Tipo4", "Bem-vindo à tela Tipo4!")
#     elif tipo_acesso == 'Tipo5':
#         messagebox.showinfo("Tela Tipo5", "Bem-vindo à tela Tipo5!")
#     else:
#         messagebox.showwarning("Acesso Não Encontrado", "Tipo de acesso não encontrado.")

# # Função para verificar o login
# def verificar_login():
#     usuario = entry_usuario.get()
#     senha = entry_senha.get()

#     conexao = conectar_banco()
#     if conexao:
#         cursor = conexao.cursor()
#         query = "SELECT senha, tipo_acesso FROM usuarios WHERE usuario = %s"
#         cursor.execute(query, (usuario,))
#         resultado = cursor.fetchone()

#         if resultado:
#             senha_armazenada, tipo_acesso = resultado
#             if senha_armazenada == senha:
#                 mostrar_tela(tipo_acesso)
#             else:
#                 messagebox.showerror("Erro", "Senha incorreta!")
#         else:
#             if messagebox.askyesno("Cadastro", "Usuário não encontrado. Deseja criar um cadastro?"):
#                 cadastrar_usuario(usuario, senha)
        
#         cursor.close()
#         conexao.close()

# # Função para cadastrar um novo usuário
# def cadastrar_usuario(usuario, senha):
#     def salvar_cadastro():
#         tipo_acesso = tipo_acesso_var.get()
#         texto = entry_texto.get()

#         conexao = conectar_banco()
#         if conexao:
#             cursor = conexao.cursor()
#             query = "INSERT INTO usuarios (usuario, senha, tipo_acesso, texto) VALUES (%s, %s, %s, %s)"
#             try:
#                 cursor.execute(query, (usuario, senha, tipo_acesso, texto))
#                 conexao.commit()
#                 messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
#                 janela_cadastro.destroy()
#             except Error as e:
#                 messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
#             finally:
#                 cursor.close()
#                 conexao.close()
    
#     janela_cadastro = tk.Toplevel(janela)
#     janela_cadastro.title("Cadastro")

#     tk.Label(janela_cadastro, text="Tipo de Acesso").pack()
#     tipo_acesso_var = tk.StringVar(value='Tipo1')
#     for tipo in ['Tipo1', 'Tipo2', 'Tipo3', 'Tipo4', 'Tipo5']:
#         tk.Radiobutton(janela_cadastro, text=tipo, variable=tipo_acesso_var, value=tipo).pack()

#     tk.Label(janela_cadastro, text="Texto").pack()
#     entry_texto = tk.Entry(janela_cadastro)
#     entry_texto.pack()

#     tk.Button(janela_cadastro, text="Salvar", command=salvar_cadastro).pack()

# # Configuração da interface gráfica
# janela = tk.Tk()
# janela.title("Login")

# tk.Label(janela, text="Usuário").pack()
# entry_usuario = tk.Entry(janela)
# entry_usuario.pack()

# tk.Label(janela, text="Senha").pack()
# entry_senha = tk.Entry(janela, show="*")
# entry_senha.pack()

# tk.Button(janela, text="Entrar", command=verificar_login).pack()

# janela.mainloop()
