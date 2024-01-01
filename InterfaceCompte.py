import tkinter
import random
import json
import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile

def toggle_interest_entry_state():
    # Obtenez la valeur du bouton radio sélectionné
    account_type = account_type_var.get()
    # Si c'est un compte courant, activez la case de saisie du taux d'intérêt
    if account_type == "Courant":
        decouvert_entry.config(state=tk.NORMAL)
        Taux_interet_entry.config(state=tk.DISABLED)
    else:
        decouvert_entry.config(state=tk.DISABLED)
        Taux_interet_entry.config(state=tk.NORMAL)

def writeToJSONFile(prop, solde ,fileName):
        json.dump(prop, solde)



window = tkinter.Tk()
window.title("Application de création de comptes dans une banque")

# Variable de contrôle pour les boutons radio
account_type_var = tk.StringVar()
account_type_var.set("Courant Epargne")  # Par defaut 

# Create and pack widgets
frame = tkinter.Frame(window)
frame.pack()

#saving user info 
user_info_frame = tkinter.LabelFrame(frame,text="User information")
user_info_frame.grid(row=0 , column=0 , padx=60, pady=60)
 
nbr = random.randint(1,99999)
numero = tkinter.Label(user_info_frame, text=" Numero : " )
numero.grid(row=0 ,column=0)
nbr1 = tkinter.Label(user_info_frame, text= nbr )
nbr1.grid(row=0 ,column=1)


prop = tkinter.Label(user_info_frame, text=" Propriétaire :")
prop.grid(row=1 ,column=0)
sold_int = tkinter.Label(user_info_frame, text="Solde initial :" , )
sold_int.grid(row=2 ,column=0 )

euro = tkinter.Label(user_info_frame, text="Euro")
euro.grid(row=2 , column=2)

prop_entry = tkinter.Entry(user_info_frame)
sold_int_entry = tkinter.Entry(user_info_frame)
prop_entry.grid(row=1 ,column=1)
sold_int_entry.grid(row=2 ,column=1)

title_label = tkinter.Label(user_info_frame, text="Type")
title_label.grid(row=3 , column=0 )

choix1 = Radiobutton(user_info_frame,text="Courant",variable=account_type_var , value="Courant", command=toggle_interest_entry_state )
choix1.grid(row=3, column=1)
choix2 = Radiobutton(user_info_frame,text="Epargne" , variable=account_type_var , value="Epargne", command=toggle_interest_entry_state)
choix2.grid(row=3 , column=2)


Taux_interet= tkinter.Label(user_info_frame, text=" Taux interet :")
Taux_interet.grid(row=4 , column=0)
Taux_interet_entry= tkinter.Entry(user_info_frame)
Taux_interet_entry.grid(row=4 , column=1)
Taux_interetsl = tkinter.Label(user_info_frame, text="%")
Taux_interetsl.grid(row=4 , column=2)

decouvert= tkinter.Label(user_info_frame, text=" M.Decouvert :")
decouvert.grid(row=5 , column=0)
decouvert_entry= tkinter.Entry(user_info_frame)
decouvert_entry.grid(row=5 , column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10 , pady=5)


#term_check = tkinter.Checkbutton(user_info_frame, text="Les informations sont correctes ? ")
#term_check.grid(row=6 , column=0)

 
def enter_data():
    proprietaire = prop_entry.get()
    solde_initial = sold_int_entry.get()
    montantDec = decouvert_entry.get()
    tauxIntr = Taux_interet_entry.get()
    #choix_1 = choix1_.get()
    print("numero de compte  : ",nbr)
    print("Proprietaire : ",proprietaire)
    print("Solde initial : " , solde_initial)
    print("le type de compte : " ) 
    account_type = account_type_var.get()

    if account_type == "Courant":
        print("Courant")
        print("Montant Decouvert : ",montantDec)
    else:
        print("Epargne") 
        print("Taux interet : ",tauxIntr)
        
    data = {}
    data['nbr'] = nbr
    data['proprietaire '] = proprietaire
    data['solde initial '] = solde_initial
    data['Taux interet '] = tauxIntr
    data['Montant Decouvert '] = montantDec
    files = [('JSON File', '*.json')]
    fileName='DataSave'
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='DataSave')
    writeToJSONFile(filepos, fileName, data)

check_button = Button(user_info_frame, text="Creation compte" , command=enter_data)
check_button.grid(row=8 , column=1 , sticky="news" , padx=20 , pady=20)


window.mainloop()