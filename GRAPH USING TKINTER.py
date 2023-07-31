import tkinter as tk
import random

def create_population_graph():
    cities = ['City1', 'City2', 'City3', 'City4', 'City5', 'City6', 'City7', 'City8', 'City9', 'City10']
    population = [random.randint(100000, 5000000) for _ in range(10)]  # Random population data for 10 cities

    root = tk.Tk()  
    root.title("Population Graph")
    root.geometry("600x500")

    canvas = tk.Canvas(root, width=500, height=300, bg="white")
    canvas.pack()

    # X-axis
    canvas.create_line(100, 300, 500, 300, arrow=tk.LAST)  # X-axis line
    for i in range(10):
        x = 100 + i * 40
        canvas.create_text(x, 310, text=cities[i], anchor=tk.N)  # City names
        canvas.create_line(x, 300, x, 290, width=2)  # Ticks on the X-axis

    # Y-axis
    canvas.create_line(50, 300, 50, 50, arrow=tk.LAST)  # Y-axis line
    for i in range(6):
        y = 300 - i * 50
        canvas.create_text(40, y, text=str(1000000 * i), anchor=tk.E)  # Population labels
        canvas.create_line(50, y, 60, y, width=2)  # Ticks on the Y-axis

    # Population bars
    for i in range(10):
        x = 100 + i * 40
        y = 300 - population[i] // 20000
        canvas.create_rectangle(x - 10, y, x + 10, 300, fill="blue")  # Blue bars representing population

    root.mainloop()

if __name__ == "__main__":
    create_population_graph()


