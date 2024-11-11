import tkinter as tk
from tkinter import messagebox
import subprocess


def logout():
    messagebox.showinfo("Logout", "Você foi deslogado!")
    window.destroy()
    subprocess.run(["python", "pages/loginpage.py"])


# Janela principal
window = tk.Tk()
window.title("Hospital Management")
window.geometry("800x400")
window.configure(bg="#1B1B1D")

# Cores
emphasis = "#00ACC1"
bg_color = "#1B1B1D"
darker_bg_color = "#121212"
text_color = "#E0F7FA"
button_color = "#1B1B1D"
button_text_color = "#00ACC1"

# Painel de navegação
nav_frame = tk.Frame(window, bg=bg_color, width=200)
nav_frame.pack(side=tk.LEFT, fill=tk.Y, anchor="n", padx=10, pady=10)

# Views


def load_dashboard():
    for widget in main_frame.winfo_children():
        widget.destroy()

    dashboard_label = tk.Label(main_frame, text="Isso é o Dashboard", font=(
        "Arial", 18, "bold"), bg=bg_color, fg=text_color)
    dashboard_label.pack(expand=True)


def load_pacientes():
    for widget in main_frame.winfo_children():
        widget.destroy()

    pacientes_label = tk.Label(main_frame, text="Isso é o Pacientes", font=(
        "Arial", 18, "bold"), bg=bg_color, fg=text_color)
    pacientes_label.pack(expand=True)


def load_vendas():
    for widget in main_frame.winfo_children():
        widget.destroy()

    vendas_label = tk.Label(main_frame, text="Isso é o Vendas", font=(
        "Arial", 18, "bold"), bg=bg_color, fg=text_color)
    vendas_label.pack(expand=True)


def load_consultas():
    for widget in main_frame.winfo_children():
        widget.destroy()

    consultas_label = tk.Label(main_frame, text="Isso é o Consultas", font=(
        "Arial", 18, "bold"), bg=bg_color, fg=text_color)
    consultas_label.pack(expand=True)


def load_membros():
    for widget in main_frame.winfo_children():
        widget.destroy()

    membros_label = tk.Label(main_frame, text="Isso é o Membros", font=(
        "Arial", 18, "bold"), bg=bg_color, fg=text_color)
    membros_label.pack(expand=True)


# Botões de navegação
nav_buttons = {
    "DASHBOARD": load_dashboard,
    "PACIENTES": load_pacientes,
    "VENDAS": load_vendas,
    "CONSULTAS": load_consultas,
    "MEMBROS": load_membros,
    "SAIR": logout
}

# Criando os botões de navegação e centralizando
for text, command in nav_buttons.items():
    button = tk.Button(nav_frame, text=text, font=("Arial", 15, "bold"),
                       bg=darker_bg_color, fg=text_color, command=command,
                       relief="flat", activebackground=darker_bg_color,
                       activeforeground=button_text_color, cursor='hand2')
    button.pack(fill=tk.X, padx=10, pady=5, expand=True)

# Área principal
main_frame = tk.Frame(window, bg=bg_color)
main_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Inicializando com o conteúdo do Dashboard
main_content_label = tk.Label(
    main_frame, text="Escolha uma opção",
    font=("Arial", 18, "bold"), bg=bg_color, fg=text_color)
main_content_label.pack(expand=True)

if __name__ == '__main__':
    window.mainloop()
