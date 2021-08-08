from tkinter import Tk, Canvas


def find_points(w1, w2, threshold):
    # Part of line
    # x1 = -threshold / -w1
    # x1 *= 300  # Length of the segment between (0, 0) and (1, 0) = 800 - 100 - 390 = 300
    # x1 += 100  # Margin = 100 from left of y-axis
    # point1 = (x1, 420)
    #
    # x2 = -threshold / -w2
    # x2 *= 245    # Length of segment (0, 0) and (0, 1) = 500 - 80 - 175 = 245
    # x2 = 500 - (x2 + 80)
    # point2 = (100, x2)

    # Full Line
    y = (-0.33 * -w1 + threshold) / w2
    y *= 245
    y = 500 - (y + 80)
    point1 = (0, y)

    y = (2.33 * -w1 + threshold) / w2
    y *= 245
    y = 500 - (y + 80)
    point2 = (800, y)

    return point1, point2


def show_line(weights, thresholds):
    window = Tk()
    window.title('Cartesian Plane')
    window.resizable(False, False)

    plane = Canvas(window, width=800, height=500, bg='#ebf2ea')
    # Drawing
    plane.create_line(100, 0, 100, 800, fill='#50adea')  # y-axis
    plane.create_line(0, 420, 800, 420, fill='#50adea')  # x-axis

    plane.create_text(85, 436, anchor='w', font='Purisa', text='(0, 0)')  # Origin point
    plane.create_text(85, 159, anchor='w', font='Purisa', text='(0, 1)')  # on the y-axis
    plane.create_text(380, 159, anchor='w', font='Purisa', text='(1, 1)')  # on y = x axis
    plane.create_text(390, 440, anchor='w', font='Purisa', text='(1, 0)')  # on the x-axis

    # Put points on the plane
    plane.create_oval(95, 414, 105, 430, fill='#0abda0')  # Origin point
    plane.create_oval(95, 170, 105, 186, fill='#0abda0')  # On the y-axis
    plane.create_oval(390, 414, 400, 430, fill='#0abda0')  # On the x-axis
    plane.create_oval(390, 170, 400, 186, fill='#0abda0')  # On the y = x axis

    for loop in range(int(len(weights) / 2)):  # Detecting 2 point for each line
        point1, point2 = find_points(weights[2 * loop], weights[2 * loop + 1], thresholds[loop])
        plane.create_line(point2[0], point2[1], point1[0], point1[1])

    plane.pack()

    window.mainloop()
