import tkinter as tk
import guisetstatic
import guihex1name
import os
import colorsys

# Code to add widgets will go here...
#tk.mainloop()


def main():
	tz = tk.Tk()
	tz.wm_title("Meme Menu")
	tz.minsize(350, 100)
	a = tk.Button(tz, text="setip",font=('courier', '20') ,command=guisetstatic.main)
	b = tk.Button(tz, text="name minecraft",font=('courier', '20') ,command=guihex1name.main)
	t1 = tk.Label(tz, text="-Noah and Preston",font=('courier', '10'))
	a.pack()
	b.pack()
	t1.pack()
	tz.mainloop()
if __name__ == "__main__":
    main()
