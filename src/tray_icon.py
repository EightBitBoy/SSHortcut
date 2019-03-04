import wx

ICON_PATH = "icon_tray.png"
ICON_TOOLTIP = "SSHortcut"

class TrayIcon(wx.adv.TaskBarIcon):
    def __init__(self, main_frame):
        super(TrayIcon, self).__init__()
        self.main_frame = main_frame
        self.SetIcon(wx.Icon(ICON_PATH), ICON_TOOLTIP)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_click)
        #icon = wx.adv.TaskBarIcon()
        #graphics = wx.Icon("icon_tray.png")
        #loadSuccessful = graphics.LoadFile("icon_tray.png", type=wx.BITMAP_TYPE_PNG)
        #print(loadSuccessful) #TODO Do something with this.
        #setIconSuccessful = icon.SetIcon(graphics, "SSHortcut")
        #print(setIconSuccessful) #TODO Do something with this.
        #print(icon.IsIconInstalled()) #TODO Do something with this.

    def on_left_click(self, event):
        print("left click")
