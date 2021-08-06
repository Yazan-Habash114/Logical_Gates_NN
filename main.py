from tkinter import Tk, Label, PhotoImage, Frame, Entry
from PIL import ImageTk, Image
import normal_gates as ng


title_font = ('Comic Sans MS', 30)
my_font1 = ('Comic Sans MS', 13)
my_font2 = ('Comic Sans MS', 10)

selected = 0
gates_dict = {0: 'AND', 1: 'NAND', 2: 'OR', 3: 'NOR', 4: 'XOR', 5: 'XNOR'}


def change_frame_colour(frames, index):
    global selected
    # Deselect old selection
    frames[selected].grid_forget()
    frames[selected].config(bd=0)
    frames[selected].grid(column=selected, row=0, padx=4, pady=4)

    # Select new selection
    selected = index
    frames[index].grid_forget()
    frames[index].config(bd=4, bg='#0abda0')
    frames[index].grid(column=index, row=0, padx=4, pady=4)
    print(gates_dict[selected])

    if gates_dict[selected] == 'AND':
        w1, w2 = ng.learn([(0, 0), (0, 1), (1, 0), (1, 1)], [0, 0, 0, 1])
        print(w1, w2)


def run():
    # Define main window
    root_window = Tk()
    root_window.title('Logic_Gates_NN')
    root_window.call('wm', 'iconphoto', root_window._w, PhotoImage(file='Images/icon.png'))
    root_window.resizable(False, False)

    # Instructions
    main_label = Label(bg='#d4dca9')

    title = Label(main_label, padx=179, pady=10, text='Logical Gates NN', fg='#595775', bg='#ebf2ea', font=title_font)
    title.pack(pady=(20, 0), padx=40)

    Label(main_label, text='Choose from these gates to learn', fg='#bf9d7a', font=my_font1, padx=205).pack()

    gates = Label(main_label, width=50, height=3, padx=5, pady=5, bg='#ebf2ea')
    # Images
    frames = list()
    for i in range(6):
        frame = Frame(gates, width=12, height=8, bg='black', cursor='hand2')
        frame.grid(column=i, row=0, padx=4, pady=4)
        frames.append(frame)

    frames[0].config(bd=4, bg='#0abda0')
    and_img = Image.open('Images/AND.png').resize((100, 100))
    and_img = ImageTk.PhotoImage(and_img)
    and_label = Label(frames[0], image=and_img)
    and_label.bind('<Button>', lambda _: change_frame_colour(frames, index=0))
    and_label.pack()

    nand_img = Image.open('Images/NAND.png').resize((100, 100))
    nand_img = ImageTk.PhotoImage(nand_img)
    nand_label = Label(frames[1], image=nand_img)
    nand_label.bind('<Button>', lambda _: change_frame_colour(frames, index=1))
    nand_label.pack()

    or_img = Image.open('Images/OR.png').resize((100, 100))
    or_img = ImageTk.PhotoImage(or_img)
    or_label = Label(frames[2], image=or_img)
    or_label.bind('<Button>', lambda _: change_frame_colour(frames, index=2))
    or_label.pack()

    nor_img = Image.open('Images/NOR.png').resize((100, 100))
    nor_img = ImageTk.PhotoImage(nor_img)
    nor_label = Label(frames[3], image=nor_img)
    nor_label.bind('<Button>', lambda _: change_frame_colour(frames, index=3))
    nor_label.pack()

    xor_img = Image.open('Images/XOR.png').resize((100, 100))
    xor_img = ImageTk.PhotoImage(xor_img)
    xor_label = Label(frames[4], image=xor_img)
    xor_label.bind('<Button>', lambda _: change_frame_colour(frames, index=4))
    xor_label.pack()

    xnor_img = Image.open('Images/XNOR.png').resize((100, 100))
    xnor_img = ImageTk.PhotoImage(xnor_img)
    xnor_label = Label(frames[5], image=xnor_img)
    xnor_label.bind('<Button>', lambda _: change_frame_colour(frames, index=5))
    xnor_label.pack()

    gates.pack()

    controls = Label(main_label)
    # Controls
    outer_fence = Frame(controls, padx=40, width=40, height=40, pady=5, borderwidth=2, relief='solid')

    Label(outer_fence, text='Other Inputs and Training Results...', borderwidth=2, relief='solid').grid(column=0, row=0)

    testing_area = Frame(outer_fence, padx=40, pady=5, borderwidth=2, relief='solid')
    Label(testing_area, text='Enter inputs for testing', font=my_font1, fg='#bf9d7a', borderwidth=2,
          relief='solid').pack(pady=(10, 2))
    testing_input = Frame(testing_area, padx=5, pady=5, borderwidth=2, relief='solid')
    Label(testing_input, text='X1 = ', font=my_font2).grid(column=0, row=0)
    x1 = Entry(testing_input, fg='#0abda0', width=15)
    x1.grid(column=1, row=0)

    Label(testing_input, text='X2 = ', font=my_font2).grid(column=0, row=1)
    x2 = Entry(testing_input, fg='#0abda0', width=15)
    x2.grid(column=1, row=1)

    Label(testing_input, text='Result = ', font=my_font2).grid(column=0, row=2)
    result = Entry(testing_input, fg='#0abda0', width=15, state='disabled')
    result.grid(column=1, row=2)
    testing_input.pack()
    testing_area.grid(column=1, row=0, padx=(20, 0))

    outer_fence.pack(padx=52, pady=20)
    controls.pack(pady=(0, 25))

    main_label.grid(column=1, row=0, sticky='N')

    root_window.mainloop()


if __name__ == '__main__':
    run()
