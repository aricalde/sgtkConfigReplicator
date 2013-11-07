# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csTankReplicator_form.ui'
#
# Created: Wed Nov  6 20:35:34 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TankReplicator(object):
    def setupUi(self, TankReplicator):
        TankReplicator.setObjectName(_fromUtf8("TankReplicator"))
        TankReplicator.resize(410, 470)
        TankReplicator.setMinimumSize(QtCore.QSize(410, 470))
        TankReplicator.setMaximumSize(QtCore.QSize(410, 470))
        self.centralwidget = QtGui.QWidget(TankReplicator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(410, 423))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalWidget = QtGui.QWidget(self.centralwidget)
        self.verticalWidget.setEnabled(True)
        self.verticalWidget.setGeometry(QtCore.QRect(4, 2, 401, 421))
        self.verticalWidget.setMinimumSize(QtCore.QSize(291, 421))
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 800))
        self.verticalWidget.setStyleSheet(_fromUtf8("alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.oriProjectList = QtGui.QComboBox(self.verticalWidget)
        self.oriProjectList.setEditable(True)
        self.oriProjectList.setObjectName(_fromUtf8("oriProjectList"))
        self.verticalLayout.addWidget(self.oriProjectList)
        self.label_2 = QtGui.QLabel(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.destProjectsWidget = QtGui.QListWidget(self.verticalWidget)
        self.destProjectsWidget.setObjectName(_fromUtf8("destProjectsWidget"))
        self.verticalLayout.addWidget(self.destProjectsWidget)
        self.label_3 = QtGui.QLabel(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.syncAreasList = QtGui.QListWidget(self.verticalWidget)
        self.syncAreasList.setObjectName(_fromUtf8("syncAreasList"))
        self.verticalLayout.addWidget(self.syncAreasList)
        self.replicateButton = QtGui.QPushButton(self.verticalWidget)
        self.replicateButton.setObjectName(_fromUtf8("replicateButton"))
        self.verticalLayout.addWidget(self.replicateButton)
        TankReplicator.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TankReplicator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        TankReplicator.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(TankReplicator)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        TankReplicator.setStatusBar(self.statusBar)
        self.actionAbout = QtGui.QAction(TankReplicator)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(TankReplicator)
        QtCore.QMetaObject.connectSlotsByName(TankReplicator)

    def retranslateUi(self, TankReplicator):
        TankReplicator.setWindowTitle(QtGui.QApplication.translate("TankReplicator", "Tank Replicator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TankReplicator", "Original Project:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TankReplicator", "Target projects:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TankReplicator", "Sync Areas:", None, QtGui.QApplication.UnicodeUTF8))
        self.replicateButton.setText(QtGui.QApplication.translate("TankReplicator", "Replicate", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("TankReplicator", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("TankReplicator", "About", None, QtGui.QApplication.UnicodeUTF8))

