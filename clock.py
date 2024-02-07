import time
from tkinter import Tk, Label, Button

root = None
time_label = None

#==============================================================================
def update_time():
    global root, time_label

    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=f"{current_time}")
    # Update again after 1 second
    root.after(1000, update_time)

#==============================================================================
def main():
    global root, time_label

    root = Tk()
    root.title("Clock")  # Update title of the window
    root.config(bg="black") # Update background color of the window
    # Set window size
    root.geometry("310x90")
    # Make the window topmost
    root.wm_attributes("-topmost", 1)

    #time_label = Label(root, text="--:--:--", font=("Courier", 80))
    time_label = Label(
        root,
        text="23:56:58",
        font=("Futura", 40),
        bg="#0d0208",
        fg="#008f11", # Matrix colors:  #0d0208, #003b00, #008f11, #00ff41
    )

    time_label.pack()
    #time_label.pack(fill="both", expand=True)
    #time_label.place(anchor="center", relx=0.5, rely=0.5)

    # Get dimensions of the time_label and set the window size accordingly
    time_label.update()
    width = time_label.winfo_width()
    height = time_label.winfo_height()
    print(f"width: {width}, height: {height}")
    root.geometry(f"{width}x{height}")

    # Start initial update
    update_time()

    #quit_button = Button(root, text="Quit", command=root.quit)
    #quit_button.pack()

    root.mainloop()

#==============================================================================
if __name__ == "__main__":
    main()
  
