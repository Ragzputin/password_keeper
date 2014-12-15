# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 11:12:48 2014

@author: raghavkumar
"""

#from Tkinter import Tk, Menu, W, E, RAISED
from ttk import Frame, Button, Label, Style, Entry
#from ttk import Entry
import tkMessageBox
import json
import Tkinter
from Tkinter import *
import os.path

class Primary(Frame):
    #Global Vars

    def __init__(self, parent, dict, enlist):
        Frame.__init__(self, parent)
        self.parent = parent
        self.dict = dict
        self.enlist = enlist
        self.initUI()


    def initUI(self):
        self.parent.title("Password Keeper")

        self.style = Style()
        self.style.theme_use("clam")

        en1 = Entry(self)
        en1.grid(row=2, column=0)
        en2 = Entry(self)
        en2.grid(row=2, column=1)
        en3 = Entry(self)
        en3.grid(row=2, column=2)

        en4 = Entry(self)
        en4.grid(row=3, column=0)
        en5 = Entry(self)
        en5.grid(row=3, column=1)
        en6 = Entry(self)
        en6.grid(row=3, column=2)

        en7 = Entry(self)
        en7.grid(row=4, column=0)
        en8 = Entry(self)
        en8.grid(row=4, column=1)
        en9 = Entry(self)
        en9.grid(row=4, column=2)

        en10 = Entry(self)
        en10.grid(row=5, column=0)
        en11 = Entry(self)
        en11.grid(row=5, column=1)
        en12 = Entry(self)
        en12.grid(row=5, column=2)

        en13 = Entry(self)
        en13.grid(row=6, column=0)
        en14 = Entry(self)
        en14.grid(row=6, column=1)
        en15 = Entry(self)
        en15.grid(row=6, column=2)

        def updatePasswords():
            update_bool = False

            if en1.get() != "":
                self.enlist.append(en1.get())
            if en2.get() != "":
                self.enlist.append(en2.get())
            if en3.get() != "":
                self.enlist.append(en3.get())
            if en4.get() != "":
                self.enlist.append(en4.get())
            if en5.get() != "":
                self.enlist.append(en5.get())
            if en6.get() != "":
                self.enlist.append(en6.get())
            if en7.get() != "":
                self.enlist.append(en7.get())
            if en8.get() != "":
                self.enlist.append(en8.get())
            if en9.get() != "":
                self.enlist.append(en9.get())
            if en10.get() != "":
                self.enlist.append(en10.get())
            if en11.get() != "":
                self.enlist.append(en11.get())
            if en12.get() != "":
                self.enlist.append(en12.get())
            if en13.get() != "":
                self.enlist.append(en13.get())
            if en14.get() != "":
                self.enlist.append(en14.get())
            if en15.get() != "":
                self.enlist.append(en15.get())

            print "Self.enlist values: ", self.enlist

            if len(self.dict) > 0:
                for key in self.dict:
                    for i in range(len(self.enlist)):
                        if i % 3 == 0:
                            if key == self.enlist[i]:
                                tkMessageBox.showinfo(title=None,message="This domain already exists!")
                                break
                            else:
                                update_bool = True

            if update_bool or len(self.dict) == 0:
                ls = []
                key = 0
                dct2 = {}
                for idx,item in enumerate(self.enlist):
                    if idx % 3 == 0:
                        key = item
                        ls = []
                        dct2[key] = []
                    else:
                        ls.append(item)
                        dct2[key] = ls
                        self.dict.update(dct2)

                    print "ls:", ls
                    print "Dict1: ", self.dict
                    print "Dict2: ", dct2

                with open("/Users/raghavkumar/Documents/Python_docs/password_keeper/my_dict.json", "wb") as fp:
                    json.dump(self.dict,fp)

                tkMessageBox.showinfo(title=None,message="Updated!")

        def viewPasswords():
            root = Tk()
            Secondary(root, self.dict)
            root.mainloop()

        def clearRows():
            en1.delete(0, Tkinter.END)
            en2.delete(0, Tkinter.END)
            en3.delete(0, Tkinter.END)
            en4.delete(0, Tkinter.END)
            en5.delete(0, Tkinter.END)
            en6.delete(0, Tkinter.END)
            en7.delete(0, Tkinter.END)
            en8.delete(0, Tkinter.END)
            en9.delete(0, Tkinter.END)
            en10.delete(0, Tkinter.END)
            en11.delete(0, Tkinter.END)
            en12.delete(0, Tkinter.END)
            en13.delete(0, Tkinter.END)
            en14.delete(0, Tkinter.END)
            en15.delete(0, Tkinter.END)

        #_________________________
        #Start of Menu definitions
        #_________________________
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        eraseMenu = Menu(fileMenu)

        fileMenu.add_command(label="View Passwords", command=viewPasswords)
        eraseMenu.add_command(label="Erase All",command=self.eraseAll)
        eraseMenu.add_command(label="Remove Password")
        fileMenu.add_cascade(label="Erase",menu=eraseMenu)
        fileMenu.add_command(label="Exit",command=self.exitApp)
        menubar.add_cascade(label="File",menu=fileMenu)
        #_________________________
        #End of Menu definitions
        #_________________________


        dom = Label(self, text="Domain/Site Name")
        dom.grid(row=1, column=0)
        usr = Label(self, text="Username")
        usr.grid(row=1, column=1)
        pss = Label(self, text="Password")
        pss.grid(row=1,column=2)
        imp = Button(self, text="Import", command=updatePasswords)
        imp.grid(row=0, columnspan=2, sticky = W+E)
        clr = Button(self, text="Clear Rows", command=clearRows)
        clr.grid(row=0, column=2, sticky = W+E)

        self.pack()

    def eraseAll(self):
        del self.enlist[:]
        self.dict = {}
        with open("/Users/raghavkumar/Documents/Python_docs/password_keeper/my_dict.json","wb") as fp:
            json.dump(self.dict,fp)

        tkMessageBox.showinfo(title=None,message="All Passwords Erased!")
        print "Self.dict is now: ", self.dict

    def exitApp(self):
        self.quit()


class Login(Frame):
    def __init__(self, parent, dict, enlist):
        Frame.__init__(self,parent)
        self.parent = parent
        self.dict = dict
        self.enlist = enlist
        self.loginInit()

    def loginInit(self):
        self.parent.title("Password Keeper")
        Style().configure("Tlabel",font="Times")

        lbusr = Label(self,text="Master Username")
        lbusr.grid(row=0,column=0)
        lbps = Label(self,text="Master Password")
        lbps.grid(row=1,column=0)

        enusr = Entry(self)
        enusr.grid(row=0,column=1)
        enps = Entry(self)
        enps.grid(row=1,column=1)

        def login():
            credict = {}
            with open("cred.json","rb") as f:
                credict = json.load(f)

            for key in credict:
                if key == enusr.get() and credict[key] == enps.get():
                    switch()
                elif key != enusr.get() and credict[key] == enps.get():
                    tkMessageBox.showinfo(title=None,message="Wrong Username! Please Re-enter")
                    enusr.delete(0, Tkinter.END)
                    enps.delete(0, Tkinter.END)
                    break
                elif key == enusr.get() and credict[key] != enps.get():
                    tkMessageBox.showinfo(title=None,message="Wrong password! Please Re-enter.")
                    enusr.delete(0, Tkinter.END)
                    enps.delete(0, Tkinter.END)
                    break
                else:
                    tkMessageBox.showinfo(title=None,message="Username/Password combination is wrong! Please Re-enter")
                    enusr.delete(0, Tkinter.END)
                    enps.delete(0, Tkinter.END)
                    break

        def switch():
            self.parent.destroy()
            root = Tk()
            Primary(root,self.dict,self.enlist)
            root.mainloop()

        reg = Button(self,text="New User",command=self.register)
        reg.grid(row=2,column=0,sticky=W+E)
        lgn = Button(self,text="Login",command=login)
        lgn.grid(row=2,column=1,sticky=W+E)

        self.pack()

    def register(self):
        root = Tk()
        if os.path.isfile("cred.json"):
            with open("cred.json","rb") as f:
                dict = json.load(f)
        else:
            dict = {}

        Registration(root,dict)
        root.mainloop()

class Registration(Frame):
    def __init__(self, parent, dict):
        Frame.__init__(self,parent)
        self.parent = parent
        self.dict = dict
        self.registerUI()

    def registerUI(self):
        self.parent.title("Password Keeper Registration")

        Style().configure("Tlabel",font="Courier")

        lbusr = Label(self,text="Enter a Master Username")
        lbusr.grid(row=0,column=0)
        lbps = Label(self,text="Enter a Master Password")
        lbps.grid(row=1,column=0)

        enusr = Entry(self)
        enusr.grid(row=0,column=1)
        enps = Entry(self)
        enps.grid(row=1,column=1)

        def reg():
            dict2 = {}
            if len(self.dict) == 0:
                self.dict[enusr.get()] = enps.get()
            else:
                dict2[enusr.get()] = enps.get()
                self.dict.update(dict2)

            print "Self.dict is now ",self.dict

            with open("cred.json","wb") as f:
                json.dump(self.dict,f)

            tkMessageBox.showinfo(title=None,message="You have registered!")

            """
            with open("cred.json","rb") as f:
                print f.read()
            """
            self.parent.destroy()

        reg = Button(self,text="Register",command=reg)
        reg.grid(row=2,column=0,sticky=W+E)

        self.pack()


class Secondary(Frame):
    def __init__(self, parent, dict):
        Frame.__init__(self,parent)
        self.parent = parent
        self.dict = dict
        self.secinitUI()

    def secinitUI(self):
        self.parent.title("Password Keeper")

        Style().configure("TLabel",font="Times")

        l1 = Label(self,text="Domain",relief=RAISED,bg="green")
        l1.grid(row=0,column=0)
        l2 = Label(self,text="Username",relief=RAISED,bg="green")
        l2.grid(row=0,column=1)
        l3 = Label(self,text="Password",relief=RAISED,bg="green")
        l3.grid(row=0,column=2)

        count = 1
        for key in self.dict:
            new_key = key
            while new_key == key:

                dom = Label(self, text=key)
                dom.grid(row=count,column=0)
                usr = Label(self, text=self.dict[key][0])
                usr.grid(row=count,column=1)
                pss = Label(self, text=self.dict[key][1])
                pss.grid(row=count,column=2)

                new_key = ""
                count += 1

        self.pack()

#End of class definition

def main():
    with open("/Users/raghavkumar/Documents/Python_docs/password_keeper/my_dict.json","rb") as fb:
        if fb:
            d = json.load(fb)
        else:
            d = {}
    enlist = []
    root = Tk()
    app = Login(root, d, enlist)
    root.mainloop()

if __name__ == '__main__':
    main()