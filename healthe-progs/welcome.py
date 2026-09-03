#!/usr/bin/env python3
from ctypes import CDLL
CDLL('libgtk4-layer-shell.so')

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("Gtk4LayerShell", "1.0")
from gi.repository import Gtk, Adw, Gdk, Gtk4LayerShell as L

CSS = b"""
window.background {
    background-color: rgba(30, 30, 46, 0.8);
    border-radius: 12px;
    border: 2px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
}
"""


class App(Adw.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        css = Gtk.CssProvider()
        css.load_from_data(CSS)
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

        win = Gtk.Window(application=self)
        win.set_title("Hello, Hyprland!")
        win.set_default_size(800, 600)

        L.init_for_window(win)
        L.set_layer(win, L.Layer.OVERLAY)
        L.set_keyboard_mode(win, L.KeyboardMode.ON_DEMAND)
        L.set_namespace(win, "healthe-ui")

        key_ctrl = Gtk.EventControllerKey()
        key_ctrl.connect("key-pressed", lambda _, key, __, ___: win.close() if key == Gdk.KEY_Escape else None)
        win.add_controller(key_ctrl)

        close_btn = Gtk.Button(label="Close")
        close_btn.connect("clicked", lambda _: win.close())

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        box.set_margin_top(24)
        box.set_margin_bottom(24)
        box.set_margin_start(24)
        box.set_margin_end(24)
        box.set_valign(Gtk.Align.CENTER)
        box.set_halign(Gtk.Align.CENTER)

        label = Gtk.Label(label="Hello, Hyprland!")
        box.append(label)
        box.append(close_btn)

        win.set_child(box)
        win.present()


app = App()
app.run(None)
