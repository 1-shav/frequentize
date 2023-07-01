import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from fns import Pixela
import cairosvg
import io
import os
import matplotlib.pyplot as plt

#------------------------------------CONSTANTS------------------------------------------#
bg_blue = "#171c28"
bright_red = "#ff4646"
bright_green = "#01df72"
whitish = "#e0dfe1"

#------------------------------------Pixela-related-------------------------------------#
pixela = Pixela()

graph_stats = pixela.graph_get_stats()


def plot_line_graph_jpg():
    plt.figure(figsize=(8,1), facecolor=bg_blue)

    ax = plt.axes()
    ax.set_facecolor(bg_blue)
    ax.axis('off')

    points = open(f'{pixela.graph_id}_line.svg', 'r').readlines()[12][1:-2]

    points = [tuple(map(float, point.split())) for point in points.split(',')]

    plt.plot(*zip(*points), color=whitish)

    plt.savefig(f"{pixela.graph_id}_line.jpg")
    print("line graph [jpg] saved!")

pixela.graph_get_svg(True)
pixela.graph_get_svg(False)
plot_line_graph_jpg()

#------------------------------------GUI-related----------------------------------------#
root = tk.Tk()
root.title("frequentize.phi")
root.geometry("800x600+550+200")
root.resizable(False, False)
root.configure(bg=bg_blue)


frequentize_label = tk.Label(root, text="frequentize", background=bg_blue, foreground=whitish, font=("Brass Mono", 21))
frequentize_label.grid(row=0, column=2, padx = 10, pady = 10, sticky="W")


blank_label = tk.Label(root, text=" ", background=bg_blue, foreground=whitish, font=("Brass Mono", 21))
blank_label.grid(row=1, column=0)


grid_label = tk.Label(root, text=pixela.graph_name, background=bg_blue, foreground=whitish, font=("Brass Mono", 21))
grid_label.grid(row=1, column=1, sticky="W")


grid_canvas = tk.Canvas(root, width=750, height=122, background=bg_blue, highlightcolor=whitish)
image_data = cairosvg.svg2png(url=f"{pixela.graph_id}.svg")
pixela_grid = Image.open(io.BytesIO(image_data))
resized_grid = pixela_grid.resize((820, 164))
grid = ImageTk.PhotoImage(resized_grid)
grid_canvas.create_image(390, 66, image=grid)
grid_canvas.grid(row=2, column=1, columnspan=4, pady=10)    


line_graph_canvas = tk.Canvas(root, width=750, height=122, background=bg_blue, highlightthickness=0)
line_graph_image = Image.open(f"{pixela.graph_id}_line.jpg")
resized_line_graph = line_graph_image.resize((1035, 122))
line_graph_photo = ImageTk.PhotoImage(resized_line_graph)
line_graph_canvas.create_image(365, 61, image=line_graph_photo)
line_graph_canvas.grid(row=3, column=1, columnspan=4)


stats_label = tk.Label(root, text=f"Max :: {graph_stats['maxQuantity']}\tMin :: {graph_stats['minQuantity']}\tTotal :: {graph_stats['totalQuantity']}\nAvg :: {graph_stats['avgQuantity']}\tToday  :: {graph_stats['todaysQuantity']}\tPixels :: {graph_stats['totalPixelsCount']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 17))
stats_label.grid(row=4, column=1, columnspan=4, pady = 10)


root.mainloop()