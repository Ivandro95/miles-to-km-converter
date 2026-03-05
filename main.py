from tkinter import *


def converter():
    miles_data = float(first_entry.get())
    km_data = round(miles_data * 1.609)
    km_label_result.config(text=f"{km_data}")

#window
window = Tk()
#window.minsize(width=500,height=300)
window.config(padx=20, pady=20)
window.title("Miles to KM converter")

#labels
is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=0,row=1)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

km = Label(text="KM")
km.grid(column=2, row=1)

km_label_result = Label(text="0")
km_label_result.grid(column=1,row=1)

#entries
first_entry = Entry()
first_entry.grid(column=1,row=0)

#button
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)



window.mainloop()