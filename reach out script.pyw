import os.path
import tkinter as tk
from settings import settings

#Set path
PATH = "C:/Users/%s/%s/" % (settings["username"], settings["script_location"])
FULL_PATH = os.path.join(PATH, "reach out.txt")

#Backbone of program. Writes a reach out script to file 
#named 'reach out.txt' using variables assigned in settings.py
def writeFile():
        
        #Open new file or overwrite existing
	file = open(FULL_PATH, "w")

        #Write to file
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
	#Respond to button click
	buttonWrite.config(fg="green", text="Written To File!")


#Create window
gui = tk.Tk()
gui.title("Reach Out")
gui.geometry("225x100")

#Get case number
inc_label = tk.Label(gui, text="Inc:", padx=10, pady=5)
inc_label.grid(row=0, column=0)
inc = tk.Entry(gui)
inc.grid(row=0, column=1)
inc.focus()

#Get client's name
name_label = tk.Label(gui, text="Name:", padx=10, pady=5)
name_label.grid(row=1, column=0)
name = tk.Entry(gui)
name.grid(row=1, column=1)

#Run writeToFile() function using user input
buttonWrite = tk.Button(gui, padx=10, pady=5)
buttonWrite.config(fg="blue", text="Write To File", command=writeFile)
buttonWrite.grid(row=2, column=1)

#Start GUI
gui.mainloop()
