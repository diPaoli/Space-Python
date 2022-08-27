

def show_Score():

    # shows registered scores
    import db_func
    scores_data = db_func.select_all() 

    #import tkinter as tk
    import customtkinter as ctk

    ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    window = ctk.CTk()  # create CTk window like you do with the Tk window
    window.geometry("300x400")
    window.title('High Scores')
    window.resizable(True, True)



    r = 0
    for values in scores_data:
        frame = ctk.CTkFrame(window, corner_radius=10)
        
        ctk.CTkLabel(frame, text=values[0], width=60, anchor='e').grid(row=r, column=0)
        ctk.CTkLabel(frame, text=values[1], width=60).grid(row=r, column=1)
        ctk.CTkLabel(frame, text=values[2], width=60).grid(row=r, column=2)

        frame.pack(padx=2, pady=2, expand=False)
        r += 1


    # Botão fechar
    # def close():
    #     window.quit()
    # button = ctk.CTkButton(master=window, text="Close", command=close)
    # button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

    window.mainloop()