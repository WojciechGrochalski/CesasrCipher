# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import CipherC as Cipher
import textract


import PySimpleGUI as sg
#Pattern
pattern=4
encrypted=""
decrypted=""
radio_choices = []
file_browse=[
    [
     sg.Text("Choose File"),
     sg.In(size=(25, 1), enable_events=True,key="-FILE-"),
     sg.FileBrowse(),
     sg.Button('Ok')
    ],
    [
     sg.Radio('Encrypt',"RADIO1",enable_events=True,key="-EN-"),
     sg.Radio('Decrypt',"RADIO1",enable_events=True,key="-DE-"),
     sg.Checkbox('Save to new file',enable_events=True,key="-SAVE-", visible=False)
    ],
    [
     sg.Text("Choose File Name", key='-SAVE_Text-', visible=False),
     sg.In(size=(25, 1), enable_events=True, key='-SAVE_IN-', visible=False),
     sg.Button('Ok', enable_events=True, key='-SAVE_OK-', visible=False)
    ]
]
save_file=[
    [
     sg.Text("Choose File"),
     sg.In(size=(25, 1), enable_events=True),
     sg.FileBrowse(),
     sg.Button('Ok')
    ]
]
intput=[
    [
        sg.Text(auto_size_text=True,size=(20 ,30), key="-TOIN-")
    ]
]
output=[
    [
         sg.Text(auto_size_text=True,size=(20 ,30), key="-TOOT-")
    ]
]
layout=[
    [
        sg.Col(file_browse),
        sg.VSeparator(),
        sg.Column(intput),
        sg.VSeparator(),
        sg.Column(output),
    ]
]

window = sg.Window('Cesar Cipher', layout)
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if (event == sg.WINDOW_CLOSED or event == 'Quit'):
        break
    if(event=="-FILE-"):
        file=values["-FILE-"]
        tex =textract.process(file)
        tex=tex.decode("utf-8")
        encrypted = Cipher.encrypt(tex, pattern)
        decrypted = Cipher.decrypt(encrypted, pattern)
    if(values["-EN-"]or values["-DE-"]):
        window.FindElement('-SAVE-').update(visible=True)
        if(values['-EN-'] and values['-FILE-']):
            window["-TOIN-"].update(encrypted)
            window["-TOOT-"].update("")
        if(values['-DE-'] and values['-FILE-']):
            window["-TOOT-"].update(decrypted)
            window["-TOIN-"].update("")
        if(event=='-SAVE-'):
             window.FindElement('-SAVE_Text-').update(visible=True)
             window.FindElement('-SAVE_IN-').update(visible=True)
             window.FindElement('-SAVE_OK-').update(visible=True)
    if(event=='-SAVE_OK-'and (encrypted or decrypted)):
         save_file_name=values['-SAVE_IN-']
         if(values['-DE-']):
             f=open(save_file_name+'.txt',"wt")
             if(f.mode=="wt"):
                 f.write(decrypted)
                 f.close()
         if(values['-EN-']):
             f=open(save_file_name+'.txt',"wt")
             if(f.mode=="wt"):
                 f.write(encrypted)
                 f.close()

window.close()
