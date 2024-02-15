import tkinter as tk

# Resizes the map grid with the input values from the entries
def resize_grid():
    global xSize, ySize
    xSize = entryXSize.get()
    ySize = entryYSize.get()
    print("Size saved: ", xSize, ySize)

# Create main window
root = tk.Tk()
root.title("Idle Shrooms Map-Maker")

# Create the Frame containing the input parameters
inputFrame = tk.Frame(root)
inputFrame.grid()

# Initialize variables
xSize = 3
ySize = 3

# Create input boxes
entryXSize = tk.Entry(inputFrame)
entryXSize.grid(column=1, row=0)

entryYSize = tk.Entry(inputFrame)
entryYSize.grid(column=1, row=1)

# Create labels for input boxes
labelXSize = tk.Label(inputFrame, text="GridX:")
labelXSize.grid(column=0, row=0)

labelYSize = tk.Label(inputFrame, text="GridY:")
labelYSize.grid(column=0, row=1)

# Create the buttons
buttonResizeGrid = tk.Button(inputFrame, text="Resize Grid", command=resize_grid)
buttonResizeGrid.grid(column=1, row=3)

root.mainloop()