from tkinter import *
from tkinter import messagebox
import customtkinter as ct
from Controller import Controller


class view:

    def __init__(self):
        self.c = Controller()
        self.nome = ""
        ct.set_appearance_mode("System")
        ct.set_default_color_theme("dark-blue")
        self.janela = ct.CTk()
        self.janela.geometry("750x500")
        self.janela.resizable(False, False)
        self.seeObras()
        self.janela.mainloop()

    def createLabel(self, frame, tamanho):
        for i in range(tamanho):
            obra_data = self.c.puxarObra(i + 1)
            label_text = f"{obra_data[i]}"
            print(obra_data)

            label = ct.CTkLabel(frame, text=label_text, font=(
                "JetBrains Mono", 20), fg_color='#31304D', width=430, height=50, anchor='w')
            label.grid(row=i, column=0, padx=5, pady=2, sticky='w')

    def loginScreen(self):
        self.janela.title('Login')

        self.frameL = ct.CTkFrame(master=self.janela)
        self.frameL.pack(fill="both", expand=True, )

        labelUser = ct.CTkLabel(
            self.frameL, text="Usuario", font=("arial bold", 20))
        labelPass = ct.CTkLabel(
            self.frameL, text="Senha", font=("arial bold", 20))
        self.entryUserL = ct.CTkEntry(self.frameL, 230)
        self.entryPassL = ct.CTkEntry(self.frameL, 230, show="*")
        buttonLogin = ct.CTkButton(
            self.frameL, text="Entrar", command=lambda: self.login())
        buttonRegister = ct.CTkButton(self.frameL, text="Registrar", command=lambda: [
                                      self.frameL.destroy(), self.registerScreen()])

        labelUser.place(x=200, y=90)
        labelPass.place(x=200, y=160)
        self.entryUserL.place(x=300, y=90)
        self.entryPassL.place(x=300, y=160)
        buttonRegister.place(x=200, y=300)
        buttonLogin.place(x=400, y=300)

    def registerScreen(self):
        self.janela.title('Registro')

        self.frameR = ct.CTkFrame(master=self.janela)
        self.frameR.pack(fill="both", expand=True)

        labelUser = ct.CTkLabel(
            self.frameR, text="Usuario", font=("arial bold", 20))
        labelPass = ct.CTkLabel(
            self.frameR, text="Senha", font=("arial bold", 20))
        confirmlabelPass = ct.CTkLabel(
            self.frameR, text="Senha", font=("arial bold", 20))
        self.entryUserR = ct.CTkEntry(self.frameR, 230)
        self.entryPassR = ct.CTkEntry(self.frameR, 230, show="*")
        self.confirmentryPassR = ct.CTkEntry(self.frameR, 230, show="*")
        buttonLogin = ct.CTkButton(self.frameR, text="Entrar", command=lambda: [
                                   self.frameR.destroy(), self.loginScreen()])
        buttonRegister = ct.CTkButton(
            self.frameR, text="Registrar", command=lambda: self.registro())

        labelUser.place(x=200, y=90)
        labelPass.place(x=200, y=160)
        confirmlabelPass.place(x=200, y=230)
        self.entryUserR.place(x=300, y=90)
        self.entryPassR.place(x=300, y=160)
        self.confirmentryPassR.place(x=300, y=230)
        buttonRegister.place(x=200, y=300)
        buttonLogin.place(x=400, y=300)

    def registro(self):
        if self.entryPassR.get() == self.confirmentryPassR.get() and self.c.receberRegistro(self.entryUserR.get(), self.entryPassR.get()):
            self.nome = self.entryUserR.get()
            self.frameR.destroy()
            self.mainScreen()
        else:
            messagebox.showwarning(
                title="Atenção", message="Senhas diferentes ou usuario já existente!!")

    def login(self):
        if self.c.receberLogin(self.entryUserL.get(), self.entryPassL.get()):
            self.nome = self.entryUserL.get()
            self.frameL.destroy()
            self.mainScreen()
        else:
            messagebox.showwarning(
                title="Atenção", message="Senha incorreta ou usuario não existente!!")

    def mainScreen(self):
        self.janela.title('Principal')

        self.frameM = ct.CTkFrame(master=self.janela)
        self.frameM.pack(fill="both", expand=True)

        labelName = ct.CTkLabel(
            self.frameM, text=self.nome, font=("arial bold", 23))
        labelTitle = ct.CTkLabel(
            self.frameM, text="O que deseja fazer?", font=("arial bold", 25))
        buttonAdd = ct.CTkButton(self.frameM, text="Adicionar obra", width=280, height=38, font=(
            "arial bold", 15), command=lambda: [self.frameM.destroy(), self.AddObra()])
        buttonView = ct.CTkButton(
            self.frameM, text="Ver obras", width=280, height=38, font=("arial bold", 15))
        buttonExit = ct.CTkButton(self.frameM, text="Sair", width=280, height=38, font=(
            "arial bold", 15), command=lambda: [self.frameM.destroy(), self.loginScreen()])

        labelName.place(x=20, y=10)
        labelTitle.place(x=250, y=90)
        buttonAdd.place(x=220, y=180)
        buttonView.place(x=220, y=270)
        buttonExit.place(x=220, y=360)

    def addObra(self):
        self.janela.title('Adicionar')

        self.frameA = ct.CTkFrame(master=self.janela)
        self.frameA.pack(fill="both", expand=True)

        def slider_event(value):
            text_var.set(f"NOTA: {int(self.sliderRating.get())}")

        text_var = ct.StringVar(value="NOTA: 0")

        self.labelUName = ct.CTkLabel(
            self.frameA, text=self.nome, font=("arial bold", 23))
        labelName = ct.CTkLabel(
            self.frameA, text="NOME DA OBRA:", font=("arial bold", 18))
        self.entryName = ct.CTkEntry(self.frameA, 180)
        labelGenres = ct.CTkLabel(
            self.frameA, text="GENERO:", font=("arial bold", 18))
        self.comboboxGenres = ct.CTkComboBox(self.frameA, values=[
                                             "TERROR", "COMEDIA", "ROMANCE", "SUSPENSE", "DRAMA", "AÇÃO", "MUSICAL", "AVENTURA", "DOCUMENTARIO", "FICÇÃO", "ANIMAÇÃO"], width=180)
        labelRating = ct.CTkLabel(
            self.frameA, textvariable=text_var, font=("arial bold", 20))
        labelComment = ct.CTkLabel(
            self.frameA, text="COMENTARIO:", font=("arial bold", 19))
        self.entryComment = ct.CTkEntry(self.frameA, 180)
        self.sliderRating = ct.CTkSlider(
            self.frameA, from_=0, to=5, command=slider_event, number_of_steps=5, width=175)
        labelStatus = ct.CTkLabel(
            self.frameA, text="STATUS:", font=("arial bold", 18))
        self.comboboxStatus = ct.CTkComboBox(
            self.frameA, values=["ANDAMENTO", "COMPLETO", "A VER"], width=180)
        labelType = ct.CTkLabel(
            self.frameA, text="TIPO:", font=("arial bold", 18))
        self.comboboxType = ct.CTkComboBox(
            self.frameA, values=["FILME", "SERIE", "LIVRO"], width=180)
        buttonAdd = ct.CTkButton(self.frameA, text="Adicionar", width=180, height=30, font=(
            "arial bold", 15), command=lambda: [self.adicionarObra()])
        buttonView = ct.CTkButton(
            self.frameA, text="Ver obras", width=180, height=30, font=("arial bold", 15))
        buttonExit = ct.CTkButton(self.frameA, text="Sair", width=180, height=30, font=(
            "arial bold", 15), command=lambda: [self.frameA.destroy(), self.mainScreen()])

        self.labelUName.place(x=20, y=10)
        labelName.place(x=180, y=50)
        self.entryName.place(x=330, y=50)
        labelComment.place(x=188, y=90)
        self.entryComment.place(x=330, y=90)
        labelGenres.place(x=240, y=130)
        self.comboboxGenres.place(x=330, y=130)
        labelRating.place(x=260, y=170)
        self.sliderRating.place(x=340, y=175)
        labelStatus.place(x=245, y=210)
        self.comboboxStatus.place(x=330, y=210)
        labelType.place(x=275, y=250)
        self.comboboxType.place(x=330, y=250)
        buttonAdd.place(x=100, y=340)
        buttonView.place(x=300, y=340)
        buttonExit.place(x=500, y=340)

        self.sliderRating.set(0)

    def adicionarObra(self):
        if self.c.receberObra(self.nome, self.entryName.get(), self.entryComment.get(), self.comboboxGenres.get(), self.sliderRating.get(), self.comboboxStatus.get(), self.comboboxType.get()):
            messagebox.showinfo(
                "Adicionado", "Sua obra foi adicionada com sucesso")
            self.entryName.delete(0, END), self.entryComment.delete(0, END), self.comboboxGenres.set(
                "TERROR"), self.sliderRating.set(0), self.comboboxStatus.set("ANDAMENTO"), self.comboboxType.set("FILME")

        else:
            messagebox.showinfo(
                "Não adicionado", "Sua obra já está adicionada")
            self.entryName.delete(0, END), self.entryComment.delete(0, END), self.comboboxGenres.set(
                "TERROR"), self.sliderRating.set(0), self.comboboxStatus.set("ANDAMENTO"), self.comboboxType.set("FILME")

    def seeObras(self):
        self.janela.title('Obras')

        self.frameS = ct.CTkFrame(master=self.janela)
        self.frameS.pack(fill="both", expand=True)

        self.createLabel(self.frameS, 3)


view()