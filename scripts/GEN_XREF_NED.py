#==============================================================#
# Generates the XREF database from NED references              #
#==============================================================#
from pyROSITA.data import eROSITACatalog
from pyROSITA.utils import mylog
import os
import pathlib as pt

#--------------------------------------------------------------#
# Settings
database_directory = "/home/ediggins/pyROSITA_test"
catalog_path = None
first_n = None #for debugging, only catalog the first N entries.
databases = "all" #NYI
#--------------------------------------------------------------#
# Setup
if not os.path.exists(database_directory):
    mylog.info(f"{database_directory} doesn't currently exist. Creating it.")
    pt.Path(database_directory).mkdir(parents=True)

if catalog_path is None:
    from pyROSITA.data import download_data_product
    mylog.info(f"The catalog path was not specified. Downloading.")
    download_data_product("https://erosita.mpe.mpg.de/dr1/AllSkySurveyData_dr1/Catalogues_dr1/MerloniA_DR1/eRASS1_Hard.tar.gz",database_directory)
    catalog_path = os.path.join(database_directory,"eRASS1_Hard.v1.0.fits")

q = eROSITACatalog(catalog_path, _db_file=os.path.join(database_directory,"XREF.db"))

if first_n is not None:
    q.data = q.data.iloc[:first_n]

q.cross_reference(max_workers=10,databases=["NED"])