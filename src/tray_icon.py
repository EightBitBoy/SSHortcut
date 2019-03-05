import wx

ICON_PATH = "assets/icon_tray.png" #TODO Read about systemindependent file paths
ICON_TOOLTIP = "SSHortcut"

class TrayIcon(wx.adv.TaskBarIcon):
    def __init__(self, main_frame: wx.Frame):
        super(TrayIcon, self).__init__()
        self.main_frame = main_frame

        if not wx.adv.TaskBarIcon.IsAvailable():
            print("The taskbar icon is not available!") #TODO Handle this.

        self.SetIcon(wx.Icon(ICON_PATH), ICON_TOOLTIP)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.on_left_click)
        #icon = wx.adv.TaskBarIcon()
        #graphics = wx.Icon("icon_tray.png")
        #loadSuccessful = graphics.LoadFile("icon_tray.png", type=wx.BITMAP_TYPE_PNG)
        #print(loadSuccessful) #TODO Do something with this.
        #setIconSuccessful = icon.SetIcon(graphics, "SSHortcut")
        #print(setIconSuccessful) #TODO Do something with this.
        #print(icon.IsIconInstalled()) #TODO Do something with this.

    def add_menu_item(self, menu, label, function):
        item = wx.MenuItem(menu, -1, label)
        menu.Bind(wx.EVT_MENU, function, id = item.GetId())
        menu.Append(item)
        return item

    def CreatePopupMenu(self):
        menu = wx.Menu()
        self.add_menu_item(menu, 'Action', self.on_action)
        menu.AppendSeparator()
        self.add_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def on_left_click(self, event):
        print("left click")

    def on_action(self, event):
        print("action")

    #TODO Find you if existing the application this way is correct.
    #TODO Probably should handle exit in main frame.
    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.main_frame.Close()
