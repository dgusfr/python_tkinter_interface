import tkinter
from tkinter import messagebox

def validar_login(username, password):
    # Define as credenciais válidas
    credenciais_validas = {"diego": "123456"}
    # Verifica se o usuário e senha correspondem às credenciais válidas
    if username in credenciais_validas and credenciais_validas[username] == password:
        return True
    else:
        return False

def login():
    # Obtém o nome de usuário e senha inseridos
    username = username_entry.get()
    password = password_entry.get()
    # Verifica se o login é válido
    if validar_login(username, password):
        messagebox.showinfo(title="Login Sucesso", message="Bem-Vindo!")
    else:
        messagebox.showerror(title="Erro", message="Login inválido.")

#Evento de tecla acionada
def handle_enter_key(event):
    # Atributo do evento que indica a tecla pressionada
    if event.keysym == "Return":
        login()

window = tkinter.Tk()
window.title("Formulário de Login")
window.geometry('340x440')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Nome de usuário", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Senha", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

# Adiciona um evento para a tecla Enter
window.bind("<Key>", handle_enter_key)

window.mainloop()