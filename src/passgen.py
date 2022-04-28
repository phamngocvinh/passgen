import tkinter as tk

if __name__ == '__main__':
    # Main window
    root = tk.Tk()
    root.iconbitmap('./assets/icon.ico')
    root.title("Passgen - Complex Password Generator")
    root.geometry("300x400")

    # Generated password
    lbl_password = tk.Label()
    lbl_password.config(text='s897wre987gw897v9d8fb')
    lbl_password.pack()

    # Header button frame
    frame_head_button = tk.Frame()
    # Reset button
    button_generate = tk.Button(master=frame_head_button)
    button_generate.config(text="Generate")
    button_generate.grid(row=0, column=0)

    # Copy button
    button_copy = tk.Button(master=frame_head_button)
    button_copy.config(text="Copy")
    button_copy.grid(row=0, column=1)
    frame_head_button.pack()

    # Option frame
    frame_option = tk.Frame()
    # Length label
    label_length = tk.Label(master=frame_option, text='Length')
    label_length.grid(row=0, column=0)

    # Length entry
    entry_length = tk.Entry(master=frame_option)
    entry_length.grid(row=0, column=1)

    # Length slider
    scale_length = tk.Scale(master=frame_option, orient='horizontal')
    scale_length.grid(row=0, column=2)

    # A-Z label
    label_upper_alphabet = tk.Label(master=frame_option, text='A-Z')
    label_upper_alphabet.grid(row=1, column=0)

    # A-Z checkbox
    checkbox_upper_alphabet = tk.Checkbutton(master=frame_option)
    checkbox_upper_alphabet.grid(row=1, column=2)

    # a-z label
    label_lower_alphabet = tk.Label(master=frame_option, text='a-z')
    label_lower_alphabet.grid(row=2, column=0)

    # a-z checkbox
    checkbox_lower_alphabet = tk.Checkbutton(master=frame_option)
    checkbox_lower_alphabet.grid(row=2, column=2)

    # 0-9 label
    label_number = tk.Label(master=frame_option, text='0-9')
    label_number.grid(row=3, column=0)

    # 0-9 checkbox
    checkbox_number = tk.Checkbutton(master=frame_option)
    checkbox_number.grid(row=3, column=2)

    # Special label
    label_special = tk.Label(master=frame_option, text='!@#$%^&*')
    label_special.grid(row=4, column=0)

    # Special checkbox
    checkbox_special = tk.Checkbutton(master=frame_option)
    checkbox_special.grid(row=4, column=2)
    frame_option.pack()

    # Limit frame
    frame_limit = tk.Frame()
    # Minimum number label
    label_min_number = tk.Label(master=frame_limit, text='Minimum Numbers')
    label_min_number.grid(row=0, column=0)

    # Minimum number entry
    entry_number = tk.Entry(master=frame_limit)
    entry_number.grid(row=0, column=2)

    # Minimum special label
    label_min_special = tk.Label(master=frame_limit, text='Minimum Special')
    label_min_special.grid(row=1, column=0)

    # Minimum special entry
    entry_special = tk.Entry(master=frame_limit)
    entry_special.grid(row=1, column=2)
    frame_limit.pack()

    # Footer frame
    frame_footer_button = tk.Frame()
    # About button
    button_about = tk.Button(master=frame_footer_button)
    button_about.config(text="About")
    button_about.grid(row=0, column=0)

    # Exit button
    button_exit = tk.Button(master=frame_footer_button)
    button_exit.config(text="Exit")
    button_exit.grid(row=0, column=1)
    frame_footer_button.pack()

    root.mainloop()
