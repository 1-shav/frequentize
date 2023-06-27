import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from fns import Pixela
import cairosvg
import io
import os

# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM

# image = svg2rlg("testinf.svg")
# renderPM.drawToFile(image, "testinf.png", fmt="PNG")

#------------------------------------CONSTANTS------------------------------------------#
bg_blue = "#171c28"
bright_red = "#ff4646"
bright_green = "#01df72"
whitish = "#e0dfe1"

#------------------------------------Pixela-related-------------------------------------#
pixela = Pixela()

graph_stats = pixela.graph_get_stats()

if not os.path.isfile("testinf.svg"):
    pixela.graph_get_svg(False)
if not os.path.isfile("testinf_line.svg"):
    pixela.graph_get_svg(True)


#------------------------------------GUI-related----------------------------------------#
root = tk.Tk()
root.title("frequentize.phi")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg=bg_blue)

frequentize_label = tk.Label(root, text="frequentize", background=bg_blue, foreground=whitish, font=("Brass Mono", 21))
frequentize_label.grid(row=0, column=2, padx = 10, pady = 10)

blank_label = tk.Label(root, text=" ", background=bg_blue, foreground=whitish, font=("Brass Mono", 21))
blank_label.grid(row=1, column=0)

grid_label = tk.Label(root, text=pixela.graph_name, background=bg_blue, foreground=whitish, font=("Brass Mono", 21))
grid_label.grid(row=1, column=1, sticky="W")

grid_canvas = tk.Canvas(root, width=750, height=122, background=bg_blue, highlightcolor=whitish)
# pixela_grid = Image.open("testinf.png")
image_data = cairosvg.svg2png(url="testinf.svg")
pixela_grid = Image.open(io.BytesIO(image_data))
resized_grid = pixela_grid.resize((820, 164))
grid = ImageTk.PhotoImage(resized_grid)
grid_canvas.create_image(390, 66, image=grid)
grid_canvas.grid(row=2, column=1, columnspan=4, pady=10)

line_graph_canvas = tk.Canvas(root, width=750, height=122, background=bg_blue, highlightcolor=whitish)
image_data = cairosvg.svg2png(url="testinf_line.svg")
line_graph = Image.open(io.BytesIO(image_data))
resized_line = line_graph.resize((750, 144))
line_graph_image = ImageTk.PhotoImage(resized_line)
line_graph_canvas.create_image(366, 80, image=line_graph_image)
line_graph_canvas.grid(row=3, column=1, columnspan=4, pady=10)

# max_label = tk.Label(root, text=f"Max :: {graph_stats['maxQuantity']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 15))
# max_label.grid(row=3, column=1)

# min_label = tk.Label(root, text=f"Min  :: {graph_stats['minQuantity']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 15))
# min_label.grid(row=3, column=2)

# total_label = tk.Label(root, text=f"Total :: {graph_stats['totalQuantity']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 15))
# total_label.grid(row=3, column=3)

# avg_label = tk.Label(root, text=f"Avg :: {graph_stats['avgQuantity']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 15))
# avg_label.grid(row=4, column=1)

# today_label = tk.Label(root, text=f"Today  :: {graph_stats['todaysQuantity']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 15))
# today_label.grid(row=4, column=2)

# total_pixel_label = tk.Label(root, text=f"Pixels :: {graph_stats['totalPixelsCount']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 15))
# total_pixel_label.grid(row=4, column=3)

# style = ttk.Style()
# style.configure("TButton", font=("Brass Mono", 34), background=[("active", bright_red), ("pressed", bright_green)], foreground=)

# add_button = ttk.Button(root, text="Add Pixel", style="TButton", padding=39)
# add_button.grid(row=5, column=2, columnspan=2)

stats_label = tk.Label(root, text=f"Max :: {graph_stats['maxQuantity']}\tMin :: {graph_stats['minQuantity']}\tTotal :: {graph_stats['totalQuantity']}\nAvg :: {graph_stats['avgQuantity']}\tToday  :: {graph_stats['todaysQuantity']}\tPixels :: {graph_stats['totalPixelsCount']}", background=bg_blue, foreground=whitish, font=("Brass Mono", 17))
stats_label.grid(row=4, column=1, columnspan=4)


root.mainloop()