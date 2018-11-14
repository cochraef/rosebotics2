import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    root = tkinter.Tk()

    sender = com.MqttClient()
    sender.connect_to_ev3()

    setup_gui(root, sender)
    root.mainloop()


def setup_gui(root_window, sender):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=100)
    frame.grid()

    ttk.Style().configure("TButton", padding=9, relief="flat")

    text1 = ttk.Label(frame, text='Play red light green light', )
    text1.grid()

    style = ttk.Style()
    style.map("C.TButton",
              foreground=[('pressed', 'green'), ('active', 'green')],
              background=[('pressed', 'green'), ('active', 'green')])

    go_forward_button = ttk.Button(frame, text="Green Light!", style="C.TButton",
                                   width='20')
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(sender)

    style = ttk.Style()
    style.map("B.TButton",
              foreground=[('pressed', 'yellow'), ('active', 'orange')],
              background=[('pressed', 'yellow'), ('active', 'yellow')])

    go_forward_slow_button = ttk.Button(frame, text="Yellow Light", style="B.TButton",
                                        width='20')
    go_forward_slow_button.grid()

    go_forward_slow_button['command'] = \
        lambda: handle_go_slow_forward(sender)

    style = ttk.Style()
    style.map("A.TButton",
              foreground=[('pressed', 'red'), ('active', 'red')],
              background=[('pressed', 'red'), ('active', 'red')])

    go_stop_button = ttk.Button(frame, text="Red Light", style="A.TButton",
                                width='20')
    go_stop_button.grid()

    go_stop_button['command'] = \
        lambda: handle_stop__(sender)


def handle_go_forward(sender):
    sender.send_message('go_forward')


def handle_go_slow_forward(sender):
    sender.send_message('go_forward_slow')


def handle_stop__(sender):
    sender.send_message('stop__')

main()