from sqlobject import *
from sqlobject.inheritance import InheritableSQLObject


#db_filename = os.path.abspath('sqlobject_test.db')



def init(new=False):
    # Establish connection with database
    connection_string = 'mysql://cami:hamira@localhost/sqlobj_test'
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection
    if new:
        Measurements.dropTable(ifExists=True)
        Molecule.dropTable(ifExists=True)
        Settings.dropTable(ifExists=True)


class Molecule(SQLObject):
    molecule_name = StringCol()
    
    measurements = MultipleJoin("Measurements")



class Settings(SQLObject):
    date = StringCol()
    time = IntCol()
    temperature = IntCol()
    acquisation_mode = StringCol()
    frequency = IntCol()
    number_accumulation = IntCol()
    exposure_time = IntCol()
    h_binning = IntCol()
    v_binnng = IntCol()
    h_flip = IntCol()

    measurements = MultipleJoin("Measurements")


class Measurements(SQLObject):
    molecule = ForeignKey("Molecule",cascade=True)
    settings = ForeignKey("Settings",cascade=True)
    ramanShift = IntCol()
    date = IntCol()
    time = IntCol()


init(new=True)
Settings.createTable()
Molecule.createTable()
Measurements.createTable()