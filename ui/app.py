# -*- coding: utf-8 -*-
#
# Tencent is pleased to support the open source community by making QTA available.
# Copyright (C) 2016THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the BSD 3-Clause License (the "License"); you may not use this 
# file except in compliance with the License. You may obtain a copy of the License at
# 
# https://opensource.org/licenses/BSD-3-Clause
# 
# Unless required by applicable law or agreed to in writing, software distributed 
# under the License is distributed on an "AS IS" basis, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.
#
'''UISpy App启动入口
'''



import wx

from mainframe import MainFrame
from util.logger import Log


class UISpyApp(wx.App):
    
    def OnInit(self):
        self.main = MainFrame()
        self.main.Center()
        self.main.Show()
        self.SetTopWindow(self.main)
        return True


if __name__ == '__main__':
    try:
        Log.i('main','UISpy started...')
        app = UISpyApp()
        app.MainLoop()
    except:
        import traceback
        message = traceback.format_exc()
        Log.e('main', message)
        dialog = wx.MessageDialog(None, message, u"错误", wx.OK|wx.ICON_ERROR)
        dialog.ShowModal()