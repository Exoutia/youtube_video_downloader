import tkinter as tk
from pytube import YouTube
root = tk.Tk()
root.geometry("500x500")
root.title("Youtube video Downloader")

tk.Label(root, text= "Enter the link of the video", font=("Helvetica", 16)).pack()
myVar = tk.StringVar()
myVar.set("Enter the link of the video")
tk.Entry(root, textvariable=myVar, font=("Helvetica", 16)).pack()
url = tk.StringVar()
tk.Entry(root, textvariable=url, font=("Helvetica", 16)).pack()
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
        
