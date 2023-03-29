import tkinter
from tkinter import messagebox

class Converter:

    def window(self):
        self.screen = tkinter.Tk()
        self.screen.geometry("300x250")
        self.screen.config(padx = 50, pady = 25)
        self.screen.title("distance converter".title())

    def get_distance(self):
        self.dis = tkinter.Entry()
        self.dis.insert(0, "Enter the distance")
        self.dis.pack()

    def convert(self):
        self.click = tkinter.Button(text = "Convert")
        self.click.pack(side = "bottom",pady = 15)

    def result(self):
        self.equal_to = tkinter.Label()
        self.equal_to.pack(side = "bottom")

    def pick(self):
        self.com = tkinter.IntVar()
        self.m = tkinter.Radiobutton(self.screen,variable = self.com, text = "To miles", value = 1)
        self.km = tkinter.Radiobutton(self.screen,variable = self.com, text = "To kilometers", value = 2)
        self.km.place(x = 25,y = 75)
        self.m.place(x = 25,y = 50)
        self.con = str

    def empty_msg(self):
        messagebox.showerror("Error", "You should enter a number")

    def empty_radio(self):
        messagebox.showerror("Error", "You should choose an option")

