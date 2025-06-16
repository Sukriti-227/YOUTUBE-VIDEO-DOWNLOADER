from tkinter import *      
from pytube import *
 
# downlaod_video is a function to downaload youtube video through using pytube module 
def download_video():
    try:
        yt = YouTube(url_entry.get())
        video = yt.streams.get_highest_resolution()
        video.download()
        status_label.config(text="Download completed!")
    except Exception as e:
        status_label.config(text="Error occurred. Please check the URL.\n")

#************************** Using tkinter to make a GUI(Graphical user interface) page************************

#  root = Tk() is used for generate a GUI page 
root = Tk()

# geometry is built in function of tkinter module which is used to resize of GUI Page
root.geometry("900x700")

# title function is used to get a title of your GUI Page
root.title("YOUTUBE VIDEO DOWNLOADER")

# name_label = variable is used to get name in the GUI Page
name_label = Label(root , text="YOUTUBE VIDEO DOWNLOADER  \n" , font=(SUNKEN,25) ,background="red" , foreground="white")
name_label.pack() # pack is compulsory to get output of the label

url_label = Label(root, text="Enter YouTube URL and Link: " , font = SUNKEN ,background="red", foreground="white" ) 
url_label.pack()

# url_entry name variable is used to make a entry block where we can paste the url and link of youtube video
url_entry = Entry(root, width=50, font=SUNKEN  )
url_entry.pack() 

# PhotoImage is function to find a resource image in png form 
photo = PhotoImage(r"youtube png.png")
# We make a variable img_label where we use the (image) function
img_label = Label(image=photo) 

img_label.pack()

click_label = Label(root , text="  Click here download  \n\n  👇👇👇  " , font=SUNKEN ,background="white")
click_label.pack()

# Button() function is specially used to generate a button in GUI and it is compulsory to get a commond in your button function.
download_label = Button(root, text="\n Download", command=download_video , font = SUNKEN , background="green")
download_label.pack()

# Status label is used to show your configration of download completed and error on your screen.
status_label = Label(root , text="  \n👇👇" ,font = SUNKEN , background="white")
status_label.pack()

# owner_label is used to show the owner name in this GUI page 
owner_label = Label(root , text="Developer = Vaishnavi Kasoudhan , Sukriti Gangwar" , font=SUNKEN )
owner_label.pack()

# this is used to help the coder to make it is understanding code
helper_label = Label(root ,text="This program is specially developed for download the youtube video directly . \n Paste the url of video ")
helper_label.pack()

# steps_label is used to how to used this GUI page in easy and simple way ..........
steps_label = Label(root , text=" \nThanks for visiting my GUI \n\n 1. Copy url of youtube video \n 2. Paste into the entry block \n 3. Click to download button \n 4. If found a error then check url of youtube video")
steps_label.pack()

# Start the main loop
root.mainloop()

# Thanks for visiting my program dear Sir/Mam