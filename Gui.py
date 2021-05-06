from lolMatches import getMatches

from PySide6 import QtCore, QtWidgets, QtGui


def appendString(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

class UI(object):
    leagues = list()
    def setupUi(self, ui):   #ui = qMainWindow
        ui.setObjectName("isMsi")
        ui.resize(643, 478)
        self.centralwidget = QtWidgets.QWidget(ui)
        self.centralwidget.setObjectName("centralwidget")
        self.checkboxesFrame = QtWidgets.QFrame(self.centralwidget)
        self.checkboxesFrame.setGeometry(QtCore.QRect(19, 9, 261, 421))
        self.checkboxesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.checkboxesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.checkboxesFrame.setObjectName("checkboxesFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.checkboxesFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.isLpl = QtWidgets.QCheckBox(self.checkboxesFrame)
        self.isLpl.setObjectName("isLpl")
        self.gridLayout.addWidget(self.isLpl, 2, 0, 1, 1)
        self.isLck = QtWidgets.QCheckBox(self.checkboxesFrame)
        self.isLck.setObjectName("isLck")
        self.gridLayout.addWidget(self.isLck, 3, 0, 1, 1)
        self.isLec = QtWidgets.QCheckBox(self.checkboxesFrame)
        self.isLec.setObjectName("isLec")
        self.gridLayout.addWidget(self.isLec, 0, 0, 1, 1)
        self.isWorlds = QtWidgets.QCheckBox(self.checkboxesFrame)
        self.isWorlds.setObjectName("isWorlds")
        self.gridLayout.addWidget(self.isWorlds, 5, 0, 1, 1)
        self.isLcs = QtWidgets.QCheckBox(self.checkboxesFrame)
        self.isLcs.setObjectName("isLcs")
        self.gridLayout.addWidget(self.isLcs, 1, 0, 1, 1)
        self.isMsi = QtWidgets.QCheckBox(self.checkboxesFrame)
        self.isMsi.setObjectName("isMsi")
        self.gridLayout.addWidget(self.isMsi, 4, 0, 1, 1)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(20, 270, 261, 51))
        self.submitButton.setObjectName("submitButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(300, 0, 332, 431))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.matchesDisplay = QtWidgets.QTextBrowser(self.groupBox)
        self.matchesDisplay.setObjectName("matchesDisplay")
        self.verticalLayout.addWidget(self.matchesDisplay)
        self.dayDisplay = QtWidgets.QCalendarWidget(self.checkboxesFrame)
        self.dayDisplay.setObjectName("dayDisplay")
        self.gridLayout.addWidget(self.dayDisplay)
        self.gridLayout.addWidget(self.submitButton)
        ui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 22))
        self.menubar.setObjectName("menubar")
        ui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui)
        self.statusbar.setObjectName("statusbar")
        ui.setStatusBar(self.statusbar)
        self.retranslateUi(ui)
        QtCore.QMetaObject.connectSlotsByName(ui)

    def retranslateUi(self, ui):
        _translate = QtCore.QCoreApplication.translate
        ui.setWindowTitle(_translate("isMsi", "LolMatches"))
        ui.setWindowIcon(QtGui.QIcon('icon.png'))
        self.isLpl.setText(_translate("isMsi", "LPL"))
        self.isLck.setText(_translate("isMsi", "LCK"))
        self.isLec.setText(_translate("isMsi", "LEC"))
        self.isWorlds.setText(_translate("isMsi", "Worlds"))
        self.isLcs.setText(_translate("isMsi", "LCS"))
        self.isMsi.setText(_translate("isMsi", "MSI"))
        self.submitButton.setText(_translate("isMsi", "Show Matches"))
        self.groupBox.setTitle(_translate("isMsi", "Matches"))

    def setMatches(self):
        print('Settin Matches')
        date = self.dayDisplay.selectedDate()
        date = date.toPython()
        matches = getMatches(self.getLeagues(), date)
        if not matches:
            self.matchesDisplay.clear()
            msg = QtWidgets.QMessageBox()
            msg.setText("No matches at: " + date.__str__())
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            x = msg.exec_()
        else:
            self.matchesDisplay.clear()
            for str in matches:
                self.matchesDisplay.append(str)

    def getLeagues(self):
        return self.leagues

    def append(self, str, *args):
        chkboxes = self.checkboxesFrame.findChildren(QtWidgets.QCheckBox)
        for chkBox in chkboxes:
            if chkBox.text() == str:
                if chkBox.isChecked():
                    self.leagues.append(str)
                else:
                    self.leagues.remove(str)
                print(self.leagues)

