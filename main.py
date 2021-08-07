from tkinter import Tk, Label, PhotoImage, Frame, Entry, Button
from tkinter import ttk
from PIL import ImageTk, Image
from canvas import show_line
import tkinter as tk
import normal_gates as ng
import math


title_font = ('Comic Sans MS', 30)
my_font1 = ('Comic Sans MS', 13)
my_font2 = ('Comic Sans MS', 10)

selected = 0
gates_dict = {0: 'AND', 1: 'NAND', 2: 'OR', 3: 'NOR', 4: 'XOR', 5: 'XNOR'}

W1 = 0.0
W2 = 0.0
THRESHOLD = 0.0
CALCULATED_VALUE = math.inf


def testing(x1, x2, func, result):
    global W1, W2, THRESHOLD, CALCULATED_VALUE
    CALCULATED_VALUE = ng.calculate(W1, int(x1.get()), W2, int(x2.get()), THRESHOLD, func.get())
    result.config(text=str(CALCULATED_VALUE))


def start_learning(epochs, alpha, func):
    w1, w2, threshold = 0.0, 0.0, 0.0
    if gates_dict[selected] == 'AND':
        w1, w2, threshold = ng.learn([(0, 0), (0, 1), (1, 0), (1, 1)], [0, 0, 0, 1], epochs, alpha, func)
    elif gates_dict[selected] == 'NAND':
        w1, w2, threshold = ng.learn([(0, 0), (0, 1), (1, 0), (1, 1)], [1, 1, 1, 0], epochs, alpha, func)
    elif gates_dict[selected] == 'OR':
        w1, w2, threshold = ng.learn([(0, 0), (0, 1), (1, 0), (1, 1)], [0, 1, 1, 1], epochs, alpha, func)
    elif gates_dict[selected] == 'NOR':
        w1, w2, threshold = ng.learn([(0, 0), (0, 1), (1, 0), (1, 1)], [1, 0, 0, 0], epochs, alpha, func)
    print(w1, w2, threshold)
    global W1, W2, THRESHOLD
    W1 = w1
    W2 = w2
    THRESHOLD = threshold
    show_line(w1, w2, threshold)


def get_inputs(ep, lr, combo):
    epochs = int(ep.get())
    learning_rate = float(lr.get())
    activation_function = combo.get()
    if 0 < learning_rate <= 1:
        start_learning(epochs, learning_rate, activation_function)
    else:
        return


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


def run():
    # Define main window
    root_window = Tk()
    root_window.title('Logic_Gates_NN')
    root_window.call('wm', 'iconphoto', root_window.w, PhotoImage(file='Images/icon.png'))
    root_window.resizable(False, False)

    # Instructions
    main_label = Label(bg='#d4dca9')

    title = Label(main_label, padx=185, pady=10, text='Logical Gates NN', fg='#595775', bg='#ebf2ea', font=title_font)
    title.pack(pady=(20, 0), padx=40)

    Label(main_label, text='Choose from these gates to learn', fg='#bf9d7a', font=my_font1, padx=211).pack()

    gates = Label(main_label, width=50, height=3, padx=20, pady=5, bg='#ebf2ea')
    # Images
    frames = list()
    for i in range(6):
        frame = Frame(gates, width=12, height=8, bg='black', cursor='hand2')
        frame.grid(column=i, row=0, padx=5, pady=4)
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
    outer_fence = Frame(controls, width=40, height=40, pady=2)

    # Inputs for learning
    fence = Frame(outer_fence, padx=3, pady=2)

    Label(fence, text='Settings and configurations', font=my_font1, fg='#bf9d7a').pack()

    inputs = Frame(fence, padx=3, pady=2)

    Label(inputs, text='# of epochs:', font=my_font2).grid(column=0, row=0)
    ep = Entry(inputs, fg='black', width=15)
    ep.grid(column=1, row=0)

    Label(inputs, text='Learning Rate:', font=my_font2).grid(column=0, row=1)
    lr = Entry(inputs, fg='black', width=15)
    lr.grid(column=1, row=1)

    Label(inputs, text='Activation function(Output):', font=my_font2).grid(column=0, row=2)
    combo_output = ttk.Combobox(inputs, width=12, textvariable=tk.StringVar(), state='readonly')
    combo_output['values'] = ('tanh', 'sigmoid', 'ReLU', 'step', 'linear')
    combo_output.current(1)
    combo_output.grid(column=1, row=2)

    Label(inputs, text='Activation function(Hidden):', font=my_font2).grid(column=0, row=3)
    combo_hidden = ttk.Combobox(inputs, width=12, textvariable=tk.StringVar(), state='readonly')
    combo_hidden['values'] = ('tanh', 'sigmoid', 'ReLU', 'step', 'linear')
    combo_hidden.current(1)
    combo_hidden.grid(column=1, row=3)

    Button(inputs, text='Learn', font=my_font2, padx=22, cursor='hand2', bg='#0abda0',
           command=lambda: get_inputs(ep, lr, combo_output)).grid(column=1, row=4, pady=5)

    inputs.pack()
    fence.grid(column=0, row=0)

    # Inputs for testing
    testing_area = Frame(outer_fence, padx=40, pady=5)
    Label(testing_area, text='Enter inputs for testing', font=my_font1, fg='#bf9d7a').pack(pady=(10, 2))

    testing_input = Frame(testing_area, padx=5, pady=5)
    Label(testing_input, text='X1 = ', font=my_font2).grid(column=0, row=0)
    x1 = Entry(testing_input, fg='black', width=15)
    x1.grid(column=1, row=0)

    Label(testing_input, text='X2 = ', font=my_font2).grid(column=0, row=1)
    x2 = Entry(testing_input, fg='black', width=15)
    x2.grid(column=1, row=1)

    Label(testing_input, text='Result = ', font=my_font2).grid(column=0, row=2)
    result = Label(testing_input, fg='black', width=13, borderwidth=1, relief='solid')
    result.grid(column=1, row=2)
    Button(testing_input, text='Test', font=my_font2, padx=30, cursor='hand2', bg='#0abda0',
           command=lambda: testing(x1, x2, combo_output, result)).grid(column=1, row=3, pady=5)

    testing_input.pack()

    testing_area.grid(column=1, row=0, padx=(20, 0))

    outer_fence.pack(padx=52, pady=20)
    controls.pack(pady=(0, 25), padx=50)

    main_label.grid(column=1, row=0, sticky='N')

    root_window.mainloop()


if __name__ == '__main__':
    run()
