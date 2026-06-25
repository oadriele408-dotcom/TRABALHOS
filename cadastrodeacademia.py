import tkinter as tk
from tkinter import ttk, messagebox

# --- Funções de Validação ---

def validar_nome(texto):
    # Permite apenas letras e espaços
    if texto == "":
        return True
    return all(c.isalpha() or c.isspace() for c in texto)

def validar_idade(texto):
    # Permite apenas números E limita o comprimento máximo a 2 caracteres
    if texto == "":
        return True
    return texto.isdigit() and len(texto) <= 2

def validar_cpf(texto):
    # Permite apenas números (você pode digitar até os 11 dígitos do CPF)
    if texto == "":
        return True
    return texto.isdigit()


# --- Função de Cadastro ---

def cadastrar_aluno():
    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()
    cpf = entry_cpf.get().strip()
    plano = cb_plano.get()

    # Validação para garantir que os campos não estão vazios
    if not nome or not idade or not cpf or not plano:
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
        return
    
    # Inserindo os dados na tabela para visualização
    tree.insert("", tk.END, values=(nome, idade, cpf, plano))
    
    # Limpando os campos após o cadastro
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    cb_plano.set('')
    
    messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")


# --- Configuração da Janela Principal ---
root = tk.Tk()
root.title("Sistema de Academia - Cadastro")
root.geometry("550x460")
root.configure(padx=20, pady=20)

# Registrando as funções de validação no Tkinter
valida_nome_cmd = root.register(validar_nome)
valida_idade_cmd = root.register(validar_idade)
valida_cpf_cmd = root.register(validar_cpf)


# --- Seção de Formulário ---

# Nome (Apenas Letras)
tk.Label(root, text="Nome Completo:").grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(root, width=40, validate="key", validatecommand=(valida_nome_cmd, "%P"))
entry_nome.grid(row=0, column=1, pady=5)

# Idade (Apenas Números - Máximo 2 dígitos)
tk.Label(root, text="Idade:").grid(row=1, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(root, width=40, validate="key", validatecommand=(valida_idade_cmd, "%P"))
entry_idade.grid(row=1, column=1, pady=5)

# CPF (Apenas Números)
tk.Label(root, text="CPF (Apenas números):").grid(row=2, column=0, sticky="w", pady=5)
entry_cpf = tk.Entry(root, width=40, validate="key", validatecommand=(valida_cpf_cmd, "%P"))
entry_cpf.grid(row=2, column=1, pady=5)

# Plano (Pré-definidos)
tk.Label(root, text="Plano:").grid(row=3, column=0, sticky="w", pady=5)
planos_disponiveis = ["Mensal", "Trimestral", "Semestral", "Anual"]
cb_plano = ttk.Combobox(root, values=planos_disponiveis, width=37, state="readonly")
cb_plano.grid(row=3, column=1, pady=5)


# --- Botão de Ação ---
btn_cadastrar = tk.Button(root, text="Cadastrar Aluno", command=cadastrar_aluno, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=15, ipadx=20)


# --- Seção de Tabela ---
colunas = ("Nome", "Idade", "CPF", "Plano")
tree = ttk.Treeview(root, columns=colunas, show="headings", height=8)

tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("CPF", text="CPF")
tree.heading("Plano", text="Plano")

tree.column("Nome", width=180)
tree.column("Idade", width=50, anchor="center")
tree.column("CPF", width=120, anchor="center")
tree.column("Plano", width=100, anchor="center")

tree.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()