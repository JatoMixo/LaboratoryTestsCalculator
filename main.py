# Made and Code by JatoMixo
# - Twitter: @JatoMixo_Gamer
# - Web: jatomixo.com
from tkinter import *

def add_headland():
    pass

def main():
    root = Tk()

    headland_menu = Menu(root)
    headland_add = Menu(headland_menu)

    headland_add.add_command(label="New Headland", command="add_headland")
    headland_menu.add_cascade(label="Headland", menu=headland_add)

    root.config(menu=headland_menu)
    
    root.title("JatoMixo - Laboratory Tests Calculator")
    root.iconbitmap("D:/Miguel/Programas/LaboratoryTestsElaborator/test.ico")
    root.geometry("630x891")

    title_indicator = Label(root, text="Title: ")
    title_indicator.grid()

    title = Entry(root, width=95)
    title.grid(column=1, row=0)

    root.mainloop()

if __name__ == "__main__":
    main()