from tkinter import filedialog as fd

def browseFiles():
	filename = fd.askopenfilename(initialdir = "/", title = "Select a File",
        filetypes = (("JPG Files", "*.JPG*"), ("All files","*.*")))

	return filename