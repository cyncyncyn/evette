#!?usr/bin/python
# -*- coding: UTF-8 -*-

#Copyright (C) 2007 Adam Spencer - Free Veterinary Management Suite

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

##Contact: evetteproject@dsl.pipex.com

import wx
import wx.html
import miscmethods
import db
import dbmethods
import customwidgets

ADD_USER = 1301
EDIT_USER = 1302
DELETE_USER = 1304
REFRESH_USERS = 1305

class GenericSettingsPanel(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, parent, title):
		
		self.localsettings = parent.GetParent().localsettings
		
		wx.Panel.__init__(self, parent)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		edit = wx.CheckBox(self, -1, self.GetLabel("editlabel"))
		edit.Bind(wx.EVT_CHECKBOX, self.EditChecked)
		topsizer.Add(edit, 0, wx.ALIGN_LEFT)
		
		delete = wx.CheckBox(self, -1, self.GetLabel("deletelabel"))
		delete.Bind(wx.EVT_CHECKBOX, self.DeleteChecked)
		topsizer.Add(delete, 0, wx.ALIGN_LEFT)
		
		self.SetSizer(topsizer)
		
		self.edit = edit
		self.delete = delete
	
	def DeleteChecked(self, ID):
		
		if self.delete.GetValue() == True:
			self.edit.SetValue(True)
	
	def EditChecked(self, ID):
		
		if self.edit.GetValue() == False:
			self.delete.SetValue(False)

class AppointmentSettingsPanel(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, parent, title):
		
		self.localsettings = parent.GetParent().localsettings
		
		wx.Panel.__init__(self, parent)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		edit = wx.CheckBox(self, -1, self.GetLabel("editlabel"))
		edit.Bind(wx.EVT_CHECKBOX, self.EditChecked)
		topsizer.Add(edit, 0, wx.ALIGN_LEFT)
		
		delete = wx.CheckBox(self, -1, self.GetLabel("deletelabel"))
		delete.Bind(wx.EVT_CHECKBOX, self.DeleteChecked)
		topsizer.Add(delete, 0, wx.ALIGN_LEFT)
		
		vetform = wx.CheckBox(self, -1, self.GetLabel("editvetformlabel"))
		vetform.Bind(wx.EVT_CHECKBOX, self.EditVetFormChecked)
		topsizer.Add(vetform, 0, wx.ALIGN_LEFT)
		
		self.SetSizer(topsizer)
		
		self.edit = edit
		self.delete = delete
		self.vetform = vetform
	
	def DeleteChecked(self, ID):
		
		if self.delete.GetValue() == True:
			self.edit.SetValue(True)
	
	def EditChecked(self, ID):
		
		if self.edit.GetValue() == False:
			self.delete.SetValue(False)
			self.vetform.SetValue(False)
	
	def EditVetFormChecked(self, ID):
		
		if self.vetform.GetValue() == True:
			self.edit.SetValue(True)

class ClientSettingsPanel(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, parent, title):
		
		self.localsettings = parent.GetParent().localsettings
		
		wx.Panel.__init__(self, parent)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		edit = wx.CheckBox(self, -1, self.GetLabel("editlabel"))
		edit.Bind(wx.EVT_CHECKBOX, self.EditChecked)
		topsizer.Add(edit, 0, wx.ALIGN_LEFT)
		
		delete = wx.CheckBox(self, -1, self.GetLabel("deletelabel"))
		delete.Bind(wx.EVT_CHECKBOX, self.DeleteChecked)
		topsizer.Add(delete, 0, wx.ALIGN_LEFT)
		
		editfinances = wx.CheckBox(self, -1, self.GetLabel("editfinanceslabel"))
		topsizer.Add(editfinances, 0, wx.ALIGN_LEFT)
		
		self.SetSizer(topsizer)
		
		self.edit = edit
		self.delete = delete
		self.editfinances = editfinances
	
	def DeleteChecked(self, ID):
		
		if self.delete.GetValue() == True:
			self.edit.SetValue(True)
	
	def EditChecked(self, ID):
		
		if self.edit.GetValue() == False:
			self.delete.SetValue(False)

class MiscSettingsPanel(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, parent, title):
		
		self.localsettings = parent.GetParent().localsettings
		
		wx.Panel.__init__(self, parent)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		toolbar = wx.CheckBox(self, -1, self.GetLabel("showtoolbarlabel"))
		topsizer.Add(toolbar, 0, wx.ALIGN_LEFT)
		
		changelog = wx.CheckBox(self, -1, self.GetLabel("viewchangeloglabel"))
		topsizer.Add(changelog, 0, wx.ALIGN_LEFT)
		
		editsettings = wx.CheckBox(self, -1, self.GetLabel("editsettingslabel"))
		topsizer.Add(editsettings, 0, wx.ALIGN_LEFT)
		
		multiplepanels = wx.CheckBox(self, -1, self.GetLabel("multiplepanellabel"))
		topsizer.Add(multiplepanels, 0, wx.ALIGN_LEFT)
		
		asmsync = wx.CheckBox(self, -1, self.GetLabel("synctoasmlabel"))
		topsizer.Add(asmsync, 0, wx.ALIGN_LEFT)
		
		self.SetSizer(topsizer)
		
		self.toolbar = toolbar
		self.changelog = changelog
		self.editsettings = editsettings
		self.multiplepanels = multiplepanels
		self.asmsync = asmsync

