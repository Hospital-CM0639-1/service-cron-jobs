import database_access as db
import csv_access as c
from datetime import datetime

records = db.select('SELECT e.visit_id, e.admission_timestamp, e.discharge_timestamp, e.current_status, e.triage_notes, e.priority_level, p.first_name, p.last_name, p.date_of_birth, p.gender, p.contact_number FROM emergency_visits AS e, patients AS p WHERE e.patient_id = p.patient_id AND (e.admission_timestamp >= NOW()::date OR e.discharge_timestamp >= NOW()::date)')
print(records)
c.write_csv(datetime.now().strftime('%d-%m-%Y') + '-emergencies.csv', records)