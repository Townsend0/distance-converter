from data import *

a = Converter()
a.window()
a.get_distance()
a.pick()
a.result()
a.convert()
def del_entry(event):
    a.dis.delete(0, "end")

def selected():
    b = a.com.get()
    if b == 2:
        a.con = 1.609344
    elif b == 1:
        a.con = 1/1.609344

def find_rslt():
    try:
        a.equal_to.config(text = round(float(a.dis.get()) * a.con, 2))
        a.dis.delete(0, "end")
    except ValueError:
        a.empty_msg()
    except TypeError:
        a.empty_radio()

a.km.config(command = selected)
a.m.config(command = selected)
a.click.config(command = find_rslt)
a.dis.bind("<FocusIn>", del_entry)

a.screen.mainloop()