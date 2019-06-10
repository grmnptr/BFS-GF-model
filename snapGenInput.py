#!/usr/bin/python
import os
import numpy as np
import math

# The number of samples to create 
noSamples = 10

# The time steps it should save. It should be stored in 
# a list of strings like ['2', '4', '...']
# startTime = 0.01
# endTime = 15.0
# writeInterval = 0.01
# midTime = 0.5
# writeInterval2 = 0.2
# steps1 = np.linspace(startTime, 
#                     math.floor((midTime-startTime)/writeInterval)*writeInterval+startTime, 
#                     math.floor((midTime-startTime)/writeInterval),
#                     endpoint = False)
# steps2 = np.linspace(midTime, 
#                     math.floor((endTime-midTime)/writeInterval2)*writeInterval2+midTime, 
#                     math.floor((endTime-midTime)/writeInterval2),
#                     endpoint = False)
# 
# resultDir1 = [str(round(i,3)) for i in steps1]
# resultDir2 = [str(round(i,3)) for i in steps2]
# resultDir = resultDir1 + resultDir2

resultDir = ["140"]

# Command to execute the computations with
command = ["GeN-ROM"]

# Defining the type of file it should do perturbations in
pertIntervals = {}
pertIntervals["thermo"] = {

    "transport" : 
    {
        "mu" : [10, 100]
    }
}

# Defining the fields it should save
resultsToPrint = [
    "U",
    "p",
    "p_rgh",
    "phi",
    "implicitMomentumSource",
    "explicitMomentumSource"
]


# Defining the files associated with the perturbations
fileNames = {
	"thermo" : "thermophysicalProperties"
}

# Defining the directories of the files
srcDirs =  {
	"thermo" : os.path.join(os.getcwd(),"constant/fluidRegion/")
}

# Defining the directory where the script should save these files
origDirs = {
	"thermo" : os.path.join(os.getcwd(),"ROMFiles/originalFiles/thermo")
}

# Defining the directory where the script should save the perturbed files
pertDirs = {
	"thermo" : os.path.join(os.getcwd(),"ROMFiles/perturbedFiles/thermo")
}