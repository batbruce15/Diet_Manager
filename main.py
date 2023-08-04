from tkinter import *
root = Tk()
root.title("Diet manager")

frame1 = LabelFrame(root, text="Veuillez remplir le formulaire suivant svp", pady=20, padx=30)
frame1.pack(padx=20, pady=20)
myLabel = Label(frame1, text="Entrez votre poid")
myLabel.pack()
entry1 = Entry(frame1, width=30, borderwidth=5)
entry1.pack()

myLabel = Label(frame1, text="Entrez votre taille")
myLabel.pack()
entry4 = Entry(frame1, width=30, borderwidth=5)
entry4.pack()

myLabel = Label(frame1, text="Entre votre age")
myLabel.pack()
entry2=Entry(frame1, width=30, borderwidth=5)
entry2.pack()

myLabel = Label(frame1, text="Quel est votre sexe?")
myLabel.pack()

def sexe():
    pass

radioButton1 = Radiobutton(frame1, text="Mal", value="M", command=lambda : sexe()).pack()
radioButton2 = Radiobutton(frame1, text="Femel", value="F").pack()


myLabel = Label(root, text="Resultat").pack()
entry3 = Entry(root, borderwidth=5).pack()
def Calcule_IMC():
    poid = int(entry1.get())
    taille = int(entry4.get())
    imc = poid/(taille*taille)
    entry3.insert(0, str(imc))

Button1 = Button(root, text="Calcule IMC", command=Calcule_IMC).pack()
Button2 = Button(root, text="CaLorie_a_consommer/jour").pack()

frame = LabelFrame(root, text="Commenting the result zone!", padx=50, pady=50)
frame.pack(padx=20, pady=20)
label = Label(frame, text="Repond au formulaire svp").pack()

quit = Button(root, text="Quit", command=quit, padx=40).pack()

root.mainloop()