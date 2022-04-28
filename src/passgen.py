import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.iconbitmap('./assets/icon.ico')
    root.title("Passgen - Complex Password Generator")
    root.geometry("500x400")

    lbl_password = tk.Label()
    lbl_password.config(text='s897wre987gw897v9d8fb')
    lbl_password.grid()

    root.mainloop()
