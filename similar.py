import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
from tkinter import ttk
from tkinterweb import HtmlFrame

def check_website():
    website_url = website_entry.get()
    search_texts = [text_entry1.get(), text_entry2.get(), text_entry3.get(), text_entry4.get(), text_entry5.get()]

    try:
        website_content = requests.get(website_url).content
        soup = BeautifulSoup(website_content, 'html.parser')
        found_results = []

        for i, search_text in enumerate(search_texts):
            if search_text.lower() in soup.text.lower():
                found_results.append(f"Text {i+1}: '{search_text}' is present on {website_url}'.")
                if highlight_var.get():
                    highlighted_text = soup.prettify().replace(search_text, f"<span style='background-color: yellow;'>{search_text}</span>")
                    soup = BeautifulSoup(highlighted_text, 'html.parser')

        if found_results:
            messagebox.showinfo("Website Check", "\n".join(found_results))
            if preview_var.get():
                display_website_preview(website_url)

        else:
            messagebox.showinfo("Website Check", "No text was found on the website.")
    except:
        messagebox.showerror("Error", "An error occurred while checking the website.")

def display_website_preview(website_url):
    preview_window = tk.Toplevel(window)
    preview_window.title("Website Preview")
    preview_window.geometry("800x600")

    frame = HtmlFrame(preview_window)
    frame.pack(fill="both", expand=True)
    frame.set_content(website_url)

# Create the main window
window = tk.Tk()
window.title("Website Checker")
window.geometry("500x350")

# Widgets
label = ttk.Label(window, text="Enter the website URL:")
label.pack(pady=10)

website_entry = ttk.Entry(window)
website_entry.pack()

text_label = ttk.Label(window, text="Enter the texts to search:")
text_label.pack(pady=10)

text_entry1 = ttk.Entry(window)
text_entry1.pack()

text_entry2 = ttk.Entry(window)
text_entry2.pack()

text_entry3 = ttk.Entry(window)
text_entry3.pack()

text_entry4 = ttk.Entry(window)
text_entry4.pack()

text_entry5 = ttk.Entry(window)
text_entry5.pack()

highlight_var = tk.IntVar()
highlight_check = ttk.Checkbutton(window, text="Highlight found text", variable=highlight_var)
highlight_check.pack(pady=10)

preview_var = tk.IntVar()
preview_check = ttk.Checkbutton(window, text="Show website preview", variable=preview_var)
preview_check.pack(pady=10)

check_button = ttk.Button(window, text="Check Website", command=check_website)
check_button.pack(pady=20)

# Run the main loop
window.mainloop()
