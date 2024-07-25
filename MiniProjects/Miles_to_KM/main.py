import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="Best label", font=("Arial", 24, "italic"))
label.pack(side="top")


class Car:
    def __init__(self,   **kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
    def print(self):
        print(f"Your car {self.make} is a {self.model} model")

my_car=Car(make="VW", model="passat")

print(my_car.print())

window.mainloop()
