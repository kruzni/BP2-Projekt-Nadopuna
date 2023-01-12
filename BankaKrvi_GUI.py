import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import tkinter as tk

#konekcija

def connection(): 
            conn=pymysql.connect(host='localhost',user='root',password='root',database="baza_banke_krvi")
            return conn

def refreshTable():
            for data in my_tree.get_children():
                my_tree.delete(data)
                
            for array in read():
                my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
                
            my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
            my_tree.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
    
#GUI

root = Tk()
root.title("Banka krvi")
root.geometry("1800x900")
root.iconbitmap("krv.ico")
my_tree = ttk.Treeview(root)

#rezervirana mjesta za upis
rezmj1=tk.StringVar()
rezmj2=tk.StringVar()
rezmj3=tk.StringVar()
rezmj4=tk.StringVar()
rezmj5=tk.StringVar()
rezmj6=tk.StringVar()
rezmj7=tk.StringVar()
rezmj8=tk.StringVar()
rezmj9=tk.StringVar()

#postavljanje vrijednosti za rez mjesta

def postRezMj(rijec, broj):
    if broj == 1:
        rezmj1.set(rijec)
    if broj == 2:
        rezmj2.set(rijec)
    if broj == 3:
        rezmj3.set(rijec)
    if broj == 4:
        rezmj4.set(rijec)
    if broj == 5:
        rezmj5.set(rijec)
    if broj == 6:
        rezmj6.set(rijec)
    if broj == 7:
        rezmj7.set(rijec)
    if broj == 8:
        rezmj8.set(rijec)
    if broj == 9:
        rezmj9.set(rijec)    


