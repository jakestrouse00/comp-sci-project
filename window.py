from PyQt5 import QtCore, QtGui, QtWidgets
from main import Predict


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        """All widgets for the UI are defined here"""
        Dialog.setObjectName("Dialog")
        Dialog.resize(854, 591)
        Dialog.setWhatsThis("")
        self.imagesToShow = QtWidgets.QSpinBox(Dialog)
        self.imagesToShow.setGeometry(QtCore.QRect(130, 151, 131, 31))
        self.imagesToShow.setObjectName("imagesToShow")
        self.imagesToShow.setMinimum(1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.showRandom = QtWidgets.QCheckBox(Dialog)
        self.showRandom.setGeometry(QtCore.QRect(550, 120, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showRandom.setFont(font)
        self.showRandom.setWhatsThis("")
        self.showRandom.setObjectName("showRandom")
        self.imageNumber = QtWidgets.QSpinBox(Dialog)
        self.showRandom.setChecked(True)
        self.imageNumber.setGeometry(QtCore.QRect(531, 181, 141, 31))
        self.imageNumber.setObjectName("imageNumber")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(570, 160, 71, 16))
        self.imageNumber.setMinimum(1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.continueButton = QtWidgets.QPushButton(Dialog)
        self.continueButton.setGeometry(QtCore.QRect(680, 540, 161, 41))
        self.continueButton.setObjectName("continueButton")
        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """The text and fuctionality of the widgets are changed here"""
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Predict Flower"))
        self.label.setText(_translate("Dialog", "Images to Show"))
        self.showRandom.setText(_translate("Dialog", "Random"))
        self.label_2.setText(_translate("Dialog", "Image #"))
        self.continueButton.setText(_translate("Dialog", "Start"))
        self.continueButton.clicked.connect(self.clicked)
        # loads the neural network while the ui is loading, to make predictions faster
        self.model = Predict("new_model", "testing")


    def clicked(self):
        """This function is called when the Start button is clicked"""
        # checks the state of the check box
        doRandom = self.showRandom.checkState()
        # gets the amount of images selected by the user in the ui
        imageNumber = int(self.imageNumber.text())
        # gets the amount of times to run selected by the user in the ui
        runAmount = int(self.imagesToShow.text())
        for i in range(runAmount):
            # chooses a random image from the testing folder, and places it in the test folder for the model to predict
            fileName = self.model.saveAndLoad(doRandom, imageNumber)
            # loads the image into the model
            imageData = self.model.loadImage()
            # self.model.displayShapes(imageData)
            # makes the prediction on the test image
            self.model.makePrediction(imageData, fileName)
            # removes the test image from the test folder
            self.model.removeTest(fileName)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
