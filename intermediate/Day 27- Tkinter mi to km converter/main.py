from tkinter import *

def action():
    miles = float(entry.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to kilometers")
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()