import wx
from main_frame import MainFrame

def create_icon():
    if not wx.adv.TaskBarIcon.IsAvailable():
        print("The taskbar icon is not available!") #TODO Handle this.
    icon = wx.adv.TaskBarIcon()
    graphics = wx.Icon()
    loadSuccessful = graphics.LoadFile("icon_tray.png", type=wx.BITMAP_TYPE_PNG)
    print(loadSuccessful) #TODO Do something with this.
    setIconSuccessful = icon.SetIcon(graphics)
    print(setIconSuccessful) #TODO Do something with this.
    print(icon.IsIconInstalled()) #TODO Do something with this.

def create_frame():
    frame = MainFrame(None, title="SSHortcut")
    frame.Show()

def initialize():
    application = wx.App()
    create_icon()
    create_frame()
    application.MainLoop()

if __name__ == '__main__':
    initialize()
