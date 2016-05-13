from tkinter import *

class mainWindows:
    def __init__(self, w):
        self.w = w

if __name__=='__main__':
    root = Tk()

    w, h = 800, 500
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()

    #setting up tkinter environment
    root.title('Beep Boop Translation')
    root.geometry('%dx%d+%d+%d' % (w, h, ((sw - w)/2), ((sh - h)/2)))
    root.resizable(0,0)
    root.configure(background='Red')
    #root.iconbitmap(r'translate.ico')
    root.focus_set()

    window = mainWindows(root)

    root.mainloop()


