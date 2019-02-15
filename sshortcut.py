import wx
from main_frame import MainFrame

def create_frame():
    frame = MainFrame(None, title="SSHortcut")
    frame.Show()

application = wx.App()
create_frame()
application.MainLoop()
