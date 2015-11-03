# -*- coding: UTF-8 -*-
#
# generated by wxGlade not found on Wed Oct 28 23:41:32 2015 from "/home/devin/Documents/ShuffleIR-Mobile/ShuffleFrame.wxg"
#

import wx
# Image Dialog
import wx.lib.mixins.inspection as wit
import wx.lib.imagebrowser as ib

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

from PIL import Image
import pyscreenshot as ImageGrab

import time, os, glob
import ConfigParser

from ShuffleClassifier import ShuffleClassifier

import dataNationalDex, dataStageID
import libImgConverter
import libListWindowsX11 as libListWindows
import config

mac = ShuffleClassifier()

# Frames
from dialogSelectIcons import dialogSelectIcons
from dialogNewIcon import dialogNewIcon
from dialogListWindows import dialogListWindows

class frameShuffleNew(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: frameShuffleNew.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.combo_StageID = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.sizer_2_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Stage ID"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Icons on board"), style=wx.ALIGN_LEFT)
        self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=[], style=wx.LB_NEEDED_SB | wx.LB_SINGLE)
        self.button_SI = wx.Button(self, wx.ID_ANY, _("Select Icons"))
        self.checkbox_Barrier = wx.CheckBox(self, wx.ID_ANY, _("Barriers on board?"))
        self.radio_Metal = wx.RadioBox(self, wx.ID_ANY, _("Metal Timer"), choices=[_("1"), _("2"), _("3"), _("4"), _("5")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("Snapshot"), style=wx.ALIGN_CENTER | wx.ALIGN_LEFT | wx.ALIGN_RIGHT)
        self.bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("images/snapshot_c.png", wx.BITMAP_TYPE_ANY))
        self.button_5 = wx.Button(self, wx.ID_ANY, _("Import"))
        self.button_6 = wx.Button(self, wx.ID_ANY, _("Snapshot"))
        self.button_7 = wx.Button(self, wx.ID_ANY, _("Export"))
        self.button_10 = wx.Button(self, wx.ID_ANY, _("Find Window"))
        self.button_8 = wx.Button(self, wx.ID_ANY, _("Save"))
        self.button_9 = wx.Button(self, wx.ID_ANY, _("Load"))
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Recognized Grid"), style=wx.ALIGN_CENTER)
        self.block = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_5 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_11 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_17 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_23 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_29 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_6 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_12 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_18 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_24 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_30 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_7 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_13 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_19 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_25 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_31 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_8 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_14 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_20 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_26 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_32 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_9 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_15 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_21 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_27 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_33 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_4 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_10 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_16 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_22 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_28 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.block_copy_34 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/Air.png", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, _("What to do with the result above?"), choices=[_("Edit Result"), _("Make New Icon")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.onStageID, self.combo_StageID)
        self.Bind(wx.EVT_COMBOBOX, self.onStageID, self.combo_StageID)
        self.Bind(wx.EVT_BUTTON, self.onSelectIcons, self.button_SI)
        self.Bind(wx.EVT_CHECKBOX, self.onBarrier, self.checkbox_Barrier)
        self.Bind(wx.EVT_RADIOBOX, self.onMetal, self.radio_Metal)
        self.Bind(wx.EVT_BUTTON, self.onBrowseSS, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.onCapture, self.button_6)
        self.Bind(wx.EVT_BUTTON, self.onExport, self.button_7)
        self.Bind(wx.EVT_BUTTON, self.onSetting, self.button_10)
        self.Bind(wx.EVT_BUTTON, self.onSave, self.button_8)
        self.Bind(wx.EVT_BUTTON, self.onLoad, self.button_9)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_5)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_11)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_17)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_23)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_29)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_6)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_12)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_18)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_24)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_30)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_1)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_7)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_13)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_19)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_25)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_31)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_2)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_8)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_14)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_20)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_26)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_32)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_3)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_9)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_15)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_21)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_27)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_33)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_4)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_10)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_16)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_22)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_28)
        self.Bind(wx.EVT_BUTTON, self.onBlock, self.block_copy_34)
        # end wxGlade
        
        # blocks
        self.blocks = [self.block, self.block_copy, self.block_copy_1, self.block_copy_2, self.block_copy_3, self.block_copy_4, self.block_copy_5, self.block_copy_6, self.block_copy_7, self.block_copy_8, self.block_copy_9, self.block_copy_10, self.block_copy_11, self.block_copy_12, self.block_copy_13, self.block_copy_14, self.block_copy_15, self.block_copy_16, self.block_copy_17, self.block_copy_18, self.block_copy_19, self.block_copy_20, self.block_copy_21, self.block_copy_22, self.block_copy_23, self.block_copy_24, self.block_copy_25, self.block_copy_26, self.block_copy_27, self.block_copy_28, self.block_copy_29, self.block_copy_30, self.block_copy_31, self.block_copy_32, self.block_copy_33, self.block_copy_34, ]
        for n in range(0,len(self.blocks)):
            self.blocks[n].gid = n
        
        self.icons = {}

        # ShuffleIR: load config
        self.load_config()
        
        # ShuffleIR: initial
        self.list_box_1.SetSelection(0)
        self.pathImage = 'images/snapshot.png'
        self.PILimage = Image.open(self.pathImage).crop(config.varBox)
        self.varSupportList=[]
        
        self.combo_StageID.AppendItems(dataStageID.list)
        
        self.idTargetWin = 12804312
        #self.onRecognize()
        
    def load_config(self):
        print 'Loading config'
        try:
            tmpConfig = ConfigParser.ConfigParser()
            # add the settings to the structure of the file, and lets write it out...
            tmpConfig.read("config.ini")

            # Setting
            config.pathShuffleMove = tmpConfig.get('Advance_Setting','Path to ShuffleMove')
            config.varStageID = tmpConfig.get('Setting','Stage ID')
            config.varMetalTimer=int(tmpConfig.get('Setting','Metal Timer'))
            exec("config.varIceSupport = " +tmpConfig.get('Setting','Barrier on Board'))
            exec("config.listSupport = " + tmpConfig.get('Setting','Icons on Board'))
            # Advance_Setting        
            exec("config.varBox = " + tmpConfig.get('Advance_Setting','Box to Crop'))
            config.BlockSize = int(tmpConfig.get('Advance_Setting','BlockSize'))
            config.pathMask = tmpConfig.get('Advance_Setting','Path to Mask')
            
            # Mask Path
            mac.mask = Image.open(config.pathMask)
            print "Config Loaded!"
            
            self.apply_config()
        except:
            wx.LogError("Cannot load config")
            pass
        
    def apply_config(self):
        # /Path/to/ShuffleMove
        #self.text_SM.SetValue( config.pathShuffleMove )
        
        #print config.varIceSupport == False
        # Ice
        self.checkbox_Barrier.SetValue(config.varIceSupport)
        #self.checkbox_Barrier.SetValue(True)
        
        # Metal
        self.radio_Metal.SetSelection(config.varMetalTimer-1)
        
        
        # Stage ID
        self.combo_StageID.SetValue(config.varStageID)
        
        # Icons
        for key in config.listSupport:
            self.list_box_1.Append(key + " : " + dataNationalDex.list.get(key))
            
    def __set_properties(self):
        # begin wxGlade: frameShuffleNew.__set_properties
        self.SetTitle(_("ShuffleIR Mobile"))
        self.list_box_1.SetMinSize(wx.DLG_SZE(self.list_box_1, (-1, 55)))
        self.checkbox_Barrier.SetValue(1)
        self.radio_Metal.SetSelection(4)
        self.block.SetSize(self.block.GetBestSize())
        self.block_copy_5.SetSize(self.block_copy_5.GetBestSize())
        self.block_copy_11.SetSize(self.block_copy_11.GetBestSize())
        self.block_copy_17.SetSize(self.block_copy_17.GetBestSize())
        self.block_copy_23.SetSize(self.block_copy_23.GetBestSize())
        self.block_copy_29.SetSize(self.block_copy_29.GetBestSize())
        self.block_copy.SetSize(self.block_copy.GetBestSize())
        self.block_copy_6.SetSize(self.block_copy_6.GetBestSize())
        self.block_copy_12.SetSize(self.block_copy_12.GetBestSize())
        self.block_copy_18.SetSize(self.block_copy_18.GetBestSize())
        self.block_copy_24.SetSize(self.block_copy_24.GetBestSize())
        self.block_copy_30.SetSize(self.block_copy_30.GetBestSize())
        self.block_copy_1.SetSize(self.block_copy_1.GetBestSize())
        self.block_copy_7.SetSize(self.block_copy_7.GetBestSize())
        self.block_copy_13.SetSize(self.block_copy_13.GetBestSize())
        self.block_copy_19.SetSize(self.block_copy_19.GetBestSize())
        self.block_copy_25.SetSize(self.block_copy_25.GetBestSize())
        self.block_copy_31.SetSize(self.block_copy_31.GetBestSize())
        self.block_copy_2.SetSize(self.block_copy_2.GetBestSize())
        self.block_copy_8.SetSize(self.block_copy_8.GetBestSize())
        self.block_copy_14.SetSize(self.block_copy_14.GetBestSize())
        self.block_copy_20.SetSize(self.block_copy_20.GetBestSize())
        self.block_copy_26.SetSize(self.block_copy_26.GetBestSize())
        self.block_copy_32.SetSize(self.block_copy_32.GetBestSize())
        self.block_copy_3.SetSize(self.block_copy_3.GetBestSize())
        self.block_copy_9.SetSize(self.block_copy_9.GetBestSize())
        self.block_copy_15.SetSize(self.block_copy_15.GetBestSize())
        self.block_copy_21.SetSize(self.block_copy_21.GetBestSize())
        self.block_copy_27.SetSize(self.block_copy_27.GetBestSize())
        self.block_copy_33.SetSize(self.block_copy_33.GetBestSize())
        self.block_copy_4.SetSize(self.block_copy_4.GetBestSize())
        self.block_copy_10.SetSize(self.block_copy_10.GetBestSize())
        self.block_copy_16.SetSize(self.block_copy_16.GetBestSize())
        self.block_copy_22.SetSize(self.block_copy_22.GetBestSize())
        self.block_copy_28.SetSize(self.block_copy_28.GetBestSize())
        self.block_copy_34.SetSize(self.block_copy_34.GetBestSize())
        self.radio_box_1.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: frameShuffleNew.__do_layout
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(6, 6, 0, 0)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.GridSizer(3, 2, 0, 0)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        sizer_2.Add(self.combo_StageID, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_3.Add(sizer_2, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_3.Add(self.label_2, 0, wx.EXPAND, 0)
        sizer_3.Add(self.list_box_1, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_3.Add(self.button_SI, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_3.Add(self.checkbox_Barrier, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        sizer_3.Add(self.radio_Metal, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_6.Add(sizer_3, 1, 0, 0)
        sizer_4.Add(sizer_6, 1, 0, 0)
        sizer_7.Add(self.label_4, 0, wx.EXPAND, 0)
        sizer_7.Add(self.bitmap, 0, wx.ALIGN_CENTER, 3)
        sizer_1.Add(self.button_5, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_1.Add(self.button_6, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_1.Add(self.button_7, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_1.Add(self.button_10, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_1.Add(self.button_8, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_1.Add(self.button_9, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_7.Add(sizer_1, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_4.Add(sizer_7, 0, wx.ADJUST_MINSIZE, 0)
        sizer_8.Add(self.label_5, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.block, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_5, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_11, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_17, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_23, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_29, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_6, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_12, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_18, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_24, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_30, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_7, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_13, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_19, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_25, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_31, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_2, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_8, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_14, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_20, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_26, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_32, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_3, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_9, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_15, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_21, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_27, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_33, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_4, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_10, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_16, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_22, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_28, 0, 0, 0)
        grid_sizer_1.Add(self.block_copy_34, 0, 0, 0)
        sizer_8.Add(grid_sizer_1, 1, 0, 0)
        sizer_8.Add(self.radio_box_1, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_4.Add(sizer_8, 1, 0, 0)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)
        self.Layout()
        # end wxGlade


    def path_newIcon(self, nameIcon):
        suffix = 0
        filename = nameIcon
        pathIcon = 'icons/'+filename + '.png'
        while os.path.isfile(pathIcon):
            #print os.path.isfile(pathIcon), suffix, pathIcon
            suffix += 1
            filename = nameIcon + '_' + str(suffix)
            pathIcon = 'icons/'+filename + '.png'
        return filename

    
    def onBlock(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        #print "Event handler 'onBlock' not implemented!"
        if self.radio_box_1.GetSelection() == 1:
            dlg = dialogNewIcon(self)
            if dlg.ShowModal() == wx.OK:
                #print dlg.keyIcon, dlg.nameIcon, event.GetEventObject().gid, dlg.checkbox_1.IsChecked()
                
                # Save raw block as an icon file
                filename = self.path_newIcon(dlg.nameIcon)
                n = event.GetEventObject().gid
                mac.save_block(n, 'icons/'+filename + '.png')
                self.get_icon(filename)
                
                print "Saving new icon to:", 'icons/'+filename + '.png'
                
                # Update support list
                flgKey = dlg.keyIcon in config.listSupport
                if not flgKey:
                    config.listSupport.append(dlg.keyIcon)
                    print "Updating Supported Icons"
                    # Icons
                    self.list_box_1.Clear()
                    for key in config.listSupport:
                        self.list_box_1.Append(key + " : " + dataNationalDex.list.get(key))
                # Recognize
                self.onRecognize()
                
                
                
                
                # Update block's image
                #icon = self.get_icon(filename)
                #block = event.GetEventObject()
                #block.SetBitmap(icon)   
                
                # Save result to mac
                #mac.results[n] = dataNationalDex.list.get(dlg.keyIcon)
                #mac.results_type[n] = str(dlg.checkbox_1.IsChecked()).lower()
                #mac.results_filenames[n] = filename
                
            dlg.Destroy()
        else:
            n = event.GetEventObject().gid
            index = self.list_box_1.GetSelection()
            key1 = config.listSupport[index]
            key2 = dataNationalDex.list.keys()[dataNationalDex.list.values().index(mac.results[n])].split( '-')[0]
            flgBarrier = mac.results_type[n] == 'true'
            print key1, key2, flgBarrier
            
            if key1 == key2:
                #change barrier type
                try:
                    if flgBarrier:
                        key = key1
                    else:
                        key = key1+'-i'
                        
                    # change image on app
                    icon = self.icons[key]
                    block = event.GetEventObject()
                    block.SetBitmap(icon)                    
                    
                    # change mac's result
                    mac.results_type[n] = str(not flgBarrier).lower()
                    
                except KeyError:
                    print "No icon: " + key
            else:
                #change barrier type
                try:
                    # change image on app
                    icon = self.icons[key1]
                    block = event.GetEventObject()
                    block.SetBitmap(icon)   
                    
                    # Save result to mac
                    mac.results[n] = dataNationalDex.list.get(key1)
                    mac.results_type[n] = 'false'
                    mac.results_filenames[n] = key1
                    
                except KeyError:
                    print "No icon: " + key
            
        #print event.GetEventObject()
        
        event.Skip()
        
        
    def onMetal(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        config.varMetalTimer = self.radio_Metal.GetSelection()+1
        print "Metal Timer: " + str(config.varMetalTimer)
        
        
    def onExport(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        print "Exporting results to ShuffleMove"
        mac.write_board(config.varStageID, config.pathBoard)
        
    def onSetting(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        dlg = dialogListWindows(self)
        if dlg.ShowModal() == wx.OK:
            self.idTargetWin = dlg.winID
            print dlg.winID
        dlg.Destroy()
        
    def onSave(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        try:
            tmpConfig = ConfigParser.ConfigParser()
            # add the settings to the structure of the file, and lets write it out...
            cfgfile = open("config.ini",'w')
            # Setting
            tmpConfig.add_section('Setting')
            tmpConfig.set('Setting','Stage ID', config.varStageID)
            tmpConfig.set('Setting','Metal Timer', config.varMetalTimer)
            tmpConfig.set('Setting','Barrier on Board', config.varIceSupport )
            tmpConfig.set('Setting','Icons on Board', config.listSupport)
            # Advance_Setting        
            tmpConfig.add_section('Advance_Setting')
            tmpConfig.set('Advance_Setting','Path to ShuffleMove', config.pathShuffleMove)
            tmpConfig.set('Advance_Setting','Box to Crop', config.varBox)
            tmpConfig.set('Advance_Setting','BlockSize', config.BlockSize)
            tmpConfig.set('Advance_Setting','Path to Mask', config.pathMask)
            
            tmpConfig.write(cfgfile)
            cfgfile.close()
            print "Config Saved!"
        except:
            wx.LogError("Cannot save config")
            pass
        
    def onLoad(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        self.load_config()
        
    def onBarrier(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        config.varIceSupport = self.checkbox_Barrier.GetValue()
        print 'Barrier Setting: ' + str(config.varIceSupport)
    
    def get_icon(self,key):
        try:
            icon = self.icons[key]
        except KeyError:
            print "loading icon: "+key
            pathIcon = 'icons/'+key + '.png'
            img= wx.Image(pathIcon, type=wx.BITMAP_TYPE_ANY)
            img = img.Rescale(38,38,wx.IMAGE_QUALITY_HIGH)
            icon = img.ConvertToBitmap()
            self.icons[key] = icon
        return self.icons[key]
        
    def load_icons(self):
        # loading icons
        tmpList = []
        for tmp in self.varSupportList:
            key = tmp[3]
            self.get_icon(key)
            tmpList.append(key)
            
        # destroying icons
        for key in self.icons.keys():
            if tmpList.count(key) < 1:
                print "Removing icon: " + key
                del self.icons[key]
        
        #print len(self.varSupportList), self.varSupportList
        #print len(self.icons.keys()), self.icons.keys()
        
    def onSelectIcons(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        dlg = dialogSelectIcons(self)
        if dlg.ShowModal() == wx.OK:
            print "Updating Supported Icons"
            # Icons
            self.list_box_1.Clear()
            for key in config.listSupport:
                self.list_box_1.Append(key + " : " + dataNationalDex.list.get(key))
        dlg.Destroy()
        
        
    def onBrowseSS(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        
        #openFileDialog = wx.lib.imagebrowser.ImageDialog(self, 'samples/')
        with ib.ImageDialog(self) as openFileDialog:
            
            if openFileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed idea...

            # proceed loading the file chosen by the user
            # this can be done with e.g. wxPython input streams:
            try:
                PILimage = Image.open(openFileDialog.GetFile())
            except:
                wx.LogError("Cannot open file '%s'."%openFileDialog.GetPath())
                pass
                event.skip
        
        self.pathImage = openFileDialog.GetFile()
        openFileDialog.Destroy()
        
        if flagDebug:
            PILimage.save('image/snapshot.png','PNG')
        
        self.PILimage = PILimage.crop(config.varBox)
        
        #print self.PILimage.resize((240,240))
        
        self.bitmap.SetBitmap(libImgConverter.PilImageToWxBitmap(self.PILimage.resize((240,240))))
        
        self.onRecognize()
        
    def onCapture(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        
        img=ImageGrab.grab(bbox=libListWindows.getBox(self.idTargetWin), backend='imagemagick')
        self.PILimage = img.crop(config.varBox)
        self.bitmap.SetBitmap(libImgConverter.PilImageToWxBitmap(self.PILimage.resize((240,240))))
        
        #print config.pathMask, config.BlockSize, self.PILimage
        self.onRecognize()
        
        
    def onStageID(self, event):  # wxGlade: frameShuffleNew.<event_handler>
        config.varStageID = self.combo_StageID.GetValue()
        print 'Stage ID: ' + config.varStageID 
        
        
    def onRecognize(self):  # wxGlade: frameShuffle.<event_handler>
        print "Pre-checking icons..."
        self.varSupportList=[]
        # Ordinary Icons
        for tmp in config.listSupport:
            self.try_support(tmp, dataNationalDex.list.get(tmp), 'false')
            # Barriered Icons
            if config.varIceSupport != 0:
                self.try_support(tmp + '-i', dataNationalDex.list.get(tmp), 'true')
                
        #print self.varSupportList
        print "Re-importing icons to classifer...", self.varSupportList
        mac.clear_references()
        # Load Reference Icons
        for tmp in self.varSupportList:
            mac.add_reference(tmp[3],tmp[1],tmp[2])
        
        # Import Image to Classifer
        print "Loading image to classifer..."
        mac.load_image2(self.PILimage)
        print "Classifying"
        mac.classify()
        
        print "Displaying results"
        
        self.load_icons()
        
        for n in range(0,36):
            block = self.blocks[n]
            key = mac.results_filenames[n]
            icon = self.icons[key]
            block.SetBitmap(icon)
            #print n, mac.results[n], mac.results_filenames[n]
            
    def try_support(self, nameIcon0, namePokemon, typeIced='false'):
        suffix = 0
        nameIcon = nameIcon0
        pathIcon = 'icons/'+nameIcon + '.png'
        while os.path.isfile(pathIcon):
            self.varSupportList.append((nameIcon0, namePokemon, typeIced, nameIcon))
            
            print("Loaded " + namePokemon + ": " +pathIcon)
            suffix += 1
            nameIcon = nameIcon0 + '_' + str(suffix) 
            pathIcon = 'icons/'+ nameIcon+ '.png'
            
# end of class frameShuffleNew
