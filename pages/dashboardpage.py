import tkinter as tk
from tkinter import messagebox
import subprocess


def update_main_content(text):
    main_content_label.config(text=text)


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
text_color = "#E0F7FA"
button_color = "#1B1B1D"
button_text_color = "#00ACC1"

# Painel de navegação
nav_frame = tk.Frame(window, bg=bg_color, width=200)
nav_frame.pack(side=tk.LEFT, fill=tk.Y)

# Botões de navegação
nav_buttons = {
    "DASHBOARD": lambda: update_main_content("DASHBOARD - em manutenção"),
    "PACIENTES": lambda: update_main_content("PACIENTES - em manutenção"),
    "VENDAS": lambda: update_main_content("VENDAS - em manutenção"),
    "CONSULTAS": lambda: update_main_content("CONSULTAS - em manutenção"),
    "MEMBROS": lambda: update_main_content("MEMBROS - em manutenção"),
    "SAIR": logout
}

# Criando botões de navegação
for text, command in nav_buttons.items():
    button = tk.Button(nav_frame, text=text, font=("Arial", 12, "bold"),
                       bg=bg_color, fg=text_color, command=command,
                       relief="flat", activebackground=bg_color,
                       activeforeground=button_text_color)
    button.pack(fill=tk.X, padx=10, pady=5)

# Área principal
main_frame = tk.Frame(window, bg=emphasis)
main_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

main_content_label = tk.Label(main_frame, text="Escolha uma opção", font=(
    "Arial", 18, "bold"), bg=emphasis, fg="black")
main_content_label.pack(expand=True)

if __name__ == '__main__':
    window.mainloop()
