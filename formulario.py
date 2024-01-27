import tkinter  # Importando o módulo tkinter para criação de GUI.
from tkinter import ttk  # Importando um componente específico do tkinter para widgets temáticos.
import tkinter.messagebox

def enter_data():  # Definindo uma função para lidar com a entrada de dados.
    accepted = accept_var.get()  # Obtendo o valor do status de aceitação.

    if accepted == "Accepted":  # Verificando se os termos foram aceitos.
        # Informações do usuário
        firstname = first_name_entry.get()  # Obtendo o primeiro nome digitado.
        lastname = last_name_entry.get()  # Obtendo o sobrenome digitado.

        if firstname and lastname:  # Verificando se ambos os nomes estão fornecidos.
            title = title_combobox.get()  # Obtendo o título selecionado.
            age = age_spinbox.get()  # Obtendo a idade digitada.
            nationality = nationality_combobox.get()  # Obtendo a nacionalidade selecionada.

            # Informações do curso
            registration_status = reg_status_var.get()  # Obtendo o status de registro.
            numcourses = numcourses_spinbox.get()  # Obtendo o número de cursos completados.
            numsemesters = numsemesters_spinbox.get()  # Obtendo o número de semestres.

            # Imprimindo informações do usuário e do curso.
            print("------------------------------------------")
            print("Primeiro nome: ", firstname, "Sobrenome: ", lastname)
            print("Título: ", title, "Idade: ", age, "Nacionalidade: ", nationality)
            print("# Cursos: ", numcourses, "# Semestres: ", numsemesters)
            print("Status de registro:", registration_status)
            print("------------------------------------------")
        else:
            # Exibindo um aviso se o primeiro nome e o sobrenome não forem fornecidos.
            tkinter.messagebox.showwarning(title="Erro", message="Primeiro nome e sobrenome são obrigatórios.")
    else:
        # Exibindo um aviso se os termos não forem aceitos.
        tkinter.messagebox.showwarning(title="Erro", message="Você não aceitou os termos.")

# Criando a janela principal
window = tkinter.Tk()
window.title("Formulário de Entrada de Dados")  # Definindo o título da janela.

# Criando um quadro para organizar os widgets.
frame = tkinter.Frame(window)
frame.pack()

# Criando um quadro para informações do usuário.
user_info_frame = tkinter.LabelFrame(frame, text="Informações do Usuário")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# Criando rótulos e campos de entrada para informações do usuário.
first_name_label = tkinter.Label(user_info_frame, text="Primeiro Nome")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Sobrenome")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

# Criando rótulos, comboboxes e spinboxes para informações adicionais do usuário.
title_label = tkinter.Label(user_info_frame, text="Título")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Sr.", "Sra.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Idade")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nacionalidade")
nationality_combobox = ttk.Combobox(user_info_frame, values=["África", "Antártica", "Ásia", "Europa", "América do Norte", "Oceania", "América do Sul"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

# Configurando o preenchimento para os widgets no quadro de informações do usuário.
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Criando um quadro para informações do curso.
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Criando widgets para informações do curso.
registered_label = tkinter.Label(courses_frame, text="Status de Registro")

reg_status_var = tkinter.StringVar(value="Não Registrado")
registered_check = tkinter.Checkbutton(courses_frame, text="Atualmente Registrado", variable=reg_status_var, onvalue="Registrado", offvalue="Não Registrado")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Cursos Completados")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=float('inf'))
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semestres")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=float('inf'))
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

# Configurando o preenchimento para os widgets no quadro de informações do curso.
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Criando um quadro para termos e condições.
terms_frame = tkinter.LabelFrame(frame, text="Termos e Condições")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Não Aceito")
terms_check = tkinter.Checkbutton(terms_frame, text="Aceito os termos e condições.", variable=accept_var, onvalue="Aceito", offvalue="Não Aceito")
terms_check.grid(row=0, column=0)

# Criando um botão para enviar os dados inseridos.
button = tkinter.Button(frame, text="Inserir dados", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()  # Executando o loop principal de eventos.
