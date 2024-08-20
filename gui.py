import FreeSimpleGUI as sg
label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter to do")
add_button = sg.Button("Add")

window = sg.Window("MY TODO APP", layout=[[label], [input_box, add_button]])
window.read()
window.close()