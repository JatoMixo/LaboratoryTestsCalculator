from tkinter import *

def add_headland(root, array):
    array.append(Headland(root))

class Headland:

    def __init__(self, root):
        self.vars = {
            "Title" : "",
            "Paragraphs" : [],
        }

        self.objs = {
            "Title" : Entry(root, textvariable=self.vars["Title"]),
            "Paragraphs" : []
        }
    
    def add_paragraph(self, root):
        self.vars["Paragraphs"].append("")
        self.objs["Paragraphs"].append(Entry(root, textvariable=self.vars["Paragraphs"][len(self.vars["Paragraphs"]) - 1]))
    
    def show(self):
        self.objs["Title"].grid()
        for paragraph in self.objs["Paragraphs"]:
            paragraph.grid()