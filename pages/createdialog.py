from PyQt5 import QtCore, QtGui, QtWidgets
import sys,platform
def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)
sys.excepthook = no_abort

class CreateDialog(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(CreateDialog, self).__init__(parent)
        self.setupUi(self) 
        self.show()
    def setupUi(self, CreateDialog):
        self.CreateDialog = CreateDialog
        CreateDialog.setFixedSize(647, 164)
        CreateDialog.setStyleSheet("QComboBox::drop-down {    border: 0px;}QComboBox::down-arrow {    image: url(:/images/down_icon.png);    width: 14px;    height: 14px;}QComboBox{    padding: 1px 0px 1px 3px;}QLineEdit:focus {   border: none;   outline: none;}")
        CreateDialog.setWindowTitle("Create Tasks")
        self.background = QtWidgets.QWidget(CreateDialog)
        self.background.setGeometry(QtCore.QRect(0, 0, 691, 391))
        self.background.setStyleSheet("background-color: #1E1E1E;")
        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setFamily("Arial")
        self.site_box = QtWidgets.QComboBox(self.background)
        self.site_box.setGeometry(QtCore.QRect(50, 20, 151, 21))
        self.site_box.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.site_box.addItem("Site")
        self.site_box.setFont(font)
        self.input_edit = QtWidgets.QLineEdit(self.background)
        self.input_edit.setGeometry(QtCore.QRect(250, 20, 151, 21))
        self.input_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_edit.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.input_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.input_edit.setPlaceholderText("Link")
        self.input_edit.setFont(font)
        self.profile_box = QtWidgets.QComboBox(self.background)
        self.profile_box.setGeometry(QtCore.QRect(450, 20, 151, 21))
        self.profile_box.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.profile_box.addItem("Profile")
        self.profile_box.setFont(font)
        self.monitor_edit = QtWidgets.QLineEdit(self.background)
        self.monitor_edit.setGeometry(QtCore.QRect(50, 70, 61, 21))
        self.monitor_edit.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.monitor_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.monitor_edit.setPlaceholderText("Monitor")
        self.monitor_edit.setFont(font)
        self.monitor_edit.setText("5.0")
        self.error_edit = QtWidgets.QLineEdit(self.background)
        self.error_edit.setGeometry(QtCore.QRect(140, 70, 61, 21))
        self.error_edit.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.error_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.error_edit.setPlaceholderText("Error")
        self.error_edit.setFont(font)
        self.error_edit.setText("5.0")
        self.addtask_btn = QtWidgets.QPushButton(self.background)
        self.addtask_btn.setGeometry(QtCore.QRect(250, 110, 151, 32))
        self.addtask_btn.setText("Add Task")
        self.maxprice_checkbox = QtWidgets.QCheckBox(self.background)
        self.maxprice_checkbox.setGeometry(QtCore.QRect(250, 70, 87, 20))
        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setFamily("Arial")
        self.maxprice_checkbox.setFont(font)
        self.maxprice_checkbox.setStyleSheet("color: #FFFFFF;")
        self.maxprice_checkbox.setText("Max Price")
        self.price_edit = QtWidgets.QLineEdit(self.background)
        self.price_edit.setGeometry(QtCore.QRect(350, 70, 51, 21))
        self.price_edit.setFont(font)
        self.price_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.price_edit.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.price_edit.setPlaceholderText("330")
        self.price_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14) if platform.system() == "Darwin" else font.setPointSize(14*.75)
        self.addtask_btn.setFont(font)
        self.addtask_btn.setStyleSheet("border-radius: 10px;background-color: #5D43FB;color: #FFFFFF;")
        self.addtask_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.site_box.addItem("Bestbuy")
        self.site_box.addItem("Walmart")

        QtCore.QMetaObject.connectSlotsByName(CreateDialog)


