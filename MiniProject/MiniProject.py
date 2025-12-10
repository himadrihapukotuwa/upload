import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("360x640")  
app.title("Calculator")

#=== Display Section ===
entry_frame = ctk.CTkFrame(app, fg_color="#040111", corner_radius=10)
entry_frame.pack(padx=15, pady=20, fill="x")

input_var = ctk.StringVar()
output_var = ctk.StringVar()

input_label = ctk.CTkLabel(entry_frame, textvariable=input_var,
                           font=("Segoe UI", 24), anchor="e",
                           text_color="#ffffff", height=50)
input_label.pack(fill="x", padx=12, pady=(12, 4))

output_label = ctk.CTkLabel(entry_frame, textvariable=output_var,
                            font=("Segoe UI", 24, "bold"), anchor="e",
                            text_color="#ffffff", height=60)
output_label.pack(fill="x", padx=12, pady=(0, 12))

def press(key):
    if key == "=":
        try:
            expression = input_var.get().replace("^", "**")
            expression = expression.replace("%", "/100")
            result = eval(expression)
            output_var.set(str(round(result, 6)))
        except ZeroDivisionError:
            output_var.set("Div by 0")
        except:
            output_var.set("Error")

    elif key == "c":
        input_var.set("")
        output_var.set("")

    elif key == "⌫":
        input_var.set(input_var.get()[:-1])

    elif key == "√":
        try:
            value = float(input_var.get())
            output_var.set(str(round(math.sqrt(value), 6)))
        except:
            output_var.set("Error")

    elif key == "Log":
        try:
            value = float(input_var.get())
            output_var.set(str(round(math.log10(value), 6)))
        except:
            output_var.set("Error")

    else:
        input_var.set(input_var.get() + key)

#=== Buttons ===
btn_frame = ctk.CTkFrame(app, fg_color="#040111", corner_radius=8)
btn_frame.pack(padx=10, pady=0, fill="both", expand=True)

buttons = [
    ["c", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="]
]

def create_button(txt, row, col):
    color = "#FF9500" if txt == "=" else "#2e2e2e"
    if txt in ["+", "-", "*", "/", "%", "⌫", "c"]:
        color = "#1E1E1E" 
    elif txt == "=":
        color = "#FF9500" 
    else:
        color = "#2e2e2e"


    button = ctk.CTkButton(
        btn_frame, text=txt, corner_radius=100,
        fg_color=color,
        hover_color="#555555",
        font=("Segoe UI", 20, "bold"),
        text_color="#ffffff",
        command=lambda: press(txt)
    )
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for r, row_vals in enumerate(buttons):
    for c, char in enumerate(row_vals):
        create_button(char, r, c)

for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):
    btn_frame.columnconfigure(j, weight=1)

app.mainloop()
