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
    acquisation_mode = StringCol(default = '1')
    color = StringCol(default = 'green')
    frequency = IntCol()
    number_accumulation = IntCol(default = 400)
    exposure_time = IntCol(default = 4)
    h_binning = IntCol(default = 0)
    v_binnng = IntCol(default = 0)
    h_flip = IntCol(default = 0)
    v_flip = IntCol(default = 0)

    measurements = MultipleJoin("Experiment")



class Data(SQLObject):
    ramanShift = FloatCol()
    count = IntCol()
    
    experiment = ForeignKey("Experiment",cascade=True)



class Experiment(SQLObject):
    date = StringCol()
    time = StringCol()
    
    molecule = ForeignKey("Molecule",cascade=True)
    settings = ForeignKey("Settings",cascade=True)
    data = MultipleJoin("Data")


# Generate database



