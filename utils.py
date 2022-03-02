from PyQt5.QtWidgets import QMessageBox, QProgressDialog, QProgressBar
from PyQt5.QtCore import *

def message(title, text, type):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    # msg.setIcon(QMessageBox.Warning)
    msg.setIcon(type)
    msg.addButton(QMessageBox.Ok)
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    dupa = msg.exec()
    return 'Wykonano info'

def msg_question(title, quest, parent):
    msgbox = QMessageBox
    answer = msgbox.question(parent, title, quest, msgbox.Yes | msgbox.No)
    if answer == msgbox.Yes:
        return msgbox

def progdialog(progress, title_text,text):  # okienko do progressu oblicze
    dialog = QProgressDialog()
    dialog.setWindowTitle(title_text)
    dialog.setLabelText(text)
    bar = QProgressBar(dialog)
    bar.setTextVisible(True)
    bar.setValue(progress)
    bar.setFormat('Kłócę się z excelem...%p%')
    dialog.setBar(bar)
    dialog.setMinimumWidth(300)
    dialog.show()
    return dialog, bar