from tkinter import *
from googleapiclient.discovery import build
import time
import threading

api_key = "" #type your api key between the "", you can create one here : https://developers.google.com/youtube/v3

youtube = build("youtube", "v3", developerKey = api_key)

channelId = input("Enter the channel's id : ") #my channel's id : UCj8uJy3x03dmAxqQNUQg_Mw

request = youtube.channels().list(part = "statistics", id = channelId)
window = Tk()

window.title("Subscriber counter")
photo = PhotoImage(file = "youtube_logo.png")
window.iconphoto(False, photo) 
window.geometry("720x480")
window.minsize(480, 360)
window.config(background="#FF000F")

followers_txt = Label(window, text="0", font=("Arial Black", 50), bg="#FF000F", fg="white")

followers_txt.pack(expand=YES)


def checkLoop():
    while True:
        print("request sended")
        reponse = request.execute()
        followers = reponse["items"][0]["statistics"]["subscriberCount"]
        followers_txt.config(text=followers)
        reponse = request.execute()
        time.sleep(10)

threading.Thread(target=checkLoop).start()


window.mainloop()
