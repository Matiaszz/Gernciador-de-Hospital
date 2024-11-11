

import tkinter as tk

import sys
import os
try:
    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))
    from auth.login import teste, teste_login
except Exception as e:
    print(e)


# Função para placeholder
def create_rounded_entry(parent, placeholder):
    entry_frame = tk.Frame(parent, bg="white", bd=0)
    entry_frame.pack(pady=(5, 10))

    entry = tk.Entry(entry_frame, font=("Arial", 14),
                     bd=0, justify="center", width=30)
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: on_focus_in(
        event, placeholder))

    entry.bind("<FocusOut>", lambda event: on_focus_out(event, placeholder))

    entry.grid(row=0, column=0, padx=10, pady=5, ipadx=5, ipady=5)

    entry_frame.configure(width=300, height=50)
    entry_frame.pack_propagate(False)

    return entry


def on_focus_in(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(fg="black")


def on_focus_out(event, placeholder):
    if not event.widget.get():
        event.widget.insert(0, placeholder)
        event.widget.config(fg="gray")


login_page = tk.Tk()
login_page.title("Login e Cadastro")
login_page.geometry("800x400")
login_page.configure(bg="#1B1B1D")

# Cores
emphasis = "#00ACC1"
bg_color = "#1B1B1D"
text_color = "#E0F7FA"
button_color = "#1B1B1D"
button_text_color = "#00ACC1"

left_frame = tk.Frame(login_page, bg=emphasis, width=400, height=400)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frame direito - Entrar
right_frame = tk.Frame(login_page, bg=bg_color, width=400, height=400)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Configuração para o texto grande
cadastrar_label = tk.Label(
    left_frame, text="CADASTRAR", font=("Arial", 28, "bold"), bg=emphasis,
    fg="black"
)
cadastrar_label.pack(pady=(20, 10))

entrar_label = tk.Label(
    right_frame, text="ENTRAR", font=("Arial", 28, "bold"), bg=bg_color,
    fg="white"
)
entrar_label.pack(pady=(20, 10))


left_inner_frame = tk.Frame(left_frame, bg=emphasis)
left_inner_frame.pack(expand=True)

# Campos de entrada para Cadastrar
nome_entry = create_rounded_entry(left_inner_frame, "Nome completo")
email_entry = create_rounded_entry(left_inner_frame, "Email")
senha_entry = create_rounded_entry(left_inner_frame, "Senha")

# Botão de Cadastrar
cadastrar_button = tk.Button(
    left_inner_frame, text="CADASTRAR", font=("Arial", 14, "bold"),
    bg=button_color, fg=button_text_color, relief="flat",
    activebackground=button_color, activeforeground=button_text_color,
)
cadastrar_button.pack(pady=20)

# Frame interno para centralizar os widgets de login
right_inner_frame = tk.Frame(right_frame, bg=bg_color)
right_inner_frame.pack(expand=True)

# Campos de entrada para Entrar
email_login_entry = create_rounded_entry(right_inner_frame, "Email")
senha_login_entry = create_rounded_entry(right_inner_frame, "Senha")

# Botão de Entrar
entrar_button = tk.Button(
    right_inner_frame, text="ENTRAR", font=("Arial", 14, "bold"), bg="white",
    fg=bg_color, relief="flat", activebackground="white",
    activeforeground=bg_color
)
entrar_button.pack(pady=20)


def executar_cadastro():
    nome = nome_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()
    if (nome.lower() != 'nome' and email.lower() != 'email'
            and senha.lower() != 'senha'):

        if teste(nome, email, senha):
            print("Cadastro realizado com sucesso!")
            return
    print("Falha no cadastro.")
    return


def executar_login():
    email = email_login_entry.get()
    senha = senha_login_entry.get()
    if (email.lower() != 'email' and senha.lower() != 'senha'):

        if teste_login(email, senha):
            print("Login realizado com sucesso!")
            return
    print("Falha no Login.")
    return


cadastrar_button.config(command=executar_cadastro)
entrar_button.config(command=executar_login)

if __name__ == '__main__':

    login_page.mainloop()
