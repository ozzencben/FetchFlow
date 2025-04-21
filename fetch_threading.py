import threading
import requests

def run_with_threading(url, output_box, status_label):
    def fetch():
        try:
            response = requests.get(url)
            content = response.text
        except Exception as e:
            content = f"Error: {e}"

        def update_gui():
            output_box.config(state="normal")
            output_box.delete("1.0", "end")
            output_box.insert("1.0", content)
            output_box.config(state="disabled")
            status_label.config(text="Done!")

        output_box.after(0, update_gui)

    threading.Thread(target=fetch).start()
