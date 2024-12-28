# service-cron-jobs

##Reports
Reports are created as .csv files, containing a view of the data stored in the database. The boolean values are replaced with the line containing its semanstic (e.g. "True" for IsActive column of staff table is replaced with the string "Active").

##Environment
To work properly, the env.json file is requried. You need to create it in the same folder as other scripts.
It should contain the following:
{
    "host": <DB HOST>,
    "port": <DB PORT>,
    "user": <DB USER>,
    "password": <DB USER PASSWORD>,
    "backup_dir": <PATH TO THE DIRECTORY TO STORE THE BACK UP FILES>
}

##Scripts

#Reports
- **backup.py** - dumps the whole database
- **beds.py** - creates a csv report with the state of all beds
- **procedures.py** - creates a csv report with all medical procedures performed today
- **day_emergencies.py** - creates a csv report with all emergencies whose status changed today
- **day_vitals.py** - creates a csv report with all vitals recorded today
- **staff.py** - creats a csv report with all employees hired this month

#Extras
- **database_access.py** - wrapper script for database access
- **csv_access.py** - wrapper script to create and write into csv files

