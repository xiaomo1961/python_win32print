from PyQt5.QtWidgets import QWidget,QApplication,QSystemTrayIcon,QMenu,QAction,qApp
from PyQt5 import QtCore
from PyQt5.QtCore import QThread,pyqtSignal
import sys
from PyQt5.QtGui import QIcon
from untitled import Ui_Form
from system_hotkey import SystemHotkey
class Main(QWidget,Ui_Form):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('示例')
        self.setWindowIcon(QIcon('campaign.ico'))
        self.tray = Tray(self)
        self.hotKey = HotKeyThread(self)
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.hide()
    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.hide()
class Tray(QSystemTrayIcon):
    def __init__(self,UI):
        super(Tray,self).__init__()
        self.ui = UI
        self.setIcon(QIcon('campaign.ico'))
        self.setToolTip('示例')
        self.activated.connect(self.clickedIcon)
        self.menu()
        self.show()
    def clickedIcon(self,reason):
        if reason == 3:
            self.trayClickedEvent()
        elif reason ==1:
            self.contextMenu()
    def menu(self):
        menu = QMenu()
        action = QAction('退出',self,triggered=self.triggered)
        menu.addAction(action)
        self.setContextMenu(menu)
    def trayClickedEvent(self):
        if self.ui.isHidden():
            self.ui.setHidden(False)
            if self.ui.windowState() == QtCore.Qt.WindowMinimized:
                self.ui.showNormal()
            self.ui.raise_()
            self.ui.activateWindow()
        else:
            self.ui.setHidden(True)
    def triggered(self):
        self.deleteLater()
        qApp.quit()
class HotKeyThread(QThread,SystemHotkey):
    trigger = pyqtSignal()
    def __init__(self,UI):
        self.ui = UI
        super(HotKeyThread,self).__init__()
        self.register(('control','w'),callback=lambda x:self.start())
        self.trigger.connect(self.hotKeyEvent)
    def run(self):
        self.trigger.emit()
    def hotKeyEvent(self):
        if self.ui.isHidden():
            self.ui.setHidden(False)
            if self.ui.windowState() == QtCore.Qt.WindowMinimized:
                self.ui.showNormal()
            self.ui.raise_()
            self.ui.activateWindow()
        else:
            self.ui.setHidden(True)
    def quitThread(self):
        if self.isRunning():
            self.quit()
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    demo = Main()
    demo.show()
    sys.exit(app.exec_())