import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('gossip.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            role TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS gossip (
            id INTEGER PRIMARY KEY,
            title TEXT,
            text TEXT,
            image1 TEXT,
            image2 TEXT,
            image3 TEXT
        )
    ''')
    conn.commit()
    return conn

# Função para login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT role FROM users WHERE username=? AND password=?', (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        role = result[0]
        if role == 'admin':
            admin_dashboard()
        elif role == 'famous':
            famous_dashboard(username)
        else:
            client_dashboard()
    else:
        messagebox.showerror("Erro", "Credenciais inválidas!")

# Dashboard do admin
def admin_dashboard():
    clear_window()
    tk.Label(window, text="Admin Dashboard").pack()
    tk.Label(window, text="Título da fofoca:").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()
    tk.Label(window, text="Texto da fofoca:").pack()
    text_entry = tk.Text(window, height=5)
    text_entry.pack()
    
    tk.Label(window, text="Imagens (caminhos):").pack()
    image1_entry = tk.Entry(window)
    image1_entry.pack()
    image2_entry = tk.Entry(window)
    image2_entry.pack()
    image3_entry = tk.Entry(window)
    image3_entry.pack()

    def create_gossip():
        conn = connect_db()
        c = conn.cursor()
        c.execute('''
            INSERT INTO gossip (title, text, image1, image2, image3)
            VALUES (?, ?, ?, ?, ?)
        ''', (title_entry.get(), text_entry.get("1.0", tk.END), image1_entry.get(), image2_entry.get(), image3_entry.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Fofoca criada com sucesso!")

    tk.Button(window, text="Criar Fofoca", command=create_gossip).pack()

# Dashboard do famoso
def famous_dashboard(username):
    clear_window()
    tk.Label(window, text=f"Dashboard do Famoso: {username}").pack()
    tk.Label(window, text="Reportar fofoca que não gostou:").pack()
    report_entry = tk.Text(window, height=5)
    report_entry.pack()

    def report_gossip():
        messagebox.showinfo("Sucesso", "Fofoca reportada com sucesso!")

    tk.Button(window, text="Reportar", command=report_gossip).pack()

# Dashboard do cliente
def client_dashboard():
    clear_window()
    tk.Label(window, text="Dashboard do Cliente").pack()
    # Aqui você pode adicionar lógica para visualizar fofocas.

# Função para limpar a janela
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Configuração da janela principal
window = tk.Tk()
window.title("Sistema de Fofocas")
window.geometry("400x400")

tk.Label(window, text="Usuário:").pack()
username_entry = tk.Entry(window)
username_entry.pack()

tk.Label(window, text="Senha:").pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

tk.Button(window, text="Login", command=login).pack()

connect_db()
window.mainloop()
