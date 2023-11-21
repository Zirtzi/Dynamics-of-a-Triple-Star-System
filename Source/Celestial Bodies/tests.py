# Imports
from ModelFunctions import *

twoMasses = [MSUN, MEARTH]

twoIC = [SUNPOS, EARTHPOS, SUNVEL, EARTHVEL]

threeMasses = [MSUN, MEARTH, MMOON]

threeIC = [SUNPOS, EARTHPOS, MOONPOS, SUNVEL, EARTHVEL, MOONVEL]

CoupledTwoBody2DPlotPos(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

CoupledTwoBody2DAnimPos(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

CoupledTwoBody2DPlotVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, "Sun", "Earth")

CoupledTwoBody2DAnimVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, "Sun", "Earth")

CoupledTwoBody3DPlotPos(twoMasses, twoIC, 0, EARTHPERIOD, "Sun", "EARTH")

CoupledTwoBody3DAnimPos(twoMasses, twoIC, 0, EARTHPERIOD, "Sun", "Earth")

CoupledTwoBody3DPlotVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

CoupledTwoBody3DAnimVel(twoMasses, twoIC, 0, EARTHPERIOD, 0, 1, "Sun", "Name")

CoupledThreeBody2DPlotPos(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

CoupledThreeBody2DAnimPos(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

CoupledThreeBody2DPlotVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, "Sun", "Earth", "Moon")

CoupledThreeBody2DAnimVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, "Sun", "Earth", "Moon")

CoupledThreeBody3DPlotPos(threeMasses, threeIC, 0, EARTHPERIOD, "Sun", "Earth", "Moon")

CoupledThreeBody3DAnimPos(threeMasses, threeIC, 0, EARTHPERIOD, "Sun", "Earth", "Moon")

CoupledThreeBody3DPlotVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

CoupledThreeBody3DAnimVel(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")