class DiarySettingsPanel(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, parent, title):
		
		self.localsettings = parent.GetParent().localsettings
		
		wx.Panel.__init__(self, parent)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		adddiarynotes = wx.CheckBox(self, -1, self.GetLabel("adddiarynotes"))
		topsizer.Add(adddiarynotes, 0, wx.ALIGN_LEFT)
		
		editdiarynotes = wx.CheckBox(self, -1, self.GetLabel("editdiarynotes"))
		topsizer.Add(editdiarynotes, 0, wx.ALIGN_LEFT)
		
		deletediarynotes = wx.CheckBox(self, -1, self.GetLabel("deletediarynotes"))
		topsizer.Add(deletediarynotes, 0, wx.ALIGN_LEFT)
		
		self.SetSizer(topsizer)
		
		self.adddiarynotes = adddiarynotes
		self.editdiarynotes = editdiarynotes
		self.deletediarynotes = deletediarynotes

class UserSettingsPanel(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, parent, title):
		
		self.localsettings = parent.GetParent().localsettings
		
		wx.Panel.__init__(self, parent)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		edit = wx.CheckBox(self, -1, self.GetLabel("editlabel"))
		edit.Bind(wx.EVT_CHECKBOX, self.EditChecked)
		topsizer.Add(edit, 0, wx.ALIGN_LEFT)
		
		delete = wx.CheckBox(self, -1, self.GetLabel("deletelabel"))
		delete.Bind(wx.EVT_CHECKBOX, self.DeleteChecked)
		topsizer.Add(delete, 0, wx.ALIGN_LEFT)
		
		editrota = wx.CheckBox(self, -1, self.GetLabel("editrotalabel"))
		topsizer.Add(editrota, 0, wx.ALIGN_LEFT)
		
		self.SetSizer(topsizer)
		
		self.edit = edit
		self.delete = delete
		self.editrota = editrota
	
	def DeleteChecked(self, ID):
		
		if self.delete.GetValue() == True:
			self.edit.SetValue(True)
	
	def EditChecked(self, ID):
		
		if self.edit.GetValue() == False:
			self.delete.SetValue(False)

