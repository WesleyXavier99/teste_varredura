import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()
# import os
# import tkinter as tk
# from tkinter import filedialog
# import xlwt
#
# def selecao_diretorio():
#     diretorio = filedialog.askdirectory()
#     if diretorio:
#         subpastas = [f.name for f in os.scandir(diretorio) if f.is_dir()]
#         salvar_local = filedialog.asksaveasfilename(defaultextension=".xls", filetypes=[("Excel files", "*.xls")])
#         preenche_xls(subpastas, salvar_local, diretorio)
#
# def preenche_xls(subpastas, salvar_local, pasta_pai, level=1):
#     print("RODOU")
#     wb = xlwt.Workbook()
#
#     #criando umna aba
#     folha = wb.add_sheet('Sheet1')
#
#     #percorrendo todas subpastas
#     for i, pasta in enumerate(subpastas):
#         folha.write(0, i, pasta)
#         # juntando diretorio principal com o nome da pasta do job(...\pentaho\Intermodal\job\transformações)
#         caminho = os.path.join(pasta_pai, pasta)
#         sub = ".git"
#         sub2 = "README.md"
#         test = caminho
#
#         if sub in test or sub2 in test:
#             print("caminho invalido",end="\n")
#         else:
#             print("caminho completo: " + caminho, end="\n")
#             #print("pasta: " + pasta, end="\n")
#             # checando o conteudo de dentro dessa pasta
#             if os.path.isdir(caminho):
#                 conteudo = os.listdir(caminho)
#                 print("Conteudo: ", end="")
#                 print(conteudo)
#                 # acessando o conteudo
#                 for j, item in enumerate(conteudo):
#                     caminho_item = os.path.join(caminho, item)
#                     print("subpasta: ",end="")
#                     print(item)
#                     if os.path.isdir(caminho_item):
#                         #folha.write(j + 1, i, item)
#                         conteudoSubPastas = os.listdir(caminho_item)
#                         print("Conteudo subpasta: ", end="")
#                         print(conteudoSubPastas)
#                         for ct in conteudoSubPastas:
#                             folha.write(j + 1, i, ct)
#                         preenche_xls(conteudoSubPastas, salvar_local, caminho_item, level + 1)
#                     elif os.path.isfile(caminho_item):
#                         print("else")
#                         #folha.write(j + 1, i, item)
#             wb.save(salvar_local)
#
# def interface():
#     root = tk.Tk()
#     root.title("Seleção de pasta")
#     root.geometry("400x200")
#     select_folder_button = tk.Button(root, text="Selecione a pasta", command=selecao_diretorio, width=20, height=2)
#     select_folder_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#     root.mainloop()
#
# interface()
