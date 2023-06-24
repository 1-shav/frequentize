import tkinter
from tkinter import ttk


#------------------------------------CONSTANTS------------------------------------------#
bg_blue = "#171c28"
bright_red = "#ff4646"
whitish = "#e0dfe1"



#------------------------------------GUI-related----------------------------------------#
root = tkinter.Tk()
root.title("frequentize.phi")
root.geometry("800x600")
root.configure(bg=bg_blue)

frequentize_label = tkinter.Label(root, text="frequentize", background=bg_blue, foreground=whitish, font=("Brass Mono", 21))
frequentize_label.grid(row=0, column=0)








root.mainloop()