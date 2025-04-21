import tkinter
from tkinter import messagebox
from fetch_threading import run_with_threading
from fetch_asyncio import run_with_asyncio

window = tkinter.Tk()
window.title("FetchFlow")
window.resizable(False, False)
window.attributes("-alpha", 0.95)
window.update_idletasks()
window.config(bg="cornsilk2")

width = 600
height = 600
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

method_var = tkinter.StringVar(value="threading")

placeholder_text = "Enter your URL"

def click_button():
    url = url_entry.get("1.0", tkinter.END).strip()
    selected_method = method_var.get()

    if not url or url == placeholder_text:
        messagebox.showwarning("Input Error", "Please enter a URL before starting.")
        return

    status_label.config(text="Fetching...")

    if selected_method == "threading":
        run_with_threading(url, output_box, status_label)
    elif selected_method == "asyncio":
        run_with_asyncio(url, output_box, status_label)

def on_focus_in(event):
    if url_entry.get("1.0", "end-1c") == placeholder_text:
        url_entry.delete("1.0", tkinter.END)
        url_entry.config(fg="black")

def on_focus_out(event):
    if url_entry.get("1.0", "end-1c").strip() == "":
        url_entry.insert("1.0", placeholder_text)
        url_entry.config(fg="gray")

# UI Elements
big_label = tkinter.Label(text="Please enter your URL", font=("montserrat", 15, "bold"), bg="cornsilk2")
big_label.pack(pady=20)

url_entry = tkinter.Text(font=("montserrat", 12), padx=5, wrap="word", width=60, height=5)
url_entry.insert("1.0", placeholder_text)
url_entry.config(fg="gray")
url_entry.bind("<FocusIn>", on_focus_in)
url_entry.bind("<FocusOut>", on_focus_out)
url_entry.pack(pady=10)

tkinter.Radiobutton(window, text="Threading", variable=method_var, value="threading", bg="cornsilk2", font=("montserrat", 12)).pack(anchor="n", pady=5)
tkinter.Radiobutton(window, text="AsyncIO", variable=method_var, value="asyncio", bg="cornsilk2", font=("montserrat", 12)).pack(anchor="n", pady=5)

status_label = tkinter.Label(text="Ready", font=("montserrat", 12), bg="cornsilk2")
status_label.pack()

output_box = tkinter.Text(font=("montserrat", 11), bg="white", wrap="word", height=10, width=70, state="disabled")
output_box.pack(pady=10)

start_button = tkinter.Button(text="Fetch", font=("montserrat", 11, "bold"), bg="#4CAF50", fg="white", width=20, command=click_button)
start_button.pack(pady=20, side=tkinter.BOTTOM)

window.mainloop()
