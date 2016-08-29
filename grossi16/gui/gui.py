#!/usr/bin/env python3

__author__ = "Gabriel Queiroz"
__credits__ = ["Gabriel Queiroz", "Estevão Lobo", "Pedro Ilído"]
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "Gabriel Queiroz"
__email__ = "gabrieljvnq@gmail.com"
__status__ = "alpha"

try:
    import tkinter as tk
except:
    try:
        import Tkinter as tk
    except:
        import sys
        print("FAILED TO LOAD GUI: TKINTER MODULE IS NOT AVAILABLE")
        print("Please, install tkinter and reload this app or use the command line interface via grossi16-cli")
        sys.exit(1)


import pygubu
import pkg_resources

class Application(pygubu.TkApplication):
    def _create_ui(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_string(pkg_resources.resource_string("grossi16.gui", "base.ui"))


        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('MainFrame', self.master)
        self._port_box = self.builder.get_object("PortBox")
        self._port_box.set("8080")
        self._last_port = "8080"

        self.master.minsize(width=250, height=100)
        self.master.maxsize(width=250, height=100)
        self.master.title("Grossi 16")
        builder.connect_callbacks(self)

        self._has_port_been_updated()

    def _on_port_change(self, event):
        print("Port changed")
        print(event.widget.get())

    def _on_url_click(self, event):
        print("Url clicked")
        # print(help(event))

    def _has_port_been_updated(self):
        if self._port_box.get() != self._last_port:
            self._last_port = self._port_box.get()
            print("Changed port to ", self._last_port)

        self.master.after(50, self._has_port_been_updated)

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()
