import requests
from tkinter import *
import time

MY_LAT = 44.318378
MY_LNG = 23.796400
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    #print(f"ISS is at :\nLatitude{latitude}\nLongitude: {longitude}\n")
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        canvas.itemconfig(canvas_is_overhead, text="ISS IS OVER YOUR HEAD !!!!!", fill="green")
        canvas.itemconfig(canvas_iss_coords, text="")
    else:
        print(f"Another {latitude - MY_LAT} latitude and {longitude - MY_LNG}")
        canvas.itemconfig(canvas_is_overhead, text="It is not over your head yet! ", fill="black")
        canvas.itemconfig(canvas_iss_coords, text=f"Another:\n{round(latitude - MY_LAT,2)} latitude\n{round(longitude - MY_LNG,2)} longitude")
    window.after(100000, func=is_iss_overhead)

window = Tk()
window.title("ISS POSITION")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=250, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack()

canvas_is_overhead = canvas.create_text(200, 50, text="", font=(FONT_NAME, 15, "bold", "italic"))
canvas_iss_coords = canvas.create_text(200, 180, text="", font=(FONT_NAME, 15, "bold"))

is_iss_overhead()

window.mainloop()