import sys
from createRamanDB import *

init(new=True)
Settings.createTable()
Molecule.createTable()
Experiment.createTable()
Data.createTable()
molecules = ['ferrodoxin', 'hydrogenase','ferrodoxin']
dates = ['10_12_2015', '10_23_2015', '11_1_2015']
times = ['11am','12pm','3pm']
temperature = [20,22,23]
frequency = [600,550,600]


for j in range(3):
    filename = 'raman{}.csv'.format(j)
    with open(filename, 'rb') as csvfile:

        molecule = Molecule(molecule_name = molecules[j])
        settings =Settings(temperature = temperature[j], frequency = frequency[j])
        
        experiment = Experiment(date = dates[j], time = times[j] , molecule = molecule, settings = settings)
        for line in csvfile.readlines():
            array = line.split(',')
            count = int(array[0])
            ramanShift = float(array[1])
            Data(ramanShift = ramanShift, count = count, experiment = experiment)
    




    csvfile.close()
