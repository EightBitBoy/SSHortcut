import wx
import wx.adv

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.tb_icon = wx.adv.TaskBarIcon()
        print(self.tb_icon.IsOk())
