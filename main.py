characters_for_buttons = ["*","^","/","+","0","-",
                         "7","8","9","4","5","6",
                         "1","2","3"]
var = 0
var2= 0
def calculation(ss):
    try:
        answer = eval(entry_formula.get())
        lbl_answer["text"] = answer
    except: lbl_answer["text"] = "Error"

def clicked_button(variable):
    entry_formula.insert(tk.END, characters_for_buttons[variable])
def clear_numbers():
    entry_formula.delete(0,tk.END)


import tkinter as tk

window = tk.Tk()
window.title("Calculator")


frame_btns = tk.Frame(master=window,bg="lightyellow")
frame_btns.grid( row=0 , column=0)

#buttons being created in a loop
while var < 15:
    for i in range(3):
        btn = tk.Button(master=frame_btns,
                        text=f"{characters_for_buttons[var]}",padx=20,pady=15,
                        command=lambda var=var:clicked_button(var))
        if not characters_for_buttons[var].isdigit():
            btn.config(bg="grey15",fg="white")
        else: btn.config(bg="mistyrose")
        btn.grid(column=i,row=var2,padx=2,pady=2)
        var += 1
    var2 += 1

lbl_answer = tk.Label(master=window)
lbl_answer.grid(row=1,column=1)

btn_clear = tk.Button(master=window,text="Clear",command=clear_numbers)
btn_clear.grid(column=2,row=1)


entry_formula = tk.Entry(master=window)
entry_formula.grid(column=0, row=1)

window.bind('<Enter>', calculation)

window.mainloop()