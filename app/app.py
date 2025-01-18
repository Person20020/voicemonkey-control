import tkinter as tk
from tkinter import filedialog, Text, simpledialog, OptionMenu, messagebox
import os


# Enter your API token here
token = ""#put api key here


root = tk.Tk()
root.title("Device Control Panel")
img = tk.PhotoImage(file='voicemonkey.png')
root.iconphoto(True, img)
devices = {
    "name": [],
    "id": [],
    "button": []
}
flows = {
    "name": [],
    "id": [],
    "button": []
}

deviceUrl = "https://api-v2.voicemonkey.io/trigger?token=" + token + "&device="
flowUrl = "https://api-v2.voicemonkey.io/trigger?token=" + token + "&flow="

def addDevice():
    newName = simpledialog.askstring(title="Input", prompt="Enter a name for the new device.", parent=root)
    newId = simpledialog.askstring(title="Input", prompt="Enter the Voice Monkey device ID.\nIt is everything after 'device=' in your routine trigger API URL.", parent=root)


    if newName is None or newId is None:
        return
    
    if newName == "" or newId == "":
        messagebox.showwarning(title="Missing values", message="One or both of the input boxes was empty. Please try again.")
        return
    
    devices["name"].append(newName)
    devices["id"].append(newId)

    newButton = tk.Button(frame, text=newName, padx=10, pady=5, fg="#ffffff", bg="#000000", command=lambda: print(newName))
    devices["button"].append(newButton)
    
    # Destroy all of the device buttons
    for button in deviceButtons.winfo_children():
        button.destroy()
    # Re pack all of the buttons
    for button in devices["button"]:
        button.pack(pady=5)

def addFlow():
    newName = simpledialog.askstring(title="Input", prompt="Enter a name for the new flow.", parent=root)
    newId = simpledialog.askstring(title="Input", prompt="Enter the Voice Monkey flow ID.\nIt is the number at the end of your flow API URL.", parent=root)


    if newName is None or newId is None:
        return
    
    if newName == "" or newId == "":
        messagebox.showwarning(title="Missing values", message="One or both of the input boxes was empty. Please try again.")
        return
    
    flows["name"].append(newName)
    flows["id"].append(newId)

    newButton = tk.Button(frame, text=newName, padx=10, pady=5, fg="#ffffff", bg="#000000", command=lambda: print(newName))
    newButton.pack(pady=5)

    for button in flowButtons.winfo_children():
        button.destroy()
    for button in flows["button"]:
        button.pack(pady=5)


canvas = tk.Canvas(root, height=700, width=700, bg="#aaaaaa")
canvas.pack()

frame = tk.Frame(root, bg="#ffffff")
frame.place(relwidth=0.98, relheight=0.98, relx=0.02/2, rely=0.02/2)

deviceFrame = tk.Frame(frame, bg="#ffffff")
deviceFrame.pack(pady=5)
addDeviceButton = tk.Button(deviceFrame, text="Add new device", padx=10, pady=5, fg="#ffffff", bg="#bbbbbb", command=addDevice)
addDeviceButton.pack(pady=10)
deviceButtons = tk.Frame(deviceFrame)
deviceButtons.pack()

flowFrame = tk.Frame(frame, bg="#ffffff")
flowFrame.pack(pady=5)
addFlowButton = tk.Button(flowFrame, text="Add new flow", padx=10, pady=5, fg="#ffffff", bg="#bbbbbb", command=addFlow)
addFlowButton.pack(pady=10)
flowButtons = tk.Frame(flowFrame)
flowButtons.pack()


root.mainloop()

if devices["name"]:
    for id in devices["id"]:
        print(id)
    for name in devices["name"]:
        print(name)

if flows["name"]:
    for id in flows["id"]:
        print(id)
    for name in flows["name"]:
        print(name)
