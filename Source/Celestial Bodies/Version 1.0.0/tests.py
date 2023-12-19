# Imports
from ModelFunctions import *

twoMasses = [MSUN, MEARTH]

twoIC = [SUNPOS, EARTHPOS, SUNVEL, EARTHVEL]

threeMasses = [MSUN, MEARTH, MMOON]

threeIC = [SUNPOS, EARTHPOS, MOONPOS, SUNVEL, EARTHVEL, MOONVEL]

OnEarth = [MEARTH, REARTH]

OnMoon = [MMOON, RMOON]

ballIc = [100, 0]

# ProjectileMotionPositionPlot(OnEarth, ballIc, 0, 4.52, "Earth", "Projectile")

# ProjectileMotionPositionAnim(OnEarth, ballIc, 0, 4.52, "Earth", "Projectile")

# ProjectileMotionVelocityPlot(OnEarth, ballIc, 0, 4.52, "Earth", "Projectile")

# ProjectileMotionVelocityAnim(OnEarth, ballIc, 0, 4.52, "Earth", "Projectile")

# CoupledTwoBody2DPlotPos(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

# CoupledTwoBody2DAnimPos(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

# CoupledTwoBody2DPlotVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, "Sun", "Earth")

# CoupledTwoBody2DAnimVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, "Sun", "Earth")

# CoupledTwoBody3DPlotPos(twoMasses, twoIC, 0, EARTHPERIOD, "Sun", "EARTH")

# CoupledTwoBody3DAnimPos(twoMasses, twoIC, 0, EARTHPERIOD, "Sun", "Earth")

# CoupledTwoBody3DPlotVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

# CoupledTwoBody3DAnimVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Name")

# CoupledThreeBody2DPlotPos(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

# CoupledThreeBody2DAnimPos(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

# CoupledThreeBody2DPlotVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, "Sun", "Earth", "Moon")

# CoupledThreeBody2DAnimVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, "Sun", "Earth", "Moon")

# CoupledThreeBody3DPlotPos(threeMasses, threeIC, 0, EARTHPERIOD, "Sun", "Earth", "Moon")

# CoupledThreeBody3DAnimPos(threeMasses, threeIC, 0, EARTHPERIOD, "Sun", "Earth", "Moon")

# CoupledThreeBody3DPlotVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

# CoupledThreeBody3DAnimVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

# class PlotCanvas(FigureCanvasQTAgg):
#     def __init__(self, parent=None, width=3, height=2, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         FigureCanvasQTAgg.__init__(self, fig)
#         self.setParent(parent)
#         self.plot()

#     def plot(self):
#         data = [5 for i in range(25)]
#         self.axes.plot(data, 'r-')
#         self.axes.set_title('PyQt Matplotlib Example')
#         self.draw()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # Title of Window
#         self.setWindowTitle("Plot Integration with Toolbar")
#         # Height and Width of Window
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QWidget for the central widget
#         centralWidget = QWidget(self)
#         self.setCentralWidget(centralWidget)

#         # Create a QVBoxLayout instance
#         layout = QVBoxLayout(centralWidget)

#         # Create the Matplotlib canvas and add it to the layout
#         plotCanvas = PlotCanvas(self, width=3, height=2)
#         layout.addWidget(plotCanvas)

#         # Create the navigation toolbar and add it to the layout
#         toolbar = NavigationToolbar(plotCanvas, self)
#         layout.addWidget(toolbar)

#         # Create a QLineEdit as a text field and add it to the layout
#         self.textField = QLineEdit("Enter some text here...")
#         layout.addWidget(self.textField)

# app = QApplication(sys.argv)
# mainWindow = MainWindow()
# mainWindow.show()
# sys.exit(app.exec())

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Main Window")
#         self.setGeometry(100, 100, 600, 400)
        
#         self.openSecondWindowButton = QPushButton("Open Second Window", self)
#         self.openSecondWindowButton.clicked.connect(self.openSecondWindow)
#         self.openSecondWindowButton.resize(200, 50)
#         self.openSecondWindowButton.move(200, 175)

#     def openSecondWindow(self):
#         self.secondWindow = SecondWindow()
#         self.secondWindow.show()

# class SecondWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Second Window")
#         self.setGeometry(150, 150, 400, 300)
        
