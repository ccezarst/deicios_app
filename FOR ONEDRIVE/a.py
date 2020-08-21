from tkinter import *
import mysql.connector

'''running = True
returned = False
show = True


frame = Tk()
frame.geometry("400x500")
frame.title("Delicios app")
frame.wm_attributes("-alpha", 0)'''




db = mysql.connector.connect(
    host="localhost",
    username="root",
    passwd="Pufosul``#",
    database="delicios_app_database"
)
dbcursor = db.cursor()

'''
def returna():
    returned = True
    running = False
    frame.wm_attributes("-alpha", 0)

label1 = Label(frame, text="Terog scrie id-ul produsului care vrei sa i'l incarci")
label1.pack()
entry1 = Entry(frame, bg="yellow")
entry1.pack()
button1 = Button(frame, text="Incarca", width=15, command=returna)
button1.pack()
button1.place(y=20, x=270)
text = Entry(frame)
text.pack(padx=10, pady=200)

def load():
    frame.wm_attributes("-alpha", 1)

    text.delete(0, END)
    
    for item in dbcursor:
        result = str(item) + "\n "
        text.insert(0, result)
    
    frame.mainloop()   
    while running:
        if returned:
            return entry1.get()'''

dbcursor.execute("CREATE TABLE produse (cod_produs VARCHAR(255), denumire VARCHAR(255), furnizor VARCHAR(255), categorie VARCHAR(255), regula_pret VARCHAR(255), cost_de_achizitie VARCHAR(255), marja_comerciala VARCHAR(255), comestibil SMALLINT, id INT AUTO_INCREMENT PRIMARY Key)")

db.commit()
