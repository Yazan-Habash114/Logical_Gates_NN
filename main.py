from tkinter import *


title_font = ('Comic Sans MS', 23)


def run():
    # Define main window
    root_window = Tk()
    root_window.title('Logic_Gates_NN')
    root_window.call('wm', 'iconphoto', root_window._w, PhotoImage(file='Images/icon.png'))
    root_window.resizable(False, False)

    # Instructions
    canvas = Canvas(root_window)
    canvas.grid(columnspan=3)  # Put the canvas to centralize the contents

    main_label = Label(bg='#bf988f')

    title = Label(main_label, text='Logical Gates NN', fg='#595775', font=title_font)
    title.pack(pady=10, padx=270)

    gates = Label(main_label, width=50, height=3)
    # Put images here
    gates.pack()

    controls = Label(main_label, width=50, height=3)
    controls.pack(pady=10)

    main_label.grid(column=1, row=0, sticky='N')

    root_window.mainloop()


if __name__ == '__main__':
    run()
