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


def show_line(weights, thresholds):
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

    # Put points on the plane
    plane.create_oval(95, 414, 105, 430, fill='#0abda0')  # Origin point
    plane.create_oval(95, 170, 105, 186, fill='#0abda0')  # On the y-axis
    plane.create_oval(390, 414, 400, 430, fill='#0abda0')  # On the x-axis
    plane.create_oval(390, 170, 400, 186, fill='#0abda0')  # On the y = x axis

    for loop in range(int(len(weights) / 2)):
        point1, point2 = find_points(weights[2 * loop], weights[2 * loop + 1], thresholds[loop])
        plane.create_line(point2[0], point2[1], point1[0], point1[1])

    plane.pack()

    window.mainloop()
