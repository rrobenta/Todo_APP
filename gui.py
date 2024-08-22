import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter to do")
add_button = sg.Button("Add")

window = sg.Window("MY TODO APP",
                   layout=[[label], [input_box, add_button]], font=('Helvetica', 20))
while True:
    event, values = window.read
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions
window.read()
window.close()
