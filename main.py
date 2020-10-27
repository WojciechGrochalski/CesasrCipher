# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import CipherC as Cipher
import textract


import PySimpleGUI as sg
text = "CEASER cipher DEMO"
s = 4

#filename = sg.popup_get_file('Enter the file you wish to process')
file_browse=[
    [sg.Text("Choose File"),
     sg.In(size=(25, 1), enable_events=True,key="-FILE-"),
     sg.FileBrowse(),
     sg.Button('Ok')]
]
intput=[
    [
        sg.Text(size=(45,30), key="-TOIN-")
    ]
]
output=[
    [
         sg.Text(size=(45,30), key="-TOUT-")
    ]
]
layout=[
    [
        sg.Column(file_browse),
        sg.VSeparator(),
        sg.Column(intput),
        sg.VSeparator(),
        sg.Column(output),
    ]
]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if (event == sg.WINDOW_CLOSED or event == 'Quit'):
        break
    if(event=="-FILE-"):
        file=values["-FILE-"]
        tex =textract.process(file)
        tex=tex.decode("utf-8")
        encrypted = Cipher.encrypt(tex,s)
        decrypted = Cipher.decrypt(encrypted,s)
        window["-TOIN-"].update(encrypted)
        window["-TOUT-"].update(decrypted)




    # Output a message to the window


# Finish up by removing from the screen



#Encrtypted file


#Decrypt file

f=open("test.doc","wt")
# if(f.mode=="wt"):
#     f.write(decrypted)
#     f.close()

window.close()
