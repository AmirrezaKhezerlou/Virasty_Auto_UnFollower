import tkinter as tk
from tkinter import ttk, messagebox
import UnFollow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Define the font
FONT = ("iransans", 11)

# Initialize the main window
root = tk.Tk()
root.title('Virasti Auto UnFollow Pro v1')

# Create the layout
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Phone Number
ttk.Label(main_frame, text="Phone Number:").grid(column=0, row=0, sticky=tk.W)
phone_number = tk.StringVar()
ttk.Entry(main_frame, textvariable=phone_number, width=30).grid(column=1, row=0, sticky=(tk.W, tk.E))

# Password
ttk.Label(main_frame, text="Password:").grid(column=0, row=1, sticky=tk.W)
password = tk.StringVar()
ttk.Entry(main_frame, textvariable=password, width=30, show="*").grid(column=1, row=1, sticky=(tk.W, tk.E))

# Your Account UserName
ttk.Label(main_frame, text="Your Account UserName:").grid(column=0, row=2, sticky=tk.W)
username = tk.StringVar()
ttk.Entry(main_frame, textvariable=username, width=30).grid(column=1, row=2, sticky=(tk.W, tk.E))

# Max UnFollow Count
ttk.Label(main_frame, text="Max UnFollow Count:").grid(column=0, row=3, sticky=tk.W)
max_unfollow_count = tk.StringVar()
ttk.Entry(main_frame, textvariable=max_unfollow_count, width=30).grid(column=1, row=3, sticky=(tk.W, tk.E))

# Separator
separator = ttk.Separator(main_frame, orient='horizontal')
separator.grid(row=4, columnspan=2, sticky=(tk.W, tk.E), pady=10)

# Start and Close buttons
def start_session():
    if phone_number.get() and password.get() and username.get():
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        service = Service('./chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options)
        url = 'https://virasty.com/login/mobile'
        UnFollow.login(driver, url, phone_number.get(), password.get(), username.get(), max_unfollow_count.get())
    else:
        messagebox.showerror("Error", "Empty Fields Caused Error!")

def close_app():
    root.quit()

ttk.Button(main_frame, text="Start session", command=start_session).grid(column=0, row=5, sticky=tk.W)
ttk.Button(main_frame, text="Close app", command=close_app).grid(column=1, row=5, sticky=tk.E)

# Developer info
ttk.Label(main_frame, text="Developed By Amirreza5040").grid(columnspan=2, row=6, sticky=tk.W)

# Set padding for all child widgets
for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
