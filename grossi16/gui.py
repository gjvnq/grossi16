#!/usr/bin/env python3

import tkinter as tk
import pygubu


class Application(pygubu.TkApplication):
    def _create_ui(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('base.ui')

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

        root.after(50, self._has_port_been_updated)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()