from tkinter import Tk, Canvas


def find_points(w1, w2, threshold):
    x1 = -threshold / -w1
    x1 *= 300
    x1 += 100
    point1 = (x1, 420)

    x2 = -threshold / -w2
    x2 *= 245
    x2 = 500 - (x2 + 80)
    point2 = (100, x2)

    return point1, point2


def show_line(w1, w2, threshold):
    window = Tk()
    window.title('Cartesian Plane')
    window.resizable(False, False)

    plane = Canvas(window, width=800, height=500, bg='#ebf2ea')
    # Drawing
    plane.create_line(100, 0, 100, 800, fill='#50adea')  # y-axis
    plane.create_line(0, 420, 800, 420, fill='#50adea')  # x-axis

    plane.create_text(85, 436, anchor='w', font='Purisa', text='0')  # Origin point
    plane.create_text(85, 175, anchor='w', font='Purisa', text='1-')  # on the y-axis
    plane.create_text(380, 175, anchor='w', font='Purisa', text='1')  # on y = x axis
    plane.create_text(390, 440, anchor='w', font='Purisa', text='1')  # on the x-axis

    plane.create_oval(95, 414, 105, 430, fill='#0abda0')  # Origin point
    plane.create_oval(95, 170, 105, 186, fill='#0abda0')  # On the y-axis
    plane.create_oval(390, 414, 400, 430, fill='#0abda0')  # On the x-axis
    plane.create_oval(390, 170, 400, 186, fill='#0abda0')  # On the y = x axis

    point1, point2 = find_points(w1, w2, threshold)

    # plane.create_text(point2[0], point2[1], anchor='w', text='Test1-Y')
    # plane.create_text(point1[0], point1[1], anchor='w', text='Test1-X')
    plane.create_line(point2[0], point2[1], point1[0], point1[1])

    # plane.create_line(50, 175, 50, 420)
    # plane.create_line(100, 440, 400, 440)

    # plane.create_text(100, 261, anchor='w', text='Test1-Y')
    # plane.create_text(297, 420, anchor='w', text='Test1-X')
    # plane.create_line(100, 261, 297, 420)
    #
    # plane.create_text(100, 28, anchor='w', text='Test2-Y')
    # plane.create_text(467, 420, anchor='w', text='Test2-X')
    # plane.create_line(100, 28, 467, 420)

    plane.pack()

    window.mainloop()
