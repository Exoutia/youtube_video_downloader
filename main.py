import tkinter as tk
from pytube import YouTube
root = tk.Tk()
root.attributes("-topmost", False, "-alpha", 0.9)
root.configure(bg='blue')
root.geometry("500x500")
root.title("Youtube video Downloader")

tk.Label(root, text= "Your Personal Youtube Video Downloader", font=("Arial", 16)).pack()
myVar = tk.StringVar()
myVar.set("Enter the link of the video")
tk.Entry(root, textvariable=myVar, font=("Monospace", 15)).pack()
url = tk.StringVar()
tk.Entry(root, textvariable=url, font=("Arial", 15)).pack()
tk.Button(root, text="Download", command=lambda: download()).pack()


def download():
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(url.get()).streams.first().download()
        url.set("Downloaded")
    except Exception as e:
        url.set("Error")
        root.update()

root.mainloop()    
        
