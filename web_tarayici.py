import tkinter as tk
from tkinter import ttk
import webview
import threading

class WebBrowserApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Web Tarayici")
        self.master.geometry("600x150")

        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(master, textvariable=self.url_var, font=("Arial", 12), width=50)
        self.url_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        ttk.Button(master, text="Git", command=self.navigate).grid(row=0, column=3, padx=5)
        ttk.Button(master, text="Yenile", command=self.refresh).grid(row=1, column=0, pady=5)
        ttk.Button(master, text="Geri", command=self.go_back).grid(row=1, column=1)
        ttk.Button(master, text="İleri", command=self.go_forward).grid(row=1, column=2)

        self.webview_window = None

        self.default_url = "https://www.google.com"
        self.start_browser(self.default_url)

    def start_browser(self, url):
        def thread_func():
            self.webview_window = webview.create_window("Python Tarayıcı", url)
            webview.start(debug=True)
        threading.Thread(target=thread_func, daemon=True).start()

    def navigate(self):
        url = self.url_var.get()
        if not url.startswith("http"):
            url = "https://" + url
        try:
            self.webview_window.load_url(url)
        except:
            print("WebView henüz hazir değil.")
    
    def refresh(self):
        try:
            self.webview_window.reload()
        except:
            print("Yenileme başarisiz.")

    def go_back(self):
        try:
            self.webview_window.evaluate_js("history.back()")
        except:
            print("Geri gidilemedi.")

    def go_forward(self):
        try:
            self.webview_window.evaluate_js("history.forward()")
        except:
            print("İleri gidilemedi.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebBrowserApp(root)
    root.mainloop()
