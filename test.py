import tkinter as tk

window = tk.Tk()

frame_1 = tk.Frame()
frame_2 = tk.Frame()

label_a = tk.Label(master=frame_1, text = 'label a')
label_a.pack()
label_b = tk.Label(master=frame_2, text = 'label b')
label_b.pack()

frame_1.pack()
frame_2.pack()

print('ugabuga')

window.mainloop()
