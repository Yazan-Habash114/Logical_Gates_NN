from tkinter import Tk, Canvas


def show():
    window = Tk()
    window.title('Cartesian Plane')

    plane = Canvas(window, width=800, height=500, bg='#ebf2ea')
    # Drawing
    plane.create_line(30, 0, 30, 800, fill='#50adea')
    plane.create_line(0, 470, 800, 470, fill='#50adea')

    plane.create_text(15, 480, anchor='w', font='Purisa', text='0')
    plane.create_text(15, 125, anchor='w', font='Purisa', text='1-')
    plane.create_text(400, 125, anchor='w', font='Purisa', text='1')
    plane.create_text(400, 480, anchor='w', font='Purisa', text='1')

    plane.create_oval(25, 464, 35, 480, fill='#0abda0')
    plane.create_oval(25, 120, 35, 136, fill='#0abda0')
    plane.create_oval(410, 464, 420, 480, fill='#0abda0')
    plane.create_oval(410, 120, 420, 136, fill='#0abda0')
    plane.pack()

    window.mainloop()


show()
