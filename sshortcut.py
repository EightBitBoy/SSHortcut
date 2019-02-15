import wx

def create_frame():
    main_frame = wx.Frame(None, title="SSHortcut")
    main_frame.Show()

application = wx.App()
create_frame()
application.MainLoop()
