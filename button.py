import PySimpleGUI as sg
sg.theme('DarkGreen4')
sg.theme_text_color("#FFFF00")

window =  sg.Window(title="CONTOH BUTTON",
                layout=[[sg.Text("contoh button")],
                        [sg.Button("Simpan")],
                        [sg.Button("Keluar")]
                        ],
                size=(430,200),
                font=("Times, 18"))

kejadian,nilai= window.read()
print(kejadian,"=>",nilai)
window.close()