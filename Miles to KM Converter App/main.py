from tkinter import *

def miles_to_km():
    new_miles = float(miles_input.get())
    km = new_miles * 1.609
    km_result.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=65, pady=10)

miles_input = Entry(width=7)
miles_input.grid(column=2, row=0)

my_labelmiles = Label(text="Miles")
my_labelmiles.grid(column=3, row=0)

my_labelkm = Label(text="KM")
my_labelkm.grid(column=3, row=1)

my_labelkm = Label(text="is equal to")
my_labelkm.grid(column=0, row=1)

km_result = Label(text="0")
km_result .grid(column=2, row=1)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)


window.mainloop()