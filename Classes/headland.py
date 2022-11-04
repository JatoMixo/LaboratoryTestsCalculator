from tkinter import *

class Headland:

    def __init__(self, root):
        self.title = ""
        self.sub_headlands = []
        self.paragraph = ""
        self.images = []
        self.graphs = []
        self.root = root
    
    def add_subheadland(self):
        self.sub_headlands.append(Headland())
    
    def add_image(self):
        self.images.append("")
    
    def show(self):
        title_lbl = Label(self.root, text=self.title)
        for headland in self.sub_headlands: headland.show()
        paragraphs_lbl = []
        for paragraph in  self.paragraphs: paragraphs_lbl.append(Label(self.root, text=paragraph))