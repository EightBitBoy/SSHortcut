import wx

ICON_PATH = "icon_tray.png"
ICON_TOOLTIP = "SSHortcut"

class TrayIcon(wx.adv.TaskBarIcon):
    def __init__(self, main_frame):
        self.main_frame = main_frame
        icon = wx.Icon(ICON_PATH)
        self.SetIcon(icon, ICON_TOOLTIP)
