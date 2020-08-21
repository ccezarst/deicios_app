from tkinter import *
import random
import mysql.connector
from tkinter import messagebox
import restart
import time


frame = Tk()
frame.geometry("470x500")
frame.title("Delicios app")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Pufosul``#",
    database="delicios_app_database"
)
dbcursor = db.cursor()

databasecolumns = ("cod_produs", "denumire", "funizor", "categorie", "regula_pret", "cost_de_achizitie", "marja_comerciala", "comestibil")
list1 = ["entry1", "entry2", "entry3", "entry4", "entry5", "entry6", "entry7", "entry8", "entry9"]
colors = ["red", "blue", "green", "black", "#00ff00", "#0000ff", "#3333ff", "#ff3300"]
tosave = [ ]
buttonlist = [ ]
buttonposlist = [ ]

def ShowText(text):
    print(text)
    label = Label(frame, text=text, bg=random.choice(colors), fg="white", padx=20, pady=20)
    label.grid(row=15, column=1)

def Save():
    check=True
    tosave = [ ]
    for entry in list1:
        forcheck = entry.get()
        print(forcheck.isspace)
        if forcheck.isspace() or forcheck == "":
            if check:
                messagebox.showwarning("Nu sunt toate variabilele!", "Trebuie sa pui toate varibilele ca sa salvezi!")
                check = False
            entry.config({"background": "red"})
            tosave.append(False)
        else:
            tosave.append(True)
        for item in tosave:
            if item == False:
                save = False
            else:
                save = True

    if save:
        if entry4.get() == entry5.get():
            messagebox.showwarning("Nu poti sa faci asa ceva!", "Alege terog categoria!")
        else:
            save  = False
            for entry in list1:
                entry.config({"background": "yellow"})
            formula = "INSERT INTO produse (cod_produs, denumire, furnizor, categorie, regula_pret, cost_de_achizitie, marja_comerciala, comestibil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            text = (entry1.get(), entry2.get(), entry3.get(), categorie, entry6.get(), entry7.get(), entry8.get(), comestibil)
            dbcursor.execute(formula, text)
            db.commit()
            ShowText("Saved!")


entry1 = Entry(frame, bg='yellow')
entry1.grid(row=0, column=1)
list1[0] = entry1

entry2 = Entry(frame, bg='yellow')
entry2.grid(row=1, column=1)
list1[1] = entry2
 
entry3 = Entry(frame, bg='yellow')
entry3.grid(row=2, column=1)
list1[2] = entry3
 
entry4 = Entry(frame, bg='yellow')
entry4.grid(row=3, column=1)
list1[3] = entry4
 
entry5 = Entry(frame, bg='yellow')
entry5.grid(row=4, column=1)
list1[4] = entry5
 
entry6 = Entry(frame, bg='yellow')
entry6.grid(row=5, column=1)
list1[5] = entry6
 
entry7 = Entry(frame, bg='yellow')
entry7.grid(row=6, column=1)
list1[6] = entry7
 
entry8 = Entry(frame, bg='yellow')
entry8.grid(row=7, column=1)
list1[7] = entry8
 
entry9 = Entry(frame, bg='yellow')
entry9.grid(row=8, column=1)
list1[8] = entry9


restarted = open("temporary.txt", "r+")
restartedcontents = restarted.readlines()
restarted.write("")
i = 0
for item in restartedcontents:
    if item == "\n":
        pass
        i += 1
        print(i)
    else:
        list1[i].insert(0, item)
        i += 1
        print(i)
restarted.write("")
restarted.close()


def insert(buttonid):
    formula = "SELECT * FROM produse WHERE id = " + str(buttonid) + ""
    dbcursor.execute(formula)
    i = 0
    text = dbcursor.fetchall()
    text = list(text[0])
    del text[8]
    print(text)
    inserttext = True
    raisei = True
    for entry in list1:
        if raisei:
            if i == 3:
                if text[i] == 1:
                    entry4.insert(0, "da")
                    entry5.insert(0, "nu")
                elif text[i] == 2:
                    entry4.insert(0, "nu")
                    entry5.insert(0, "da")
                raisei = False

            if i == 7:
                if text[i] == 1:
                    entry9.insert(0, "da")
                elif text[i] == 0:
                    entry9.insert(0, "nu")
                raisei = False

            if i <= 7:
                entry.insert(0, text[i])
            if i != 4:
                i += 1
            print(i)
        else:
            rasei = True

def Load():

    i = -1
    row = 0
    column = 0
    second_frame = Toplevel()
    second_frame.title("Database entrys")
    second_frame.configure(bg="gray")
    second_frame.geometry("300x600")
    dbcursor.execute("SELECT * FROM produse")
    dbentry = dbcursor.fetchall()
    for tupple in dbentry:
        if row == 30:
            row = 0
            column += 1
        else:
            buttonlist.append(Button(second_frame, text=tupple[1], command=lambda: insert(row)))
            buttonlist[i+1].grid(column=column, row=row)
            buttonposlist.append(row)
            i += 1
            row += 1
        print(i)
        '''
    except Exception:
        messagebox.showerror("Some thing went wrong!", "Error!")
        answer = messagebox.askquestion("Want to restart?", "Want to restart the program?Everything will be saved and reloaded")
        if answer == "yes":
            file = open("temporary.txt", "w")
            entrylist = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get(), entry9.get()]
            print(entrylist)
            file.close()
            file = open("temporary.txt", "a")
            for item in entrylist:
                file.write(item)
                file.write("\n")
            file.close()
            time.sleep(1)
            restart.restart()
            frame.quit()
        else:
            pass'''

label1 = Label(frame, text="Cod Produs").grid(row=0, column=0)
label2 = Label(frame, text="Denumire").grid(row=1, column=0)
label3 = Label(frame, text="Furnizor").grid(row=2, column=0)
label4 = Label(frame, text="Categorie 1").grid(row=3, column=0)
label5 = Label(frame, text="Categorie 2").grid(row=4, column=0)
label6 = Label(frame, text="Regula pret").grid(row=5, column=0)
label7 = Label(frame, text="Cost de achizitie").grid(row=6, column=0)
label8 = Label(frame, text="Marja commerciala").grid(row=7, column=0)
label9 = Label(frame, text="Comestibil").grid(row=8, column=0)



exportbutton = Button(frame, text="Export", command=lambda: ShowText("Exported!"), width=10)
exportbutton.grid(row=10, column=0)
savebutton = Button(frame, text="Salveaza in bazadedate", command=Save, width=20)
savebutton.grid(row=10, column=1)
loadbutton = Button(frame, text="Incarca din bazadedate", command=Load, width=20)
loadbutton.grid(row=10, column=2)
savefromexcelbutton = Button(frame, text="Salveaza dintrun fisier excel")
savefromexcelbutton.grid(row=11, column=0)
frame.mainloop()