#         self.openThirdWindowButton = QPushButton("Open Third Window", self)
#         self.openThirdWindowButton.clicked.connect(self.openThirdWindow)
#         self.openThirdWindowButton.resize(150, 40)
#         self.openThirdWindowButton.move(125, 130)

#     def openThirdWindow(self):
#         self.thirdWindow = ThirdWindow()
#         self.thirdWindow.show()

# class ThirdWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Third Window")
#         self.setGeometry(200, 200, 300, 200)

# app = QApplication(sys.argv)
# mainWindow = MainWindow()
# mainWindow.show()
# sys.exit(app.exec())

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # Create combo box and add items
#         self.comboBox = QComboBox(self)
#         self.comboBox.addItem("Select an option")  # First item
#         self.comboBox.addItem("Option 1")
#         self.comboBox.addItem("Option 2")
#         # ...

#         # Create text field
#         self.textField = QLineEdit(self)

#         # Layout
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.comboBox)
#         layout.addWidget(self.textField)

#         # Connect the signal to the slot
#         self.comboBox.currentIndexChanged.connect(self.onComboChange)

#         self.setLayout(layout)

#     def onComboChange(self, index):
#         # Disable text field if first index is selected
#         if index == 0:
#             self.textField.setDisabled(True)
#         else:
#             self.textField.setDisabled(False)

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # Create the text fields
#         self.mainTextField = QLineEdit(self)
#         self.otherTextField1 = QLineEdit(self)
#         self.otherTextField2 = QLineEdit(self)

#         # Create the combo box
#         self.comboBox = QComboBox(self)
#         self.comboBox.addItem("Option 1")
#         self.comboBox.addItem("Option 2")

#         # Layout
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.mainTextField)
#         layout.addWidget(self.otherTextField1)
#         layout.addWidget(self.otherTextField2)
#         layout.addWidget(self.comboBox)

#         # Connect the signal to the slot
#         self.mainTextField.textChanged.connect(self.onTextChange)

#         self.setLayout(layout)

#     def onTextChange(self, text):
#         # Disable the combo box and other text fields if the main text field is not empty
#         isDisabled = bool(text)
#         self.comboBox.setDisabled(isDisabled)
#         self.otherTextField1.setDisabled(isDisabled)
#         self.otherTextField2.setDisabled(isDisabled)

# app = QApplication(sys.argv)
# mainWindow = MyWindow()
# mainWindow.show()
# sys.exit(app.exec())

# # Create a figure and an axes
# fig, ax = plt.subplots()

# # Plot some data
# ax.plot([0, 1], [0, 1], label='Line')

# # Add title and labels
# ax.set_title("Example Plot")
# ax.set_xlabel("X-axis label")
# ax.set_ylabel("Y-axis label")

# # Adjust the bottom margin to create space below the x-axis
# fig.subplots_adjust(bottom=0.25)  # Increase bottom margin to create more space

# # Add notes with careful positioning
# # The y-coordinate is chosen to be less than the bottom margin but above 0
# fig.text(0.1, 0.05, "Note: This is an important note about the plot.", ha='left', va='bottom')

# # Show the plot
# plt.show()

class SubWindow(QWidget):
    def __init__(self, main_window, title):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle(title)
        self.resize(300, 200)

        # You can add more UI elements and logic here

    def closeEvent(self, event):
        self.main_window.show()  # Show the main window when the sub window is closed
        super().closeEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.resize(400, 300)

        # Buttons to open sub windows
        self.openSubWindow1Button = QPushButton("Open SubWindow 1", self)
        self.openSubWindow1Button.clicked.connect(self.openSubWindow1)
        self.openSubWindow2Button = QPushButton("Open SubWindow 2", self)
        self.openSubWindow2Button.clicked.connect(self.openSubWindow2)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.openSubWindow1Button)
        layout.addWidget(self.openSubWindow2Button)

        # Central widget
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def openSubWindow1(self):
        self.subWindow1 = SubWindow(self, "Sub Window 1")
        self.subWindow1.show()
        self.hide()  # Hide the main window

    def openSubWindow2(self):
        self.subWindow2 = SubWindow(self, "Sub Window 2")
        self.subWindow2.show()
        self.hide()  # Hide the main window

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

main()