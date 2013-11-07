#!/usr/bin/env python

"""A tool to replicate tank project configs to various projects.

"""

# ----------------------------------------------------------------------------------------
# Licence
# ----------------------------------------------------------------------------------------
"""
Tool to replicate Sgtk project configs to other projects.
Copyright 2013 Cluster Studio S.C.  All rights reserved

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

 * Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in
   the documentation and/or other materials provided with the
   distribution.

 * The name "Cluster Studio" or the names of its contributors 
   may NOT be used to endorse or promote products derived from this
   software without specific prior written permission from Cluster Studio.

Disclaimer: THIS SOFTWARE IS PROVIDED BY CLUSTER STUDIO AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE, NONINFRINGEMENT AND TITLE ARE DISCLAIMED.
IN NO EVENT SHALL CLUSTER STUDIO, THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND BASED ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
"""


# ----------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------
import sys
import yaml
import os
import subprocess
import traceback

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTime

from modules.csTankReplicator_form import Ui_TankReplicator
from modules.get_projects_list import _get_projects_list
from modules.sync_job import _sync_job
from modules.build_path import _build_path


# ----------------------------------------------------------------------------------------
# Globals 
# ----------------------------------------------------------------------------------------

class csTankReplicator(QtGui.QMainWindow):
	def __init__(self, parent = None):

		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_TankReplicator()
		self.ui.setupUi(self)

		self.setWindowIcon(QtGui.QIcon('resources' + os.sep + 'csTankReplicator_icon.png'))

		QtCore.QObject.connect(self.ui.replicateButton, QtCore.SIGNAL("clicked()"),self._replicateConfig)

		self.ui.actionAbout.triggered.connect(self._about)


		for project in projectsDic:

			item = QtGui.QListWidgetItem(project)

			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
			item.setCheckState(QtCore.Qt.Unchecked)

			self.ui.destProjectsWidget.addItem(item)

			self.ui.oriProjectList.addItem(project)
			self.ui.oriProjectList.setEditText('')


		for job in sorted(syncJobs):

			item = QtGui.QListWidgetItem(job)

			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
			item.setCheckState(QtCore.Qt.Unchecked)

			self.ui.syncAreasList.addItem(item)


	def _syncJob(self, job):

		_sync_job(job)


	def _about(self):

		msg = '%(App)s \n%(Info)s \n\n %(Copy)s \n %(Web)s \n\n %(Developer)s \n %(DevEmail)s'

		msg = msg % {'App': 'Tank Replicator.',
					 'Info': 'A tool to replicate tank project configs \nto various projects.',
					 'Copy': 'Copyright(c) Cluster Studio 2013.', 
					 'Web': 'http://www.clusterstudio.com',
					 'Developer': 'Developer: Hasiel Alvarez',
					 'DevEmail': 'hasielhassan@clusterstudio.com'}

		QtGui.QMessageBox.about(self, 'About...', msg)
      
	def _replicateConfig(self):

		try:
			syncAreas = []
			for index in xrange(self.ui.syncAreasList.count()):
				item = self.ui.syncAreasList.item(index)
				if item.checkState() == 2:
					syncAreas.append(str(item.text()))

			selectedProjects = []
			for index in xrange(self.ui.destProjectsWidget.count()):
				item = self.ui.destProjectsWidget.item(index)
				if item.checkState() == 2:
					selectedProjects.append(str(item.text()))

			allProjects = [str(self.ui.oriProjectList.itemText(i)) for i in range(self.ui.oriProjectList.count())]


			if self.ui.oriProjectList.currentText() == '':

				QtGui.QMessageBox.information(self, 
											  'Info...', 
											  'No original projects selected!!', 
											  QtGui.QMessageBox.Ok)

			elif not self.ui.oriProjectList.currentText() in allProjects:

				QtGui.QMessageBox.information(self, 
											  'Info...', 
											  "The text for original project, don't correspond to a valid project name!!", 
											  QtGui.QMessageBox.Ok)

			elif len(selectedProjects) == 0:

				QtGui.QMessageBox.information(self, 
											  'Info...', 
											  'No target projects selected!!', 
											  QtGui.QMessageBox.Ok)

			elif len(syncAreas) == 0:

				QtGui.QMessageBox.information(self, 
											  'Info...', 
											  'No sync areas selected!!', 
											  QtGui.QMessageBox.Ok)

			else:

				reply = QtGui.QMessageBox.question(self, 'Confirmation...', 'Are you sure?', 
												   QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)

				if reply == QtGui.QMessageBox.Yes:

					#Create Progressbar dialog
					progress = QtGui.QProgressDialog("Please Wait", 'Cancel', 0, 100, win)
					progress.setCancelButton(None)
					progress.setWindowModality(QtCore.Qt.WindowModal)
					progress.setAutoReset(True)
					progress.setAutoClose(True)
					progress.setMinimum(0)
					progress.setMaximum(100)
					progress.resize(300,150)
					progress.setWindowTitle("Syncing Projects...")
					progress.show()

					rsyncJobs = []

					originalProject = str(self.ui.oriProjectList.currentText())

					progress.setValue(1)
					progress.setLabelText("Creating job list...")

					for project in selectedProjects:

						for area in syncAreas:

							job = {'name': area}
							job['project'] = project
							job['from'] = _build_path(originalProject, syncJobs[area]['path'], 'origin')							
							job['to'] =  _build_path(project, syncJobs[area]['path'], 'target')
							job['exclusions'] = syncJobs[area]['exclutions']
							rsyncJobs.append(job)

					ProcecedJobs = 0
					for job in rsyncJobs:

						progress.setLabelText("Current project..." +
											  '\n' + 
											  job['project'] + 
											  '\n\n' + 
											  "Current Folder... " + 
											  '\n' + 
											  job['name'])

						progressValue = int(round(((float(ProcecedJobs) / float(len(rsyncJobs))) * 100), 0))
						progress.setValue(progressValue)
						self._syncJob(job)
						ProcecedJobs += 1

					progress.setValue(100)
					progress.hide()
					QtGui.QMessageBox.information(self, 
												  'Info...', 
												  'All projects were processed successfully!!', 
												  QtGui.QMessageBox.Ok)

		except Exception, e:
			Error = traceback.format_exc()
			progress.hide()
			QtGui.QMessageBox.critical(self, 'Error...', str(e) + '\n\n' + str(Error), QtGui.QMessageBox.Ok)


       
if __name__ == "__main__":

	projectsDic = _get_projects_list()

	config_file = open('modules/jobs_config.yml', 'r')
	config_dict = yaml.load(config_file.read())
	config_file.close()

	syncJobs = config_dict['Jobs']
	LocalServerPath = config_dict['Paths']['Original Projects Path']
	RemoteServerPath = config_dict['Paths']['Target Projects Path']

	app = QtGui.QApplication(sys.argv)
	win = csTankReplicator()
	win.show()
	sys.exit(app.exec_())