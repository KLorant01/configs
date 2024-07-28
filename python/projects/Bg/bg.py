from tkinter.filedialog import askopenfilename

filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)