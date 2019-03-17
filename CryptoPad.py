"""
Created By: Uee
Modified By:
"""

import sys
import os

import Client
import VernamCipher

from PyQt5.QtWidgets import *
from PyQt5.Qt import QIcon
from PyQt5.QtCore import *


class Notepad (QWidget):

	def __init__(self):
		super (Notepad, self).__init__ ()

		# Plain Text
		self.textLabel = QLabel (self)
		self.textLabel.setText ("Message")
		self.plainText = QTextEdit (self)

		# Crypto Text
		self.cryptoText = QTextEdit (self)
		self.cryptoText.setReadOnly (True)
		self.cryptoText.setHidden (True)

		# Key
		self.keyLabel = QLabel (self)
		self.keyLabel.setText ("Secret Key")
		self.key = QLineEdit (self)
		self.key.setEchoMode (QLineEdit.Password)

		# Toggle
		self.checkBox = QCheckBox ("Show Crypto Text", self)

		# Buttons
		self.clearBtn = QPushButton ('Clear')
		self.saveBtn = QPushButton ('Save')
		self.openBtn = QPushButton ('Open')

		# Client Thread
		self.clientThread = ClientThread ()
		self.clientThread.start ()

		self.init_ui ()

	def init_ui(self):
		vLayout = QVBoxLayout ()
		hLayout = QHBoxLayout ()

		hLayout.addWidget (self.clearBtn)
		hLayout.addWidget (self.saveBtn)
		hLayout.addWidget (self.openBtn)

		vLayout.addWidget (self.checkBox)

		vLayout.addWidget (self.keyLabel)
		vLayout.addWidget (self.key)

		vLayout.addWidget (self.textLabel)
		vLayout.addWidget (self.plainText)

		vLayout.addWidget (self.cryptoText)

		vLayout.addLayout (hLayout)

		# Buttons
		self.clearBtn.clicked.connect (self.clearText)
		self.saveBtn.clicked.connect (self.saveText)
		self.openBtn.clicked.connect (self.openText)

		# Checkbox
		self.checkBox.stateChanged.connect (self.changeLayout)

		# Layout
		self.setLayout (vLayout)

		self.setWindowTitle ("CryptoPad")
		self.setWindowIcon (QIcon ('icon.ico'))

		self.show ()

	def clearText(self):
		self.text.clear ()

	def saveText(self):
		fileName = QFileDialog.getSaveFileName (self, 'Save File', os.getenv ('HOME'))

		with open (fileName[0], 'w') as file:
			if not self.checkBox.checkState ():
				text = self.plainText.toPlainText ()
				file.write (text)
			else:
				text = self.cryptoText.toPlainText ()
				file.write (text)

	def openText(self):
		fileName = QFileDialog.getOpenFileName (self, 'Open File', os.getenv ('HOME'))

		with open (fileName[0], 'r') as file:
			text = file.read ()
			self.plainText.setText (text)

	def changeLayout(self, state = bool):
		if state == Qt.Checked:
			self.plainText.setHidden (True)
			self.cryptoText.setText (VernamCipher.VernamCipher (self.plainText.toPlainText (), self.key.text ()))
			self.cryptoText.setHidden (False)
		else:
			self.plainText.setHidden (False)
			self.plainText.setText (VernamCipher.VernamCipher (self.cryptoText.toPlainText (), self.key.text ()))
			self.cryptoText.setHidden (True)


# Thread Class
class ClientThread (QThread):

	def __init__(self, parent = None):
		super (ClientThread, self).__init__ (parent)

	def run(self):
		Client.main ()


app = QApplication (sys.argv)
writer = Notepad ()
sys.exit (app.exec_ ())
