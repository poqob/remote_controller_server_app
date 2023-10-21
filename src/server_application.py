import tkinter as tk
from server_manager import ServerManager
import threading

# TODO
# dedect computer ip-port pass it to server. --later
# server will send packages to computer's


class ServerManagerApp:
    # fields
    # rcoln_api\config.ini
    sm = ServerManager("./config.ini")
    global root

    def __init__(self, root):
        self.root = root
        # Create a frame to hold the buttons
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Create the buttons
        self.start_button = tk.Button(
            self.frame, text="Start Server", command=self.start_server
        )
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(
            self.frame, text="Stop Server", command=self.stop_server
        )
        self.stop_button.grid(row=0, column=1, padx=10)

    def start_server(self):
        # threading
        threading.Thread(target=self.sm.start).start()

    def stop_server(self):
        self.sm.stop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Server Manager")
    app = ServerManagerApp(root)
    root.mainloop()
