import tkinter as tk
from tkinter import ttk, messagebox


produtos = []

def cadastrar_produto():
    nome = entry_nome.get()
    categoria = entry_categoria.get()
    preco = entry_preco.get()
    quantidade = entry_quantidade.get()

    if not nome or not categoria or not preco or not quantidade:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except ValueError:
        messagebox.showerror("Erro", "Preço deve ser numérico e quantidade deve ser inteira.")
        return

    produtos.append([nome, categoria, preco, quantidade])

    tree.insert("", tk.END, values=(nome, categoria, f"R$ {preco:.2f}", quantidade))

    limpar_campos()

    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)


janela = tk.Tk()
janela.title("Cadastro de Supermercado")
janela.geometry("700x450")
janela.resizable(False, False)


frame = tk.LabelFrame(janela, text="Cadastro de Produto", padx=10, pady=10)
frame.pack(fill="x", padx=10, pady=10)


tk.Label(frame, text="Nome do Produto:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(frame, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)


tk.Label(frame, text="Categoria:").grid(row=1, column=0, sticky="w")
entry_categoria = tk.Entry(frame, width=30)
entry_categoria.grid(row=1, column=1, padx=5, pady=5)


tk.Label(frame, text="Preço:").grid(row=2, column=0, sticky="w")
entry_preco = tk.Entry(frame, width=30)
entry_preco.grid(row=2, column=1, padx=5, pady=5)


tk.Label(frame, text="Quantidade:").grid(row=3, column=0, sticky="w")
entry_quantidade = tk.Entry(frame, width=30)
entry_quantidade.grid(row=3, column=1, padx=5, pady=5)


btn_cadastrar = tk.Button(
    frame,
    text="Cadastrar Produto",
    command=cadastrar_produto,
    bg="green",
    fg="white"
)
btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)


colunas = ("Nome", "Categoria", "Preço", "Quantidade")

tree = ttk.Treeview(janela, columns=colunas, show="headings")

for coluna in colunas:
    tree.heading(coluna, text=coluna)
    tree.column(coluna, width=150)

tree.pack(fill="both", expand=True, padx=10, pady=10)

janela.mainloop()