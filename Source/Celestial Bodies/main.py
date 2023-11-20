# Imports
from ModelFunctions import *

masses = [MSUN, MEARTH]
ic = [SUNPOS, EARTHPOS, SUNVEL, EARTHVEL]

CoupledTwoBody2DPlotPos(masses, ic, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

# class MainWindow(QMainWindow):
#     # Constructor
#     def __init__(self):
#         super().__init__()
#         # Title of Window
#         self.setWindowTitle("Celestial Bodies")
#         # Height and Width of Window
#         self.resize(850,500)
#         self.setMinimumWidth(850)
#         self.setMinimumHeight(400)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())