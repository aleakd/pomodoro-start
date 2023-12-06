from tkinter import *
import math


# ---------------------------- CONSTANTES ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    ventana.after_cancel(timer)
    canvas.itemconfig(tiempo_corriendo, text="00:00")
    timer_etiqueta.config(text="Timer")
    tilde_etiqueta.config(text="")
    global reps
    reps = 0 
# ---------------------------- TIMER MECANISMO ------------------------------- #
def star_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        cuenta_regresiva(long_break)
        timer_etiqueta.config(text="descanso", fg=RED)
    elif reps % 2 == 0:
        cuenta_regresiva(short_break)
        timer_etiqueta.config(text="descanso", fg=PINK)
    else:
        cuenta_regresiva(work_sec)
        timer_etiqueta.config(text="trabajo", fg=GREEN)

# ---------------------------- CUENTA REGRESIVA MECANISMO ------------------------------- #
def cuenta_regresiva(count):

    count_min = math.floor(count / 60)
    count_seg = count % 60
    if count_seg < 10:
        count_seg = f"0{count_seg}"


    canvas.itemconfig(tiempo_corriendo, text=f"{count_min}:{count_seg}")
    if count > 0:
        global timer
        timer = ventana.after(1000, cuenta_regresiva, count - 1)
    else:
        star_timer()
        mark = ""
        work_sesion = math.floor(reps/2)
        for _ in range(work_sesion):
            mark += "✔"
        tilde_etiqueta.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
ventana = Tk()
ventana.title("Pomodoro")
ventana.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
imagen = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=imagen)
tiempo_corriendo = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



timer_etiqueta = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_etiqueta.grid(row=0, column=1)

boton_start = Button(text="Start", highlightthickness=0, command=star_timer)
boton_start.grid(row=2, column=0)

boton_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
boton_reset.grid(row=2, column=2)

tilde_etiqueta = Label(fg=GREEN)
tilde_etiqueta.grid(row=4, column=1)









ventana.mainloop()