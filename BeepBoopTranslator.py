from tkinter import *

class mainWindows:
    def __init__(self, master):
        self.m = master
        Frame.__init__(self, master)
        self.topFrame = Frame(self.m)
        self.middleFrame = Frame(self.m)
        self.midLeftFrame = Frame(self.m)
        self.bottomFrame = Frame(self.m)
        self.topFrame.pack(Side=TOP)
        self.middleFrame.pack()
        self.midLeftFrame.pack(Side=LEFT)
        self.bottomFrame.pack(Side=BOTTOM)


if __name__=='__main__':
    root = Tk()

    w, h = 800, 500
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


