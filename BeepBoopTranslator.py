import Tkinter as tk

class mainWindows(tk.Frame):
    def __init__(self, master):
        self.m = master
        tk.Frame.__init__(self, master)
        self.grid()
		self.createWidgets()


if __name__=='__main__':
    root = Tk()

    w, h = 800, 501
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()

    #setting up tkinter environment
    root.title('Beep Boop Translation')
    root.geometry('%dx%d+%d+%d' % (w, h, ((sw - w)/2), ((sh - h)/2)))
    root.resizable(0,0)
    root.configure(background='Grey')
    #root.iconbitmap(r'translate.ico')
    root.focus_set()

    window = mainWindows(root)

    root.mainloop()