class EditStaffPanel(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, notebook, localsettings):
		
		self.localsettings = localsettings
		
		self.pagetitle = miscmethods.GetPageTitle(notebook, self.GetLabel("editstaffpagetitle"))
		
		wx.Panel.__init__(self, notebook)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		userlist = wx.ListBox(self, -1)
		userlist.Bind(wx.EVT_RIGHT_DOWN, self.Popup)
		userlist.Bind(wx.EVT_LISTBOX_DCLICK, self.EditUser)
		topsizer.Add(userlist, 1, wx.EXPAND)
		
		self.SetSizer(topsizer)
		
		self.localsettings = self.localsettings
		self.userlist = userlist
		
		self.RefreshUsers()
	
	def Popup(self, ID):
		
		popupmenu = wx.Menu()
		
		add = wx.MenuItem(popupmenu, ADD_USER, self.GetLabel("addlabel"))
		add.SetBitmap(wx.Bitmap("icons/new.png"))
		popupmenu.AppendItem(add)
		wx.EVT_MENU(popupmenu, ADD_USER, self.AddUser)
		
		if self.userlist.GetSelection() > -1:
			
			edit = wx.MenuItem(popupmenu, EDIT_USER, self.GetLabel("editlabel"))
			edit.SetBitmap(wx.Bitmap("icons/edit.png"))
			popupmenu.AppendItem(edit)
			wx.EVT_MENU(popupmenu, EDIT_USER, self.EditUser)
			
			delete = wx.MenuItem(popupmenu, DELETE_USER, self.GetLabel("deletelabel"))
			delete.SetBitmap(wx.Bitmap("icons/delete.png"))
			popupmenu.AppendItem(delete)
			wx.EVT_MENU(popupmenu, DELETE_USER, self.DeleteUser)
		
		popupmenu.AppendSeparator()
		
		refresh = wx.MenuItem(popupmenu, REFRESH_USERS, self.GetLabel("refreshlabel"))
		refresh.SetBitmap(wx.Bitmap("icons/refresh.png"))
		popupmenu.AppendItem(refresh)
		wx.EVT_MENU(popupmenu, REFRESH_USERS, self.RefreshUsers)
		
		self.PopupMenu(popupmenu)
	
	def AddUser(self, ID):
		
		self.EditUserDialog()
	
	def EditUser(self, ID):
		
		listboxid = self.userlist.GetSelection()
		
		userid = self.users[listboxid]
		
		action = "SELECT * FROM user WHERE ID = " + str(userid)
		results = db.SendSQL(action, self.localsettings.dbconnection)
		
		self.EditUserDialog(results[0])
	
	def EditUserDialog(self, userdata=False):
		
		busy = wx.BusyCursor()
		
		action = "SELECT Position FROM user ORDER BY Position"
		results = db.SendSQL(action, self.localsettings.dbconnection)
		
		positions = []
		
		for a in results:
			
			if positions.__contains__(a[0]) == False:
				
				positions.append(a[0])
		
		dialog = wx.Dialog(self, -1, self.GetLabel("edituserlabel"))
		
		dialogsizer = wx.BoxSizer(wx.VERTICAL)
		
		panel = wx.Panel(dialog)
		
		panel.userdata = userdata
		
		panel.localsettings = self.localsettings
		
		permissionssizer = wx.BoxSizer(wx.VERTICAL)
		
		permissionssizer.Add(wx.StaticText(panel, -1, "", size=(-1,10)), 0, wx.EXPAND)
		
		inputsizer = wx.BoxSizer(wx.HORIZONTAL)
		
		namesizer = wx.BoxSizer(wx.VERTICAL)
		
		namelabel = wx.StaticText(panel, -1, self.GetLabel("namelabel") + ":")
		font = namelabel.GetFont()
		font.SetPointSize(font.GetPointSize() - 2)
		namelabel.SetFont(font)
		namesizer.Add(namelabel, 0, wx.ALIGN_LEFT)
		
		nameentry = wx.TextCtrl(panel, -1, "", size=(150,-1))
		namesizer.Add(nameentry, 1, wx.EXPAND)
		
		inputsizer.Add(namesizer, 0, wx.EXPAND)
		
		passwordsizer = wx.BoxSizer(wx.VERTICAL)
		
		passwordlabel = wx.StaticText(panel, -1, miscmethods.NoWrap(" " + self.GetLabel("passwordlabel") + ":"))
		passwordlabel.SetFont(font)
		passwordsizer.Add(passwordlabel, 0, wx.ALIGN_LEFT)
		
		passwordentry = wx.TextCtrl(panel, -1, "", size=(150,-1))
		passwordsizer.Add(passwordentry, 1, wx.EXPAND)
		
		inputsizer.Add(passwordsizer, 0, wx.EXPAND)
		
		positionsizer = wx.BoxSizer(wx.VERTICAL)
		
		positionlabel = wx.StaticText(panel, -1, miscmethods.NoWrap(" " + self.GetLabel("positionlabel") + ":"))
		positionlabel.SetFont(font)
		positionsizer.Add(positionlabel, 0, wx.ALIGN_LEFT)
		
		positionentry = wx.ComboBox(panel, -1, "", choices=positions)
		positionsizer.Add(positionentry, 1, wx.EXPAND)
		
		inputsizer.Add(positionsizer, 0, wx.EXPAND)
		
		permissionssizer.Add(inputsizer, 0, wx.EXPAND)
		
		permissionssizer.Add(wx.StaticText(panel, -1, "", size=(-1,10)), 0, wx.EXPAND)
		
		permissionsnotebook = wx.Notebook(panel)
		
		clientpermissions = ClientSettingsPanel(permissionsnotebook, self.GetLabel("clientslabel"))
		permissionsnotebook.AddPage(clientpermissions, self.GetLabel("clientslabel"), select=True)
		
		animalpermissions = GenericSettingsPanel(permissionsnotebook, self.GetLabel("animalslabel"))
		permissionsnotebook.AddPage(animalpermissions, self.GetLabel("animalslabel"), select=False)
		
		appointmentpermissions = AppointmentSettingsPanel(permissionsnotebook, self.GetLabel("appointmentslabel"))
		permissionsnotebook.AddPage(appointmentpermissions, self.GetLabel("appointmentslabel"), select=False)
		
		medicationpermissions = GenericSettingsPanel(permissionsnotebook, self.GetLabel("medicationlabel"))
		permissionsnotebook.AddPage(medicationpermissions, self.GetLabel("medicationlabel"), select=False)
		
		procedurepermissions = GenericSettingsPanel(permissionsnotebook, self.GetLabel("procedureslabel"))
		permissionsnotebook.AddPage(procedurepermissions, self.GetLabel("procedureslabel"), select=False)
		
		lookuppermissions = GenericSettingsPanel(permissionsnotebook, self.GetLabel("lookupslabel"))
		permissionsnotebook.AddPage(lookuppermissions, self.GetLabel("lookupslabel"), select=False)
		
		formpermissions = GenericSettingsPanel(permissionsnotebook, self.GetLabel("formslabel"))
		permissionsnotebook.AddPage(formpermissions, self.GetLabel("formslabel"), select=False)
		
		userpermissions = UserSettingsPanel(permissionsnotebook, self.GetLabel("userslabel"))
		permissionsnotebook.AddPage(userpermissions, self.GetLabel("userslabel"), select=False)
		
		diarypermissions = DiarySettingsPanel(permissionsnotebook, self.GetLabel("diarylabel"))
		permissionsnotebook.AddPage(diarypermissions, self.GetLabel("diarylabel"), select=False)
		
		miscpermissions = MiscSettingsPanel(permissionsnotebook, self.GetLabel("misclabel"))
		permissionsnotebook.AddPage(miscpermissions, self.GetLabel("misclabel"), select=False)
		
		permissionssizer.Add(permissionsnotebook, 1, wx.EXPAND)
		
		tickallsizer = wx.BoxSizer(wx.HORIZONTAL)
		
		untickallbitmap = wx.Bitmap("icons/reset.png")
		untickallbutton = wx.BitmapButton(panel, -1, untickallbitmap)
		untickallbutton.SetToolTipString(self.GetLabel("resetlabel"))
		untickallbutton.Bind(wx.EVT_BUTTON, self.UnTickAll)
		tickallsizer.Add(untickallbutton, 0, wx.EXPAND)
		
		tickallbitmap = wx.Bitmap("icons/tickall.png")
		tickallbutton = wx.BitmapButton(panel, -1, tickallbitmap)
		tickallbutton.SetToolTipString(self.GetLabel("tickalltooltip"))
		tickallbutton.Bind(wx.EVT_BUTTON, self.TickAll)
		tickallsizer.Add(tickallbutton, 0, wx.EXPAND)
		
		tickallsizer.Add(wx.StaticText(panel, -1, ""), 1, wx.EXPAND)
		
		submitbitmap = wx.Bitmap("icons/submit.png")
		submitbutton = wx.BitmapButton(panel, -1, submitbitmap)
		submitbutton.SetToolTipString(self.GetLabel("submitlabel"))
		submitbutton.Bind(wx.EVT_BUTTON, self.SubmitUser)
		tickallsizer.Add(submitbutton, 0, wx.EXPAND)
		
		permissionssizer.Add(tickallsizer, 0, wx.EXPAND)
		
		panel.SetSizer(permissionssizer)
		
		panel.clientpermissions = clientpermissions
		panel.animalpermissions = animalpermissions
		panel.appointmentpermissions = appointmentpermissions
		panel.medicationpermissions = medicationpermissions
		panel.procedurepermissions = procedurepermissions
		panel.lookuppermissions = lookuppermissions
		panel.formpermissions = formpermissions
		panel.userpermissions = userpermissions
		panel.diarypermissions = diarypermissions
		panel.miscpermissions = miscpermissions
		
		panel.nameentry = nameentry
		panel.passwordentry = passwordentry
		panel.positionentry = positionentry
		
		dialogsizer.Add(panel, 1, wx.EXPAND)
		
		dialog.SetSizer(dialogsizer)
		
		if userdata != False:
			
			panel.nameentry.SetValue(userdata[1])
			panel.passwordentry.SetValue(userdata[2])
			panel.positionentry.SetValue(userdata[3])
			
			changelog = userdata[4].split("$")
			
			if changelog[0][0] == "1":
				panel.clientpermissions.edit.SetValue(True)
			else:
				panel.clientpermissions.edit.SetValue(False)
			if changelog[0][1] == "1":
				panel.clientpermissions.delete.SetValue(True)
			else:
				panel.clientpermissions.delete.SetValue(False)
			if changelog[0][2] == "1":
				panel.clientpermissions.editfinances.SetValue(True)
			else:
				panel.clientpermissions.editfinances.SetValue(False)
			
			if changelog[1][0] == "1":
				panel.animalpermissions.edit.SetValue(True)
			else:
				panel.animalpermissions.edit.SetValue(False)
			if changelog[1][1] == "1":
				panel.animalpermissions.delete.SetValue(True)
			else:
				panel.animalpermissions.delete.SetValue(False)
			
			if changelog[2][0] == "1":
				panel.appointmentpermissions.edit.SetValue(True)
			else:
				panel.appointmentpermissions.edit.SetValue(False)
			if changelog[2][1] == "1":
				panel.appointmentpermissions.delete.SetValue(True)
			else:
				panel.appointmentpermissions.delete.SetValue(False)
			if changelog[2][2] == "1":
				panel.appointmentpermissions.vetform.SetValue(True)
			else:
				panel.appointmentpermissions.vetform.SetValue(False)
			
			if changelog[3][0] == "1":
				panel.medicationpermissions.edit.SetValue(True)
			else:
				panel.medicationpermissions.edit.SetValue(False)
			if changelog[3][1] == "1":
				panel.medicationpermissions.delete.SetValue(True)
			else:
				panel.medicationpermissions.delete.SetValue(False)
			
			if changelog[4][0] == "1":
				panel.procedurepermissions.edit.SetValue(True)
			else:
				panel.procedurepermissions.edit.SetValue(False)
			if changelog[4][1] == "1":
				panel.procedurepermissions.delete.SetValue(True)
			else:
				panel.procedurepermissions.delete.SetValue(False)
			
			if changelog[5][0] == "1":
				panel.lookuppermissions.edit.SetValue(True)
			else:
				panel.lookuppermissions.edit.SetValue(False)
			if changelog[5][1] == "1":
				panel.lookuppermissions.delete.SetValue(True)
			else:
				panel.lookuppermissions.delete.SetValue(False)
			
			if changelog[6][0] == "1":
				panel.formpermissions.edit.SetValue(True)
			else:
				panel.formpermissions.edit.SetValue(False)
			if changelog[6][1] == "1":
				panel.formpermissions.delete.SetValue(True)
			else:
				panel.formpermissions.delete.SetValue(False)
			
			if changelog[7][0] == "1":
				panel.userpermissions.edit.SetValue(True)
			else:
				panel.userpermissions.edit.SetValue(False)
			if changelog[7][1] == "1":
				panel.userpermissions.delete.SetValue(True)
			else:
				panel.userpermissions.delete.SetValue(False)
			if changelog[7][2] == "1":
				panel.userpermissions.editrota.SetValue(True)
			else:
				panel.userpermissions.editrota.SetValue(False)
			
			if changelog[8][0] == "1":
				panel.miscpermissions.toolbar.SetValue(True)
			else:
				panel.miscpermissions.toolbar.SetValue(False)
			if changelog[8][1] == "1":
				panel.miscpermissions.changelog.SetValue(True)
			else:
				panel.miscpermissions.changelog.SetValue(False)
			if changelog[8][2] == "1":
				panel.miscpermissions.editsettings.SetValue(True)
			else:
				panel.miscpermissions.editsettings.SetValue(False)
			if changelog[8][3] == "1":
				panel.miscpermissions.multiplepanels.SetValue(True)
			else:
				panel.miscpermissions.multiplepanels.SetValue(False)
			if changelog[8][4] == "1":
				panel.miscpermissions.asmsync.SetValue(True)
			else:
				panel.miscpermissions.asmsync.SetValue(False)
			
			if changelog[9][0] == "1":
				panel.diarypermissions.adddiarynotes.SetValue(True)
			else:
				panel.diarypermissions.adddiarynotes.SetValue(False)
			if changelog[9][1] == "1":
				panel.diarypermissions.editdiarynotes.SetValue(True)
			else:
				panel.diarypermissions.editdiarynotes.SetValue(False)
			if changelog[9][2] == "1":
				panel.diarypermissions.deletediarynotes.SetValue(True)
			else:
				panel.diarypermissions.deletediarynotes.SetValue(False)
		
		dialog.SetSize((800,400))
		
		del busy
		
		dialog.ShowModal()
	
	def TickAll(self, ID):
		
		panel = ID.GetEventObject().GetParent()
		
		panel.clientpermissions.edit.SetValue(True)
		panel.clientpermissions.delete.SetValue(True)
		panel.clientpermissions.editfinances.SetValue(True)
		
		panel.animalpermissions.edit.SetValue(True)
		panel.animalpermissions.delete.SetValue(True)
		
		panel.appointmentpermissions.edit.SetValue(True)
		panel.appointmentpermissions.delete.SetValue(True)
		panel.appointmentpermissions.vetform.SetValue(True)
		
		panel.medicationpermissions.edit.SetValue(True)
		panel.medicationpermissions.delete.SetValue(True)
		
		panel.procedurepermissions.edit.SetValue(True)
		panel.procedurepermissions.delete.SetValue(True)
		
		panel.lookuppermissions.edit.SetValue(True)
		panel.lookuppermissions.delete.SetValue(True)
		
		panel.formpermissions.edit.SetValue(True)
		panel.formpermissions.delete.SetValue(True)
		
		panel.userpermissions.edit.SetValue(True)
		panel.userpermissions.delete.SetValue(True)
		panel.userpermissions.editrota.SetValue(True)
		
		panel.miscpermissions.toolbar.SetValue(True)
		panel.miscpermissions.changelog.SetValue(True)
		panel.miscpermissions.editsettings.SetValue(True)
		panel.miscpermissions.multiplepanels.SetValue(True)
		panel.miscpermissions.asmsync.SetValue(True)
		
		panel.diarypermissions.adddiarynotes.SetValue(True)
		panel.diarypermissions.editdiarynotes.SetValue(True)
		panel.diarypermissions.deletediarynotes.SetValue(True)
	
	def UnTickAll(self, ID):
		
		panel = ID.GetEventObject().GetParent()
		
		panel.clientpermissions.edit.SetValue(False)
		panel.clientpermissions.delete.SetValue(False)
		panel.clientpermissions.editfinances.SetValue(False)
		
		panel.animalpermissions.edit.SetValue(False)
		panel.animalpermissions.delete.SetValue(False)
		
		panel.appointmentpermissions.edit.SetValue(False)
		panel.appointmentpermissions.delete.SetValue(False)
		panel.appointmentpermissions.vetform.SetValue(False)
		
		panel.medicationpermissions.edit.SetValue(False)
		panel.medicationpermissions.delete.SetValue(False)
		
		panel.procedurepermissions.edit.SetValue(False)
		panel.procedurepermissions.delete.SetValue(False)
		
		panel.lookuppermissions.edit.SetValue(False)
		panel.lookuppermissions.delete.SetValue(False)
		
		panel.formpermissions.edit.SetValue(False)
		panel.formpermissions.delete.SetValue(False)
		
		panel.userpermissions.edit.SetValue(False)
		panel.userpermissions.delete.SetValue(False)
		panel.userpermissions.editrota.SetValue(False)
		
		panel.miscpermissions.toolbar.SetValue(False)
		panel.miscpermissions.changelog.SetValue(False)
		panel.miscpermissions.editsettings.SetValue(False)
		panel.miscpermissions.multiplepanels.SetValue(False)
		panel.miscpermissions.asmsync.SetValue(False)
		
		panel.diarypermissions.adddiarynotes.SetValue(False)
		panel.diarypermissions.editdiarynotes.SetValue(False)
		panel.diarypermissions.deletediarynotes.SetValue(False)
	
	def RefreshUsers(self, ID=False):
		
		self.userlist.Clear()
		self.users = []
		
		action = "SELECT * FROM user ORDER BY Name;"
		results = db.SendSQL(action, self.localsettings.dbconnection)
		
		for a in results:
			
			self.users.append(a[0])
			self.userlist.Append(a[1] + " - " + a[3])
		
		self.userlist.SetSelection(-1)
	
	def SubmitUser(self, ID):
		
		panel = ID.GetEventObject().GetParent()
		
		username = panel.nameentry.GetValue()
		userpassword = panel.passwordentry.GetValue()
		position = panel.positionentry.GetValue()
		
		if panel.clientpermissions.edit.GetValue() == True:
			permissions = "1"
		else:
			permissions = "0"
		if panel.clientpermissions.delete.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.clientpermissions.editfinances.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.animalpermissions.edit.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.animalpermissions.delete.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.appointmentpermissions.edit.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.appointmentpermissions.delete.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.appointmentpermissions.vetform.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.medicationpermissions.edit.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.medicationpermissions.delete.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.procedurepermissions.edit.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.procedurepermissions.delete.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.lookuppermissions.edit.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.lookuppermissions.delete.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.formpermissions.edit.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.formpermissions.delete.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.userpermissions.edit.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.userpermissions.delete.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.userpermissions.editrota.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		if panel.miscpermissions.toolbar.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.miscpermissions.changelog.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.miscpermissions.editsettings.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.miscpermissions.multiplepanels.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.miscpermissions.asmsync.GetValue() == True:
			permissions = permissions + "1$"
		else:
			permissions = permissions + "0$"
		
		
		if panel.diarypermissions.adddiarynotes.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.diarypermissions.editdiarynotes.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		if panel.diarypermissions.deletediarynotes.GetValue() == True:
			permissions = permissions + "1"
		else:
			permissions = permissions + "0"
		
		if panel.userdata == False:
			
			userid = False
			
		else:
			
			userid = panel.userdata[0]
		
		dbmethods.WriteToUserTable(self.localsettings.dbconnection, userid, username, userpassword, position, permissions)
		
		self.RefreshUsers()
		
		panel.GetParent().Close()
	
	def DeleteUser(self, ID):
		
		listboxid = self.userlist.GetSelection()
		
		userid = self.users[listboxid]
		
		action = "SELECT * FROM user WHERE ID = " + str(userid) + ";"
		results = db.SendSQL(action, self.localsettings.dbconnection)
		
		self.selecteduserid = userid
		
		if miscmethods.ConfirmMessage(self.GetLabel("userdeletemessage")) == True:
			
			action = "DELETE FROM user WHERE ID = " + str(self.selecteduserid) + ";"
			results = db.SendSQL(action, self.localsettings.dbconnection)
			
			self.RefreshUsers()

