import os.path
from settings import settings
import tkinter as tk

PATH = "C:/Users/%s/%s/reach out" % (settings["username"], settings["script_location"])
FULL_PATH = os.path.join(PATH, "test.txt")

def writeFile():

	file = open(FULL_PATH, "w")

	file.write(
    """Hello %s,\n
I'm a technical support technician working on your ticket %s.
I see you still needed assistance.
My name is %s, feel free to reach me \
through teams, jabber, email, or we can set up a call.
I am available any time from %s %s.
Thanks, and hope to speak soon!\n
Best regards,\n%s\n%s@cisco.com \n%s""" % 
        (name.get().strip(" "), inc.get().strip(" "), settings["name"], settings["hours"],
        settings["tmz"], settings["name"], settings["username"], settings["number"]
        )
    )

gui = tk.Tk()

name = tk.Entry(gui)
name.grid(row=0, column=1)

inc = tk.Entry(gui)
inc.grid(row=1, column=1)

butonWrite = tk.Button(gui)
butonWrite.config(text = 'Write To File', command = writeFile)
butonWrite.grid(row=2, column=1)

gui.mainloop()