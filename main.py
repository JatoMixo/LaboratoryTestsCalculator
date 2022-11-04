# Made and Code by JatoMixo
# - Twitter: @JatoMixo_Gamer
# - Web: jatomixo.com
from tkinter import *
from Classes import headland

headlands = [0]

def add_headland(root):
    headlands.append(headland.Headland(root))

def main():
    # Window
    root = Tk()

    # First headland
    headlands[0] = headland.Headland(root)

    # Navbar menus
    headland_menu = Menu(root)
    headland_add = Menu(headland_menu)

    # Navbar menus and commands
    headland_add.add_command(label="New Headland", command="add_headland")
    headland_menu.add_cascade(label="Headland", menu=headland_add)

    root.config(menu=headland_menu)

    # Personalize it    
    root.title("JatoMixo - Laboratory Tests Calculator")
    root.iconbitmap("D:/Miguel/Programas/LaboratoryTestsElaborator/logo.ico")
    root.geometry("630x891")

    # Title
    title_indicator = Label(root, text="Title: ")
    title_indicator.grid()

    title = Entry(root, width=95)
    title.grid(column=1, row=0)

    # Headlands Title
    headlands_title_lbl = Label(root, text="Headlands")
    headlands_title_lbl.grid()

    # Headland Variables
    headlands_objects = [
        {
            "Title" : Entry(textvariable=headlands[0].title, width=95),
            "Paragraph" : Entry(textvariable=headlands[0].paragraph, width=95), 
        },

    ]

    for h in headlands_objects:
        h["Title"].grid()
        h["Paragraph"].grid()



    # Mainloop
    root.mainloop()

if __name__ == "__main__":
    main()