#GUI
def clicki():
    w2=Toplevel()
    w2.title("Sustav Banke krvi")
    w2.geometry("600x600")
    w2.iconbitmap('krv.ico')
    w2['bg'] = '#9E5D5D'
    def zaposlenik_fnk():
        def connection(): 
            conn=pymysql.connect(host='localhost',user='root',password='root',database="baza_banke_krvi")
            return conn

        def refreshTable():
            for data in my_tree.get_children():
                my_tree.delete(data)
                
            for array in read():
                my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
                
            my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
            my_tree.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
        def read():
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM zaposlenik")
            rez=cursor.fetchall()
            conn.commit()
            conn.close()
            return rez

        def add():
            id=str(zaposlenikIDEntry.get())
            ime=str(zaposlenikImeEntry.get())
            prezime=str(zaposlenikPrezimeEntry.get())
            datum_rodenja=str(zaposlenikDatumRodenjaEntry.get())
            adresa=str(zaposlenikAdresaEntry.get())
            grad=str(zaposlenikGradEntry.get())
            kontakt=str(zaposlenikKontaktEntry.get())
            email=str(zaposlenikEmailEntry.get())
            datum_zaposlenja=str(zaposlenikDatumZaposlenjaEntry.get())
            
            if (id=="" or id==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ") or (datum_zaposlenja=="" or datum_zaposlenja==" "):
                messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    cursor.execute("INSERT INTO zaposlenik VALUES ('"+id+"','"+ime+"','"+prezime+"','"+datum_rodenja+"','"+adresa+"','"+grad+"','"+kontakt+"','"+email+"','"+datum_zaposlenja+"') ")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Id zaposlenika već postoji!")
                    return
                
            refreshTable()
            
        def reset():
            odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati sve podatke")
            if odluka != "Da":
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    cursor.execute("DELETE FROM zaposlenik")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Nema podataka za izbrisati!")
                    return
                
            refreshTable()

        def delete():
            odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati zaposlenika")
            if odluka != "yes":
                return
            else:
                odabrani_zaposlenik=my_tree.selection()[0]
                izbrisiPodatak=str(my_tree.item(odabrani_zaposlenik)['values'][0])
                conn=connection()
                cursor=conn.cursor()
                query = "DELETE FROM zaposlenik WHERE id = %s"
                cursor.execute(query, (izbrisiPodatak,))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Info","Zaposlenik uspješno izbrisan!")
            refreshTable()
            
        def select():
                try:
                    odabrani_zaposlenik=my_tree.selection()[0]
                    id=str(my_tree.item(odabrani_zaposlenik)['values'][0])
                    ime=str(my_tree.item(odabrani_zaposlenik)['values'][1])
                    prezime=str(my_tree.item(odabrani_zaposlenik)['values'][2])
                    datum_rodenja=str(my_tree.item(odabrani_zaposlenik)['values'][3])
                    adresa=str(my_tree.item(odabrani_zaposlenik)['values'][4])
                    grad=str(my_tree.item(odabrani_zaposlenik)['values'][5])
                    kontakt=str(my_tree.item(odabrani_zaposlenik)['values'][6])
                    email=str(my_tree.item(odabrani_zaposlenik)['values'][7])
                    datum_zaposlenja=str(my_tree.item(odabrani_zaposlenik)['values'][8])
                
                    postRezMj(id,1)
                    postRezMj(ime,2)
                    postRezMj(prezime,3)
                    postRezMj(datum_rodenja,4)
                    postRezMj(adresa,5)
                    postRezMj(grad,6)
                    postRezMj(kontakt,7)
                    postRezMj(email,8)
                    postRezMj(datum_zaposlenja,9)
                except:
                    messagebox.showinfo("Pogreška!","Molimo izaberite podatak")
                    
        def search():
            id=str(zaposlenikIDEntry.get())
            ime=str(zaposlenikImeEntry.get())
            prezime=str(zaposlenikPrezimeEntry.get())
            datum_rodenja=str(zaposlenikDatumRodenjaEntry.get())
            adresa=str(zaposlenikAdresaEntry.get())
            grad=str(zaposlenikGradEntry.get())
            kontakt=str(zaposlenikKontaktEntry.get())
            email=str(zaposlenikEmailEntry.get())
            datum_zaposlenja=str(zaposlenikDatumZaposlenjaEntry.get())
            if id is None or id == "":
                id = '%'
            if ime is None or ime == "":
                ime = '%'
            if prezime is None or prezime == "":
                prezime = '%'
            if datum_rodenja is None or datum_rodenja == "":
                datum_rodenja = '%'
            if adresa is None or adresa == "":
                adresa = '%'
            if grad is None or grad == "":
                grad = '%'
            if kontakt is None or kontakt == "":
                kontakt = '%'
            if email is None or email == "":
                email = '%'
            if datum_zaposlenja is None or datum_zaposlenja == "":
                datum_zaposlenja = '%'
            conn=connection()
            cursor=conn.cursor()
            query = "SELECT * FROM zaposlenik WHERE id like %s or ime like %s or prezime like %s or datum_rodenja like %s or adresa like %s or grad like %s or kontakt like %s or email like %s or datum_zaposlenja like %s"
            cursor.execute(query, (id, ime, prezime, datum_rodenja, adresa, grad, kontakt, email, datum_zaposlenja))
            rows = cursor.fetchall()
            match = False
            for row in rows:
                if str(row[0]) == id:
                    match = True
                    for i in range(0,9):
                        postRezMj(row[i],(i+1))
            if not match:
                messagebox.showinfo("Error!","No matching data found!")
            conn.commit()
            conn.close()
            
        def update():
            odabraniZaposlenik=""
            try:
                odabrani_zaposlenik=my_tree.selection()[0]
                odabraniZaposlenik=str(my_tree.item(odabrani_zaposlenik)['values'][0])
            except:
                messagebox.showinfo("Pogreška!","Odaberite zaposlenika!")
                
            id=str(zaposlenikIDEntry.get())
            ime=str(zaposlenikImeEntry.get())
            prezime=str(zaposlenikPrezimeEntry.get())
            datum_rodenja=str(zaposlenikDatumRodenjaEntry.get())
            adresa=str(zaposlenikAdresaEntry.get())
            grad=str(zaposlenikGradEntry.get())
            kontakt=str(zaposlenikKontaktEntry.get())
            email=str(zaposlenikEmailEntry.get())
            datum_zaposlenja=str(zaposlenikDatumZaposlenjaEntry.get())
            
            if (id=="" or id==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ") or (datum_zaposlenja=="" or datum_zaposlenja==" "):
                messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    if id is None or id == "":
                        id = '%'
                    if ime is None or ime == "":
                        ime = '%'
                    if prezime is None or prezime == "":
                        prezime = '%'
                    if datum_rodenja is None or datum_rodenja == "":
                        datum_rodenja = '%'
                    if adresa is None or adresa == "":
                        adresa = '%'
                    if grad is None or grad == "":
                        grad = '%'
                    if kontakt is None or kontakt == "":
                        kontakt = '%'
                    if email is None or email == "":
                        email = '%'
                    if datum_zaposlenja is None or datum_zaposlenja == "":
                        datum_zaposlenja = '%'
                    
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Id zaposlenika već postoji!")
                    return








        zaposlenik_w=Toplevel()
        zaposlenik_w.title('What the f')
        zaposlenik_w.geometry('1800x800')
        
        label = Label(zaposlenik_w, text = "Sustav upravljanja zaposlenicima", font=('Arial Bold',30))
        label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

        zaposlenikIDLabel = Label(zaposlenik_w,text = "id",font=('Arial',15))
        zaposlenikImeLabel = Label(zaposlenik_w,text = "Ime zaposlenika",font=('Arial',15)) 
        zaposlenikPrezimeLabel = Label(zaposlenik_w,text = "Prezime zaposlenika",font=('Arial',15)) 
        zaposlenikDatumRodenjaLabel = Label(zaposlenik_w,text = "Datum rođenja zaposlenika",font=('Arial',15)) 
        zaposlenikAdresaLabel = Label(zaposlenik_w,text = "Adresa zaposlenika",font=('Arial',15)) 
        zaposlenikGradLabel = Label(zaposlenik_w,text = "Grad zaposlenika",font=('Arial',15)) 
        zaposlenikKontaktLabel = Label(zaposlenik_w,text = "Kontakt zaposlenika",font=('Arial',15)) 
        zaposlenikEmailLabel = Label(zaposlenik_w,text = "Email zaposlenika",font=('Arial',15)) 
        zaposlenikDatumZaposlenjaLabel = Label(zaposlenik_w,text = "Datum zaposlenja zaposlenika",font=('Arial',15))  

        zaposlenikIDLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikImeLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikPrezimeLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikDatumRodenjaLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikAdresaLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikGradLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikKontaktLabel.grid(row=9,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikEmailLabel.grid(row=10,column=0,columnspan=1,padx=50,pady=5)
        zaposlenikDatumZaposlenjaLabel.grid(row=11,column=0,columnspan=1,padx=50,pady=5)

        zaposlenikIDEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj1)
        zaposlenikImeEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj2)
        zaposlenikPrezimeEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj3)
        zaposlenikDatumRodenjaEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj4)
        zaposlenikAdresaEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj5)
        zaposlenikGradEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj6)
        zaposlenikKontaktEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj7)
        zaposlenikEmailEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj8)
        zaposlenikDatumZaposlenjaEntry=Entry(zaposlenik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj9)

        zaposlenikIDEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikImeEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikPrezimeEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikDatumRodenjaEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikAdresaEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikGradEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikKontaktEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikEmailEntry.grid(row=10,column=1,columnspan=4,padx=5,pady=0)
        zaposlenikDatumZaposlenjaEntry.grid(row=11,column=1,columnspan=4,padx=5,pady=0)


        addBtn=Button(zaposlenik_w, text="Dodaj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=add)
        updateBtn=Button(zaposlenik_w, text="Ažuriraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=update)
        deleteBtn=Button(zaposlenik_w, text="Izbriši",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=delete)
        searchBtn=Button(zaposlenik_w, text="Pretraži",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=search)
        resetBtn=Button(zaposlenik_w, text="Resetiraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=reset)
        selectBtn=Button(zaposlenik_w, text="Izaberi",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=select)

        addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
        updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
        deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
        searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
        resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
        selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

        style=ttk.Style()
        style.configure("Treeview.Heading",font=('Arial Bold',15))
        my_tree['columns']=("id","ime","prezime","datum_rodenja","adresa","grad","kontakt","email","datum_zaposlenja")
        my_tree.column('#0',width=0,stretch=NO)

        my_tree.column("id",anchor=W,width=170)
        my_tree.column("ime",anchor=W,width=170)
        my_tree.column("prezime",anchor=W,width=170)
        my_tree.column("datum_rodenja",anchor=W,width=170)
        my_tree.column("adresa",anchor=W,width=170)
        my_tree.column("grad",anchor=W,width=170)
        my_tree.column("kontakt",anchor=W,width=170)
        my_tree.column("email",anchor=W,width=170)
        my_tree.column("datum_zaposlenja",anchor=W,width=170)

        my_tree.heading("id",text="id",anchor=W)
        my_tree.heading("ime",text="ime",anchor=W)
        my_tree.heading("prezime",text="prezime",anchor=W)
        my_tree.heading("datum_rodenja",text="datum_rodenja",anchor=W)
        my_tree.heading("adresa",text="adresa",anchor=W)
        my_tree.heading("grad",text="grad",anchor=W)
        my_tree.heading("kontakt",text="kontakt",anchor=W)
        my_tree.heading("email",text="email",anchor=W)
        my_tree.heading("datum_zaposlenja",text="datum_zaposlenja",anchor=W)


    zaposlenik_txt = zaposlenik_create_txt = Label(w2, text = 'Podaci o zaposleniku').pack()
    zaposlenik_create_button = Button(w2, text = 'Zaposlenik CRUD', command=zaposlenik_fnk, fg = 'white', bg='blue', padx=15, pady=15, font='sans-serif').pack()
    
    #---------------------------------------------------------------------------------------------------------------------------------------------#
    
    

    
    
    def prijevoznik_fnk():
        def connection(): 
            conn=pymysql.connect(host='localhost',user='root',password='root',database="baza_banke_krvi")
            return conn

        def refreshTable():
            for data in my_tree.get_children():
                my_tree.delete(data)
                
            for array in read():
                my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
                
            my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
            my_tree.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
        def read():
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM prijevoznik")
            rez=cursor.fetchall()
            conn.commit()
            conn.close()
            return rez

        def add():
            id=str(prijevoznikIDEntry.get())
            ime=str(prijevoznikImeEntry.get())
            prezime=str(prijevoznikPrezimeEntry.get())
            datum_rodenja=str(prijevoznikDatumRodenjaEntry.get())
            adresa=str(prijevoznikAdresaEntry.get())
            grad=str(prijevoznikGradEntry.get())
            kontakt=str(prijevoznikKontaktEntry.get())
            email=str(prijevoznikEmailEntry.get())
            datum_zaposlenja=str(prijevoznikDatumZaposlenjaEntry.get())
            
            if (id=="" or id==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ") or (datum_zaposlenja=="" or datum_zaposlenja==" "):
                messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    cursor.execute("INSERT INTO prijevoznik VALUES ('"+id+"','"+ime+"','"+prezime+"','"+datum_rodenja+"','"+adresa+"','"+grad+"','"+kontakt+"','"+email+"','"+datum_zaposlenja+"') ")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Id prijevoznika već postoji!")
                    return
                
            refreshTable()
            
        def reset():
            odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati sve podatke")
            if odluka != "Da":
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    cursor.execute("DELETE FROM prijevoznik")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Nema podataka za izbrisati!")
                    return
                
            refreshTable()

        def delete():
            odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati prijevoznika")
            if odluka != "yes":
                return
            else:
                odabrani_prijevoznik=my_tree.selection()[0]
                izbrisiPodatak=str(my_tree.item(odabrani_prijevoznik)['values'][0])
                conn=connection()
                cursor=conn.cursor()
                query = "DELETE FROM prijevoznik WHERE id = %s"
                cursor.execute(query, (izbrisiPodatak,))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Info","prijevoznik uspješno izbrisan!")
            refreshTable()
            
        def select():
                try:
                    odabrani_prijevoznik=my_tree.selection()[0]
                    id=str(my_tree.item(odabrani_prijevoznik)['values'][0])
                    ime=str(my_tree.item(odabrani_prijevoznik)['values'][1])
                    prezime=str(my_tree.item(odabrani_prijevoznik)['values'][2])
                    datum_rodenja=str(my_tree.item(odabrani_prijevoznik)['values'][3])
                    adresa=str(my_tree.item(odabrani_prijevoznik)['values'][4])
                    grad=str(my_tree.item(odabrani_prijevoznik)['values'][5])
                    kontakt=str(my_tree.item(odabrani_prijevoznik)['values'][6])
                    email=str(my_tree.item(odabrani_prijevoznik)['values'][7])
                    datum_zaposlenja=str(my_tree.item(odabrani_prijevoznik)['values'][8])
                
                    postRezMj(id,1)
                    postRezMj(ime,2)
                    postRezMj(prezime,3)
                    postRezMj(datum_rodenja,4)
                    postRezMj(adresa,5)
                    postRezMj(grad,6)
                    postRezMj(kontakt,7)
                    postRezMj(email,8)
                    postRezMj(datum_zaposlenja,9)
                except:
                    messagebox.showinfo("Pogreška!","Molimo izaberite podatak")
                    
        def search():
            id=str(prijevoznikIDEntry.get())
            ime=str(prijevoznikImeEntry.get())
            prezime=str(prijevoznikPrezimeEntry.get())
            datum_rodenja=str(prijevoznikDatumRodenjaEntry.get())
            adresa=str(prijevoznikAdresaEntry.get())
            grad=str(prijevoznikGradEntry.get())
            kontakt=str(prijevoznikKontaktEntry.get())
            email=str(prijevoznikEmailEntry.get())
            datum_zaposlenja=str(prijevoznikDatumZaposlenjaEntry.get())
            if id is None or id == "":
                id = '%'
            if ime is None or ime == "":
                ime = '%'
            if prezime is None or prezime == "":
                prezime = '%'
            if datum_rodenja is None or datum_rodenja == "":
                datum_rodenja = '%'
            if adresa is None or adresa == "":
                adresa = '%'
            if grad is None or grad == "":
                grad = '%'
            if kontakt is None or kontakt == "":
                kontakt = '%'
            if email is None or email == "":
                email = '%'
            if datum_zaposlenja is None or datum_zaposlenja == "":
                datum_zaposlenja = '%'
            conn=connection()
            cursor=conn.cursor()
            query = "SELECT * FROM prijevoznik WHERE id like %s or ime like %s or prezime like %s or datum_rodenja like %s or adresa like %s or grad like %s or kontakt like %s or email like %s or datum_zaposlenja like %s"
            cursor.execute(query, (id, ime, prezime, datum_rodenja, adresa, grad, kontakt, email, datum_zaposlenja))
            rows = cursor.fetchall()
            match = False
            for row in rows:
                if str(row[0]) == id:
                    match = True
                    for i in range(0,9):
                        postRezMj(row[i],(i+1))
            if not match:
                messagebox.showinfo("Error!","No matching data found!")
            conn.commit()
            conn.close()
            
        def update():
            odabraniprijevoznik=""
            try:
                odabrani_prijevoznik=my_tree.selection()[0]
                odabraniprijevoznik=str(my_tree.item(odabrani_prijevoznik)['values'][0])
            except:
                messagebox.showinfo("Pogreška!","Odaberite prijevoznika!")
                
            id=str(prijevoznikIDEntry.get())
            ime=str(prijevoznikImeEntry.get())
            prezime=str(prijevoznikPrezimeEntry.get())
            datum_rodenja=str(prijevoznikDatumRodenjaEntry.get())
            adresa=str(prijevoznikAdresaEntry.get())
            grad=str(prijevoznikGradEntry.get())
            kontakt=str(prijevoznikKontaktEntry.get())
            email=str(prijevoznikEmailEntry.get())
            datum_zaposlenja=str(prijevoznikDatumZaposlenjaEntry.get())
            
            if (id=="" or id==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ") or (datum_zaposlenja=="" or datum_zaposlenja==" "):
                messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    if id is None or id == "":
                        id = '%'
                    if ime is None or ime == "":
                        ime = '%'
                    if prezime is None or prezime == "":
                        prezime = '%'
                    if datum_rodenja is None or datum_rodenja == "":
                        datum_rodenja = '%'
                    if adresa is None or adresa == "":
                        adresa = '%'
                    if grad is None or grad == "":
                        grad = '%'
                    if kontakt is None or kontakt == "":
                        kontakt = '%'
                    if email is None or email == "":
                        email = '%'
                    if datum_zaposlenja is None or datum_zaposlenja == "":
                        datum_zaposlenja = '%'
                    
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Id prijevoznika već postoji!")
                    return


        prijevoznik_w=Toplevel()
        prijevoznik_w.title('Prijevoznik')
        prijevoznik_w.geometry('1800x800')
        
        label = Label(prijevoznik_w, text = "Sustav upravljanja prijevoznicima", font=('Arial Bold',30))
        label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

        prijevoznikIDLabel = Label(prijevoznik_w,text = "id",font=('Arial',15))
        prijevoznikImeLabel = Label(prijevoznik_w,text = "Ime prijevoznika",font=('Arial',15)) 
        prijevoznikPrezimeLabel = Label(prijevoznik_w,text = "Prezime prijevoznika",font=('Arial',15)) 
        prijevoznikDatumRodenjaLabel = Label(prijevoznik_w,text = "Datum rođenja prijevoznika",font=('Arial',15)) 
        prijevoznikAdresaLabel = Label(prijevoznik_w,text = "Adresa prijevoznika",font=('Arial',15)) 
        prijevoznikGradLabel = Label(prijevoznik_w,text = "Grad prijevoznika",font=('Arial',15)) 
        prijevoznikKontaktLabel = Label(prijevoznik_w,text = "Kontakt prijevoznika",font=('Arial',15)) 
        prijevoznikEmailLabel = Label(prijevoznik_w,text = "Email prijevoznika",font=('Arial',15)) 
        prijevoznikDatumZaposlenjaLabel = Label(prijevoznik_w,text = "Datum zaposlenja prijevoznika",font=('Arial',15))  

        prijevoznikIDLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikImeLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikPrezimeLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikDatumRodenjaLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikAdresaLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikGradLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikKontaktLabel.grid(row=9,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikEmailLabel.grid(row=10,column=0,columnspan=1,padx=50,pady=5)
        prijevoznikDatumZaposlenjaLabel.grid(row=11,column=0,columnspan=1,padx=50,pady=5)

        prijevoznikIDEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj1)
        prijevoznikImeEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj2)
        prijevoznikPrezimeEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj3)
        prijevoznikDatumRodenjaEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj4)
        prijevoznikAdresaEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj5)
        prijevoznikGradEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj6)
        prijevoznikKontaktEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj7)
        prijevoznikEmailEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj8)
        prijevoznikDatumZaposlenjaEntry=Entry(prijevoznik_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj9)

        prijevoznikIDEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikImeEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikPrezimeEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikDatumRodenjaEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikAdresaEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikGradEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikKontaktEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikEmailEntry.grid(row=10,column=1,columnspan=4,padx=5,pady=0)
        prijevoznikDatumZaposlenjaEntry.grid(row=11,column=1,columnspan=4,padx=5,pady=0)


        addBtn=Button(prijevoznik_w, text="Dodaj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=add)
        updateBtn=Button(prijevoznik_w, text="Ažuriraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=update)
        deleteBtn=Button(prijevoznik_w, text="Izbriši",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=delete)
        searchBtn=Button(prijevoznik_w, text="Pretraži",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=search)
        resetBtn=Button(prijevoznik_w, text="Resetiraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=reset)
        selectBtn=Button(prijevoznik_w, text="Izaberi",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=select)

        addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
        updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
        deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
        searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
        resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
        selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

        style=ttk.Style()
        style.configure("Treeview.Heading",font=('Arial Bold',15))
        my_tree['columns']=("id","ime","prezime","datum_rodenja","adresa","grad","kontakt","email","datum_zaposlenja")
        my_tree.column('#0',width=0,stretch=NO)

        my_tree.column("id",anchor=W,width=170)
        my_tree.column("ime",anchor=W,width=170)
        my_tree.column("prezime",anchor=W,width=170)
        my_tree.column("datum_rodenja",anchor=W,width=170)
        my_tree.column("adresa",anchor=W,width=170)
        my_tree.column("grad",anchor=W,width=170)
        my_tree.column("kontakt",anchor=W,width=170)
        my_tree.column("email",anchor=W,width=170)
        my_tree.column("datum_zaposlenja",anchor=W,width=170)

        my_tree.heading("id",text="id",anchor=W)
        my_tree.heading("ime",text="ime",anchor=W)
        my_tree.heading("prezime",text="prezime",anchor=W)
        my_tree.heading("datum_rodenja",text="datum_rodenja",anchor=W)
        my_tree.heading("adresa",text="adresa",anchor=W)
        my_tree.heading("grad",text="grad",anchor=W)
        my_tree.heading("kontakt",text="kontakt",anchor=W)
        my_tree.heading("email",text="email",anchor=W)
        my_tree.heading("datum_zaposlenja",text="datum_zaposlenja",anchor=W)
    prijevoznik_txt = prijevoznik_create_txt = Label(w2, text = 'Podaci o zaposleniku').pack()
    prijevoznik_create_button = Button(w2, text = 'Prijevoznik CRUD', command=prijevoznik_fnk, fg = 'white', bg='blue', padx=15, pady=15, font='sans-serif').pack()
    #---------------------------------------------------------------------------------------------------------------------------------------------#











    def darivatelj_fnk():
        def connection(): 
            conn=pymysql.connect(host='localhost',user='root',password='root',database="baza_banke_krvi")
            return conn

        def refreshTable():
            for data in my_tree.get_children():
                my_tree.delete(data)
                
            for array in read():
                my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
                
            my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
            my_tree.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
        def read():
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM darivatelj")
            rez=cursor.fetchall()
            conn.commit()
            conn.close()
            return rez
            
        def reset():
            odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati sve podatke")
            if odluka != "Da":
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    cursor.execute("DELETE FROM darivatelj")
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Nema podataka za izbrisati!")
                    return
                
            refreshTable()

        def delete():
            odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati darivatelja")
            if odluka != "yes":
                return
            else:
                odabrani_darivatelj=my_tree.selection()[0]
                izbrisiPodatak=str(my_tree.item(odabrani_darivatelj)['values'][0])
                conn=connection()
                cursor=conn.cursor()
                query = "DELETE FROM darivatelj WHERE id = %s"
                cursor.execute(query, (izbrisiPodatak,))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Info","darivatelj uspješno izbrisan!")
            refreshTable()
            
        def select():
                try:
                    odabrani_darivatelj=my_tree.selection()[0]
                    id=str(my_tree.item(odabrani_darivatelj)['values'][0])
                    ime=str(my_tree.item(odabrani_darivatelj)['values'][1])
                    prezime=str(my_tree.item(odabrani_darivatelj)['values'][2])
                    datum_rodenja=str(my_tree.item(odabrani_darivatelj)['values'][3])
                    adresa=str(my_tree.item(odabrani_darivatelj)['values'][4])
                    grad=str(my_tree.item(odabrani_darivatelj)['values'][5])
                    kontakt=str(my_tree.item(odabrani_darivatelj)['values'][6])
                    email=str(my_tree.item(odabrani_darivatelj)['values'][7])
                    datum_zaposlenja=str(my_tree.item(odabrani_darivatelj)['values'][8])
                
                    postRezMj(id,1)
                    postRezMj(ime,2)
                    postRezMj(prezime,3)
                    postRezMj(datum_rodenja,4)
                    postRezMj(adresa,5)
                    postRezMj(grad,6)
                    postRezMj(kontakt,7)
                    postRezMj(email,8)
                    postRezMj(datum_zaposlenja,9)
                except:
                    messagebox.showinfo("Pogreška!","Molimo izaberite podatak")
                    
        def search():
            id=str(darivateljIDEntry.get())
            ime=str(darivateljImeEntry.get())
            prezime=str(darivateljPrezimeEntry.get())
            datum_rodenja=str(darivateljDatumRodenjaEntry.get())
            adresa=str(darivateljAdresaEntry.get())
            grad=str(darivateljGradEntry.get())
            kontakt=str(darivateljKontaktEntry.get())
            email=str(darivateljEmailEntry.get())
            datum_zaposlenja=str(darivateljDatumZaposlenjaEntry.get())
            if id is None or id == "":
                id = '%'
            if ime is None or ime == "":
                ime = '%'
            if prezime is None or prezime == "":
                prezime = '%'
            if datum_rodenja is None or datum_rodenja == "":
                datum_rodenja = '%'
            if adresa is None or adresa == "":
                adresa = '%'
            if grad is None or grad == "":
                grad = '%'
            if kontakt is None or kontakt == "":
                kontakt = '%'
            if email is None or email == "":
                email = '%'
            if datum_zaposlenja is None or datum_zaposlenja == "":
                datum_zaposlenja = '%'
            conn=connection()
            cursor=conn.cursor()
            query = "SELECT * FROM darivatelj WHERE id like %s or ime like %s or prezime like %s or datum_rodenja like %s or adresa like %s or grad like %s or kontakt like %s or email like %s or datum_zaposlenja like %s"
            cursor.execute(query, (id, ime, prezime, datum_rodenja, adresa, grad, kontakt, email, datum_zaposlenja))
            rows = cursor.fetchall()
            match = False
            for row in rows:
                if str(row[0]) == id:
                    match = True
                    for i in range(0,9):
                        postRezMj(row[i],(i+1))
            if not match:
                messagebox.showinfo("Error!","No matching data found!")
            conn.commit()
            conn.close()
            
        def update():
            odabranidarivatelj=""
            try:
                odabrani_darivatelj=my_tree.selection()[0]
                odabranidarivatelj=str(my_tree.item(odabrani_darivatelj)['values'][0])
            except:
                messagebox.showinfo("Pogreška!","Odaberite darivatelja!")
                
            id=str(darivateljIDEntry.get())
            ime=str(darivateljImeEntry.get())
            prezime=str(darivateljPrezimeEntry.get())
            datum_rodenja=str(darivateljDatumRodenjaEntry.get())
            adresa=str(darivateljAdresaEntry.get())
            grad=str(darivateljGradEntry.get())
            kontakt=str(darivateljKontaktEntry.get())
            email=str(darivateljEmailEntry.get())
            datum_zaposlenja=str(darivateljDatumZaposlenjaEntry.get())
            
            if (id=="" or id==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ") or (datum_zaposlenja=="" or datum_zaposlenja==" "):
                messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
                return
            else:
                try:
                    conn=connection()
                    cursor=conn.cursor()
                    if id is None or id == "":
                        id = '%'
                    if ime is None or ime == "":
                        ime = '%'
                    if prezime is None or prezime == "":
                        prezime = '%'
                    if datum_rodenja is None or datum_rodenja == "":
                        datum_rodenja = '%'
                    if adresa is None or adresa == "":
                        adresa = '%'
                    if grad is None or grad == "":
                        grad = '%'
                    if kontakt is None or kontakt == "":
                        kontakt = '%'
                    if email is None or email == "":
                        email = '%'
                    if datum_zaposlenja is None or datum_zaposlenja == "":
                        datum_zaposlenja = '%'
                    
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showinfo("Pogreška!","Id darivatelja već postoji!")
                    return



        darivatelj_w=Toplevel()
        darivatelj_w.title('Darivatelji')
        darivatelj_w.geometry('1800x800')
        
        label = Label(darivatelj_w, text = "Sustav upravljanja darivateljima", font=('Arial Bold',30))
        label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

        darivateljIDLabel = Label(darivatelj_w,text = "id",font=('Arial',15))
        darivateljImeLabel = Label(darivatelj_w,text = "Ime darivatelja",font=('Arial',15)) 
        darivateljPrezimeLabel = Label(darivatelj_w,text = "Prezime darivatelja",font=('Arial',15)) 
        darivateljDatumRodenjaLabel = Label(darivatelj_w,text = "Datum rođenja darivatelja",font=('Arial',15)) 
        darivateljAdresaLabel = Label(darivatelj_w,text = "Adresa darivatelja",font=('Arial',15)) 
        darivateljGradLabel = Label(darivatelj_w,text = "Grad darivatelja",font=('Arial',15)) 
        darivateljKontaktLabel = Label(darivatelj_w,text = "Kontakt darivatelja",font=('Arial',15)) 
        darivateljEmailLabel = Label(darivatelj_w,text = "Email darivatelja",font=('Arial',15)) 
        darivateljDatumZaposlenjaLabel = Label(darivatelj_w,text = "Datum zaposlenja darivatelja",font=('Arial',15))  

        darivateljIDLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
        darivateljImeLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
        darivateljPrezimeLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
        darivateljDatumRodenjaLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
        darivateljAdresaLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
        darivateljGradLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
        darivateljKontaktLabel.grid(row=9,column=0,columnspan=1,padx=50,pady=5)
        darivateljEmailLabel.grid(row=10,column=0,columnspan=1,padx=50,pady=5)
        darivateljDatumZaposlenjaLabel.grid(row=11,column=0,columnspan=1,padx=50,pady=5)

        darivateljIDEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj1)
        darivateljImeEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj2)
        darivateljPrezimeEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj3)
        darivateljDatumRodenjaEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj4)
        darivateljAdresaEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj5)
        darivateljGradEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj6)
        darivateljKontaktEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj7)
        darivateljEmailEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj8)
        darivateljDatumZaposlenjaEntry=Entry(darivatelj_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj9)

        darivateljIDEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
        darivateljImeEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
        darivateljPrezimeEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
        darivateljDatumRodenjaEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
        darivateljAdresaEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
        darivateljGradEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
        darivateljKontaktEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)
        darivateljEmailEntry.grid(row=10,column=1,columnspan=4,padx=5,pady=0)
        darivateljDatumZaposlenjaEntry.grid(row=11,column=1,columnspan=4,padx=5,pady=0)


        updateBtn=Button(darivatelj_w, text="Ažuriraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=update)
        deleteBtn=Button(darivatelj_w, text="Izbriši",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=delete)
        searchBtn=Button(darivatelj_w, text="Pretraži",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=search)
        resetBtn=Button(darivatelj_w, text="Resetiraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=reset)
        selectBtn=Button(darivatelj_w, text="Izaberi",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=select)

        updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
        deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
        searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
        resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
        selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

        style=ttk.Style()
        style.configure("Treeview.Heading",font=('Arial Bold',15))
        my_tree['columns']=("id","ime","prezime","datum_rodenja","adresa","grad","kontakt","email","datum_zaposlenja")
        my_tree.column('#0',width=0,stretch=NO)

        my_tree.column("id",anchor=W,width=170)
        my_tree.column("ime",anchor=W,width=170)
        my_tree.column("prezime",anchor=W,width=170)
        my_tree.column("datum_rodenja",anchor=W,width=170)
        my_tree.column("adresa",anchor=W,width=170)
        my_tree.column("grad",anchor=W,width=170)
        my_tree.column("kontakt",anchor=W,width=170)
        my_tree.column("email",anchor=W,width=170)
        my_tree.column("datum_zaposlenja",anchor=W,width=170)

        my_tree.heading("id",text="id",anchor=W)
        my_tree.heading("ime",text="ime",anchor=W)
        my_tree.heading("prezime",text="prezime",anchor=W)
        my_tree.heading("datum_rodenja",text="datum_rodenja",anchor=W)
        my_tree.heading("adresa",text="adresa",anchor=W)
        my_tree.heading("grad",text="grad",anchor=W)
        my_tree.heading("kontakt",text="kontakt",anchor=W)
        my_tree.heading("email",text="email",anchor=W)
        my_tree.heading("datum_zaposlenja",text="datum_zaposlenja",anchor=W)

    darivatelj_txt = darivatelj_create_txt = Label(w2, text = 'Podaci o darivatelju').pack()
    darivatelj_create_button = Button(w2, text = 'Darivatelj CRUD', command=darivatelj_fnk, fg = 'white', bg='blue', padx=15, pady=15, font='sans-serif').pack()
    
    
    
    def bolnica_fnk():
        def connection(): 
            conn=pymysql.connect(host='localhost',user='root',password='root',database="baza_banke_krvi")
            return conn

        def refreshTable():
            for data in my_tree.get_children():
                my_tree.delete(data)
                
            for array in read():
                my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
                
            my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
            my_tree.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
        def select():
                try:
                    odabrana_bolnica=my_tree.selection()[0]
                    id=str(my_tree.item(odabrana_bolnica)['values'][0])
                    ime=str(my_tree.item(odabrana_bolnica)['values'][1])
                    prezime=str(my_tree.item(odabrana_bolnica)['values'][2])
                    datum_rodenja=str(my_tree.item(odabrana_bolnica)['values'][3])
                    adresa=str(my_tree.item(odabrana_bolnica)['values'][4])
                    grad=str(my_tree.item(odabrana_bolnica)['values'][5])
                    kontakt=str(my_tree.item(odabrana_bolnica)['values'][6])
                    email=str(my_tree.item(odabrana_bolnica)['values'][7])
                    datum_zaposlenja=str(my_tree.item(odabrana_bolnica)['values'][8])
                
                    postRezMj(id,1)
                    postRezMj(ime,2)
                    postRezMj(prezime,3)
                    postRezMj(datum_rodenja,4)
                    postRezMj(adresa,5)
                    postRezMj(grad,6)
                    postRezMj(kontakt,7)
                    postRezMj(email,8)
                    postRezMj(datum_zaposlenja,9)
                except:
                    messagebox.showinfo("Pogreška!","Molimo izaberite podatak")
                    
        def search():
            id=str(bolnicaIDEntry.get())
            ime=str(bolnicaImeEntry.get())
            adresa=str(bolnicaAdresaEntry.get())
            grad=str(bolnicaGradEntry.get())
            kontakt=str(bolnicaKontaktEntry.get())
            email=str(bolnicaEmailEntry.get())
            if id is None or id == "":
                id = '%'
            if ime is None or ime == "":
                ime = '%'
            if prezime is None or prezime == "":
                prezime = '%'
            if datum_rodenja is None or datum_rodenja == "":
                datum_rodenja = '%'
            if adresa is None or adresa == "":
                adresa = '%'
            if grad is None or grad == "":
                grad = '%'
            if kontakt is None or kontakt == "":
                kontakt = '%'
            if email is None or email == "":
                email = '%'
            if datum_zaposlenja is None or datum_zaposlenja == "":
                datum_zaposlenja = '%'
            conn=connection()
            cursor=conn.cursor()
            query = "SELECT * FROM bolnica WHERE id like %s or ime like %s or prezime like %s or datum_rodenja like %s or adresa like %s or grad like %s or kontakt like %s or email like %s or datum_zaposlenja like %s"
            cursor.execute(query, (id, ime, prezime, datum_rodenja, adresa, grad, kontakt, email, datum_zaposlenja))
            rows = cursor.fetchall()
            match = False
            for row in rows:
                if str(row[0]) == id:
                    match = True
                    for i in range(0,9):
                        postRezMj(row[i],(i+1))
            if not match:
                messagebox.showinfo("Error!","No matching data found!")
            conn.commit()
            conn.close()

        bolnica_w=Toplevel()
        bolnica_w.title('bolnicai')
        bolnica_w.geometry('1800x800')
        
        label = Label(bolnica_w, text = "Sustav upravljanja bolnicama", font=('Arial Bold',30))
        label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

        bolnicaIDLabel = Label(bolnica_w,text = "id",font=('Arial',15))
        bolnicaImeLabel = Label(bolnica_w,text = "Ime bolnica",font=('Arial',15)) 
        bolnicaAdresaLabel = Label(bolnica_w,text = "Adresa bolnica",font=('Arial',15)) 
        bolnicaGradLabel = Label(bolnica_w,text = "Grad bolnica",font=('Arial',15)) 
        bolnicaKontaktLabel = Label(bolnica_w,text = "Kontakt bolnica",font=('Arial',15)) 
        bolnicaEmailLabel = Label(bolnica_w,text = "Email bolnica",font=('Arial',15))  

        bolnicaIDLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
        bolnicaImeLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5) 
        bolnicaAdresaLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
        bolnicaGradLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
        bolnicaKontaktLabel.grid(row=9,column=0,columnspan=1,padx=50,pady=5)
        bolnicaEmailLabel.grid(row=10,column=0,columnspan=1,padx=50,pady=5)


        bolnicaIDEntry=Entry(bolnica_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj1)
        bolnicaImeEntry=Entry(bolnica_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj2)
        bolnicaAdresaEntry=Entry(bolnica_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj5)
        bolnicaGradEntry=Entry(bolnica_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj6)
        bolnicaKontaktEntry=Entry(bolnica_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj7)
        bolnicaEmailEntry=Entry(bolnica_w,width=55,bd=5,font=('Arial',15), textvariable=rezmj8)

        bolnicaIDEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
        bolnicaImeEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
        bolnicaAdresaEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
        bolnicaGradEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
        bolnicaKontaktEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)
        bolnicaEmailEntry.grid(row=10,column=1,columnspan=4,padx=5,pady=0)



  
        searchBtn=Button(bolnica_w, text="Pretraži",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=search)
        resetBtn=Button(bolnica_w, text="Resetiraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=reset)
        selectBtn=Button(bolnica_w, text="Izaberi",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=select)

        
        searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
        resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
        selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

        style=ttk.Style()
        style.configure("Treeview.Heading",font=('Arial Bold',15))
        my_tree['columns']=("id","ime","adresa","grad","kontakt","email")
        my_tree.column('#0',width=0,stretch=NO)

        my_tree.column("id",anchor=W,width=170)
        my_tree.column("ime",anchor=W,width=170)
        my_tree.column("adresa",anchor=W,width=170)
        my_tree.column("grad",anchor=W,width=170)
        my_tree.column("kontakt",anchor=W,width=170)


        my_tree.heading("id",text="id",anchor=W)
        my_tree.heading("ime",text="ime",anchor=W)
        my_tree.heading("adresa",text="adresa",anchor=W)
        my_tree.heading("grad",text="grad",anchor=W)
        my_tree.heading("kontakt",text="kontakt",anchor=W)
        my_tree.heading("email",text="email",anchor=W)

    bolnica_txt = bolnica_create_txt = Label(w2, text = 'Podaci o bolnici').pack()
    bolnica_create_button = Button(w2, text = 'Bolnica CRUD', command=bolnica_fnk, fg = 'white', bg='blue', padx=15, pady=15, font='sans-serif').pack()
    refreshTable()


butt = Button(root, text = 'Prijava', command=clicki, fg = 'white', bg='blue', padx=15, pady=15, font='sans-serif').pack()
root.mainloop()