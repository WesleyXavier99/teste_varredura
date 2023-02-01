from tkinter import *
from tkinter import ttk
from datetime import date
from tkinter import filedialog


def buscaOrigem():
    filename = filedialog.askdirectory(initialdir="/", title="Select file")
    inp_origem.insert(INSERT,filename)

def buscaDestino():
    filename = filedialog.askdirectory(initialdir="/", title="Select file")
    inp_salvar.insert(INSERT, filename)

def fechaTela():
    tela.destroy()

def geraArquivo():
    #verificações
    if inp_origem.get('1.0', 'end').__len__()<=1 :
        erro = Label(tela,text="Preencha o campo origem!",foreground="red",width=24, height=1,background="white")
        erro.pack()
        erro.place(anchor='center', relx=0.4, rely=0.43)

    if inp_salvar.get('1.0', 'end').__len__()<=1 :
        erro = Label(tela, text="Preencha o campo Salvar em!", foreground="red", width=27, height=1, background="white")
        erro.pack()
        erro.place(anchor='center', relx=0.4, rely=0.53)

    if inp_nome_arq.get('1.0', 'end').__len__()<=1 :
        erro = Label(tela, text="Preencha o campo Salvar como!", foreground="red", width=29, height=1, background="white")
        erro.pack()
        erro.place(anchor='center', relx=0.45, rely=0.68)


#CONFIGURAÇÕES DA TELA
tela = Tk()
tela.geometry("1000x600")
tela.configure(bg='white')

#LOGO
img = PhotoImage(file="src/Img/OWSE.png")
label_logo = Label(tela, image=img,border=0)
label_logo.pack()
label_logo.place(anchor='center', relx=0.5, rely=0.2)

#BOTÕES

#origem
botao_origem = Button(tela,text='Origem',width=7,height=1,command=buscaOrigem)
botao_origem.pack()
botao_origem.place(anchor='e', relx=0.8, rely=0.4)

#salvar como
botao_salvar = Button(tela,text='Salvar em',width=7,height=1,command=buscaDestino)
botao_salvar.pack()
botao_salvar.place(anchor='e', relx=0.8, rely=0.5)

#gerar
botao_gerar = Button(tela,text='Gerar',width=7,height=1,command=geraArquivo)
botao_gerar.pack()
botao_gerar.place(anchor='center', relx=0.4, rely=0.75)

#cancelar
botao_cancelar = Button(tela,text='Cancelar',width=7,height=1, command=fechaTela)
botao_cancelar.pack()
botao_cancelar.place(anchor='center', relx=0.5, rely=0.75)

#INPUTS

#origem
inp_origem = Text(tela,height=1,width=70)
inp_origem.pack()
inp_origem.place(anchor='center', relx=0.4, rely=0.4)
inp_origem.insert(INSERT, "")

#salvar em
inp_salvar = Text(tela,height=1,width=70)
inp_salvar.pack()
inp_salvar.place(anchor='center', relx=0.4, rely=0.5)

#nome arquivo
lbl_salvar = Label(tela,text='Salvar como',background="white")
lbl_salvar.pack()
lbl_salvar.place(anchor='center', relx=0.45, rely=0.6)
#data atual para preencher o label de nome do arquivo gerado
data_atual = date.today()
data_atual = data_atual.strftime("%d/%m/%Y")
inp_nome_arq = Text(tela,height=1, width=35)
inp_nome_arq.insert(INSERT,'Relatorio de Fluxos - '+data_atual)
inp_nome_arq.pack()
inp_nome_arq.place(anchor='center',relx=0.45,rely=0.65)

#checkbox hop/pentaho
check = StringVar()
box = ttk.Combobox(tela, textvariable=check)
box['values'] = ('hop', 'pentaho')
box.pack()
box.place(anchor='center', relx=7, rely=5)
check = check.get()
box = box.get()


tela.mainloop()

