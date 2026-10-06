import tkinter as tk

window = tk.Tk()
window.title("My House")
window.geometry("600x500")

canvas = tk.Canvas(window, width=600, height=500, bg="skyblue")
canvas.pack()

# Ground
canvas.create_rectangle(0, 400, 600, 500, fill="green")

# House
canvas.create_rectangle(180, 250, 420, 400, fill="lightyellow")

# Roof
canvas.create_polygon(150, 250, 300, 120, 450, 250,
                      fill="darkred", outline="black")

# Door
canvas.create_rectangle(270, 320, 330, 400, fill="brown")
canvas.create_oval(315, 355, 322, 362, fill="black")

# Left window
canvas.create_rectangle(210, 280, 260, 330, fill="lightblue")
canvas.create_line(235, 280, 235, 330, fill="black")
canvas.create_line(210, 305, 260, 305, fill="black")

# Right window
canvas.create_rectangle(340, 280, 390, 330, fill="lightblue")
canvas.create_line(365, 280, 365, 330, fill="black")
canvas.create_line(340, 305, 390, 305, fill="black")

# Sun
canvas.create_oval(480, 50, 540, 110, fill="yellow")

# Tree trunk
canvas.create_rectangle(80, 300, 110, 400, fill="brown")

# Tree leaves
canvas.create_oval(40, 240, 130, 330, fill="darkgreen")
canvas.create_oval(70, 210, 160, 310, fill="green")
canvas.create_oval(100, 250, 180, 330, fill="darkgreen")

# Flower 1
canvas.create_line(150, 400, 150, 350, fill="darkgreen", width=3)
canvas.create_oval(140, 340, 150, 350, fill="pink")
canvas.create_oval(150, 340, 160, 350, fill="pink")
canvas.create_oval(145, 335, 155, 345, fill="pink")
canvas.create_oval(145, 345, 155, 355, fill="pink")
canvas.create_oval(148, 342, 153, 347, fill="yellow")

# Flower 2
canvas.create_line(450, 400, 450, 350, fill="darkgreen", width=3)
canvas.create_oval(440, 340, 450, 350, fill="purple")
canvas.create_oval(450, 340, 460, 350, fill="purple")
canvas.create_oval(445, 335, 455, 345, fill="purple")
canvas.create_oval(445, 345, 455, 355, fill="purple")
canvas.create_oval(448, 342, 453, 347, fill="yellow")
canvas.create_text(300, 440, text="My House", font=("Arial", 18, "bold"), fill="black")
# Cloud
canvas.create_oval(100, 80, 160, 120, fill="white", outline="white")
canvas.create_oval(140, 60, 210, 120, fill="white", outline="white")
canvas.create_oval(190, 80, 250, 120, fill="white", outline="white")
canvas.create_rectangle(120, 90, 230, 120, fill="white", outline="white")
window.mainloop()