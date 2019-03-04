import wx
from main_frame import MainFrame
from tray_icon import TrayIcon

def create_tray_icon(frame: wx.Frame):
    TrayIcon(frame)


def create_frame():
    frame = MainFrame(None, title="SSHortcut")
    frame.Show()
    return frame

def initialize():
    application = wx.App()
    frame = create_frame()
    create_tray_icon(frame)
    application.MainLoop()

if __name__ == '__main__':
    initialize()
