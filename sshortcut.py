import wx
from main_frame import MainFrame

def create_icon(frame):
    if not wx.adv.TaskBarIcon.IsAvailable():
        print("The taskbar icon is not available!") #TODO Handle this.
    icon = wx.adv.TaskBarIcon(frame)
    graphics = wx.Icon()
    loadSuccessful = graphics.LoadFile("icon_tray.png", type=wx.BITMAP_TYPE_PNG)
    print(loadSuccessful) #TODO Do something with this.
    setIconSuccessful = icon.SetIcon(graphics, "SSHortcut")
    print(setIconSuccessful) #TODO Do something with this.
    print(icon.IsIconInstalled()) #TODO Do something with this.

def create_frame():
    frame = MainFrame(None, title="SSHortcut")
    frame.Show()
    return frame

def initialize():
    application = wx.App()
    frame = create_frame()
    create_icon(frame)
    application.MainLoop()

if __name__ == '__main__':
    initialize()
