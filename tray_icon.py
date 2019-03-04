import wx

class TrayIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
