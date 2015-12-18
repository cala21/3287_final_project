from sqlobject import *
from sqlobject.inheritance import InheritableSQLObject

def init(new=False):
    # Establish connection with database
    connection_string = 'mysql://cami:hamira@localhost/sqlobj_test'
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection
    if new:
        Data.dropTable(ifExists=True)
        Experiment.dropTable(ifExists=True)
        Molecule.dropTable(ifExists=True)
        Settings.dropTable(ifExists=True)



# Create Tables

class Molecule(SQLObject):
    molecule_name = StringCol()
    
    measurements = MultipleJoin("Experiment")



class Settings(SQLObject):
    temperature = IntCol()
    acquisation_mode = StringCol()
    frequency = IntCol()
    number_accumulation = IntCol()
    exposure_time = IntCol()
    h_binning = IntCol()
    v_binnng = IntCol()
    h_flip = IntCol()

    measurements = MultipleJoin("Experiment")



class Data(SQLObject):
    ramanShift = FloatCol()
    count = IntCol()
    
    experiment = ForeignKey("Experiment",cascade=True)



class Experiment(SQLObject):
    date = IntCol()
    time = IntCol()
    
    molecule = ForeignKey("Molecule",cascade=True)
    settings = ForeignKey("Settings",cascade=True)
    data = MultipleJoin("Data")


# Generate database

init(new=True)
Settings.createTable()
Molecule.createTable()
Experiment.createTable()
Data.createTable()