class EditStaffRota(wx.Panel):
	
	def GetLabel(self, field):
		
		return  self.localsettings.dictionary[field][self.localsettings.language]
	
	def __init__(self, notebook, localsettings):
		
		self.localsettings = localsettings
		
		self.pagetitle = miscmethods.GetPageTitle(notebook, self.GetLabel("editrotapagetitle"))
		
		wx.Panel.__init__(self, notebook)
		
		topsizer = wx.BoxSizer(wx.VERTICAL)
		
		action = "SELECT Name FROM user WHERE Position LIKE \"%Vet%\" ORDER BY Name"
		results = db.SendSQL(action, localsettings.dbconnection)
		
		
		vets = []
		for a in results:
			vets.append(a[0])
		
		toolssizer = wx.FlexGridSizer(rows=1)
		
		vetlabel = wx.StaticText(self, -1, self.GetLabel("vetlabel") + ": ")
		toolssizer.Add(vetlabel, 0, wx.ALIGN_CENTER)
		
		vetentry = wx.ComboBox(self, -1, "", choices=vets)
		toolssizer.Add(vetentry, 1, wx.EXPAND)
		
		timeonlabel = wx.StaticText(self, -1, " " + self.GetLabel("timeonlabel") + ": ")
		toolssizer.Add(timeonlabel, 0, wx.ALIGN_CENTER)
		
		timeonentry = wx.TextCtrl(self, -1, "")
		toolssizer.Add(timeonentry, 1, wx.EXPAND)
		
		timeofflabel = wx.StaticText(self, -1, " " + self.GetLabel("timeofflabel") + ": ")
		toolssizer.Add(timeofflabel, 0, wx.ALIGN_CENTER)
		
		timeoffentry = wx.TextCtrl(self, -1, "")
		toolssizer.Add(timeoffentry, 1, wx.EXPAND)
		
		operatingcheckbox = wx.CheckBox(self, -1, " " + self.GetLabel("operatinglabel") + ": ")
		toolssizer.Add(operatingcheckbox, 0, wx.ALIGN_CENTER)
		
		#spacer2 = wx.StaticText(self, -1, "")
		#toolssizer.Add(spacer2, 2, wx.EXPAND)
		
		for a in (1, 3, 5):
			toolssizer.AddGrowableCol(a)
		
		submitbitmap = wx.Bitmap("icons/submit.png")
		submitbutton = wx.BitmapButton(self, -1, submitbitmap)
		submitbutton.Bind(wx.EVT_BUTTON, self.Submit)
		toolssizer.Add(submitbutton, 0, wx.ALIGN_CENTER)
		
		topsizer.Add(toolssizer, 0, wx.EXPAND)
		
		spacer = wx.StaticText(self, -1, "")
		topsizer.Add(spacer, 0, wx.EXPAND)
		
		listssizer = wx.BoxSizer(wx.HORIZONTAL)
		
		datesizer = wx.BoxSizer(wx.VERTICAL)
		
		datelabel = wx.StaticText(self, -1, self.GetLabel("datelabel") + ":")
		datesizer.Add(datelabel, 0, wx.ALIGN_LEFT)
		
		datepickersizer = wx.BoxSizer(wx.HORIZONTAL)
		#self.dateentry = wx.DatePickerCtrl(self, -1, size=(200,-1))
		self.dateentry = customwidgets.DateCtrl(self, self.localsettings)
		#self.dateentry.Bind(wx.EVT_DATE_CHANGED, self.RefreshRota)
		datepickersizer.Add(self.dateentry, 1, wx.EXPAND)
		
		refreshbitmap = wx.Bitmap("icons/refresh.png")
		refreshbutton = wx.BitmapButton(self, -1, refreshbitmap)
		refreshbutton.Bind(wx.EVT_BUTTON, self.RefreshRota)
		datepickersizer.Add(refreshbutton, 0, wx.wx.EXPAND)
		
		datesizer.Add(datepickersizer, 0, wx.EXPAND)
		
		listssizer.Add(datesizer, 1, wx.EXPAND)
		
		spacer1 = wx.StaticText(self, -1, "", size=(20,-1))
		listssizer.Add(spacer1, 0, wx.EXPAND)
		
 		summarysizer = wx.BoxSizer(wx.VERTICAL)
		
		staffsummarylabel = wx.StaticText(self, -1, self.GetLabel("staffsummarylabel") + ":")
		summarysizer.Add(staffsummarylabel, 0, wx.ALIGN_LEFT)
		
		staffsummarylistbox = customwidgets.StaffSummaryListbox(self, self.localsettings)
		staffsummarylistbox.Bind(wx.EVT_LISTBOX, self.SlotSelected)
		summarysizer.Add(staffsummarylistbox, 1, wx.EXPAND)
		
		summarybuttonssizer = wx.BoxSizer(wx.HORIZONTAL)
		
		editbitmap = wx.Bitmap("icons/edit.png")
		editbutton = wx.BitmapButton(self, -1, editbitmap)
		editbutton.Bind(wx.EVT_BUTTON, self.Edit)
		summarybuttonssizer.Add(editbutton, 0, wx.ALIGN_LEFT)
		
		deletebitmap = wx.Bitmap("icons/delete.png")
		deletebutton = wx.BitmapButton(self, -1, deletebitmap)
		deletebutton.Bind(wx.EVT_BUTTON, self.Delete)
		summarybuttonssizer.Add(deletebutton, 0, wx.ALIGN_LEFT)
		
		summarysizer.Add(summarybuttonssizer, 0, wx.ALIGN_LEFT)
		
		listssizer.Add(summarysizer, 2, wx.EXPAND)
		
		spacer3 = wx.StaticText(self, -1, "", size=(20,-1))
		listssizer.Add(spacer3, 0, wx.EXPAND)
		
		dayplansizer = wx.BoxSizer(wx.VERTICAL)
		
		dayplanlabel = wx.StaticText(self, -1,  self.GetLabel("dayplanlabel") + ":")
		dayplansizer.Add(dayplanlabel, 0, wx.ALIGN_LEFT)
		
		dayplan = wx.html.HtmlWindow(self)
		dayplansizer.Add(dayplan, 1, wx.EXPAND)
		
		listssizer.Add(dayplansizer, 3, wx.EXPAND)
		
		topsizer.Add(listssizer, 1, wx.EXPAND)
		
		self.SetSizer(topsizer)
		
		self.vetentry = vetentry
		self.timeonentry = timeonentry
		self.timeoffentry = timeoffentry
		self.staffsummarylistbox = staffsummarylistbox
		self.dayplan = dayplan
		self.operatingcheckbox = operatingcheckbox
		self.staffsummarylistbox.RefreshList()
		self.GenerateDayPlan()
	
	def Submit(self, ID):
		
		success = False
		date = self.dateentry.GetValue()
		date = miscmethods.GetSQLDateFromWXDate(date)
		vet = self.vetentry.GetValue()
		timeon = self.timeonentry.GetValue()
		timeoff = self.timeoffentry.GetValue()
		if self.operatingcheckbox.GetValue() == True:
			operating = 1
		else:
			operating = 0
		
		if vet == "":
			
			miscmethods.ShowMessage(self.GetLabel("novetnamemessage"))
			
		else:
		
			if miscmethods.ValidateTime(timeon) == True and miscmethods.ValidateTime(timeoff) == True:
				timeonint = int(timeon[:2] + timeon[3:5])
				timeoffint = int(timeoff[:2] + timeoff[3:5])
				if timeonint < timeoffint:
					success = True
				else:
					miscmethods.ShowMessage(self.GetLabel("vetfinishedbeforestartingmessage"))
			
			if success == True:
				
				starttimesql = timeon[:2] + ":" + timeon[3:5] + ":00"
				offtimesql = timeoff[:2] + ":" + timeoff[3:5] + ":00"
				
				action = "SELECT ID FROM staff WHERE DATE = \"" + date + "\" AND Vet = \"" + vet + "\" AND ( \"" + starttimesql + "\" BETWEEN TimeOn AND TimeOff OR \"" + offtimesql + "\" BETWEEN TimeOn AND TimeOff OR TimeOn BETWEEN \"" + starttimesql + "\" AND \"" + offtimesql + "\" OR TimeOff BETWEEN \"" + starttimesql + "\" AND \"" + offtimesql + "\" )"
				results = db.SendSQL(action, self.localsettings.dbconnection)
				
				if len(results) > 0:
					miscmethods.ShowMessage(self.GetLabel("vettwoplacesatoncemessage"))
				else:
					dbmethods.WriteToStaffTable(self.localsettings.dbconnection, date, vet, timeon, timeoff, operating)
					
					self.RefreshRota()
			else:
				miscmethods.ShowMessage(self.GetLabel("invalidtimemessage"))
	
	def Delete(self, ID):
		
		listboxid = self.staffsummarylistbox.GetSelection()
		staffid = self.staffsummarylistbox.htmllist[listboxid][0]
		
		action = "DELETE FROM staff WHERE ID = " + str(staffid)
		db.SendSQL(action, self.localsettings.dbconnection)
		
		self.RefreshRota()
	
	def GenerateDayPlan(self, ID=False):
		
		date = self.dateentry.GetValue()
		sqldate = miscmethods.GetSQLDateFromWXDate(date)
		
		output = miscmethods.GenerateDayPlan(self.localsettings, sqldate, 30)
		self.dayplan.SetPage(output)
	
	def RefreshRota(self, ID=False):
		
		self.staffsummarylistbox.RefreshList()
		self.GenerateDayPlan()
	
	def Edit(self, ID):
		
		listboxid = self.staffsummarylistbox.GetSelection()
		staffid = self.staffsummarylistbox.htmllist[listboxid][0]
		
		success = False
		date = self.dateentry.GetValue()
		date = miscmethods.GetSQLDateFromWXDate(date)
		vet = self.vetentry.GetValue()
		timeon = self.timeonentry.GetValue()
		timeoff = self.timeoffentry.GetValue()
		if self.operatingcheckbox.GetValue() == True:
			operating = 1
		else:
			operating = 0
		
		if miscmethods.ValidateTime(timeon) == True and miscmethods.ValidateTime(timeoff) == True:
			timeonint = int(timeon[:2] + timeon[3:5])
			timeoffint = int(timeoff[:2] + timeoff[3:5])
			if timeonint < timeoffint:
				success = True
			else:
				miscmethods.ShowMessage(self.GetLabel("vetfinishedbeforestartingmessage"))
		
		if success == True:
			
			dbmethods.WriteToStaffTable(self.localsettings.dbconnection, date, vet, timeon, timeoff, operating, staffid)
			
			self.RefreshRota()
		else:
			miscmethods.ShowMessage(self.GetLabel("invalidtimemessage"))
	
	def SlotSelected(self, ID):
		
		listboxid = self.staffsummarylistbox.GetSelection()
		staffdata = self.staffsummarylistbox.htmllist[listboxid]
		self.vetentry.SetValue(staffdata[1])
		self.timeonentry.SetValue(staffdata[3])
		self.timeoffentry.SetValue(staffdata[4])
		if staffdata[5] == 0:
			self.operatingcheckbox.SetValue(False)
		else:
			self.operatingcheckbox.SetValue(True)