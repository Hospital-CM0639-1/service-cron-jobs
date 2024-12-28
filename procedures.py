import database_access as db
import csv_access as c
from datetime import datetime

records = db.select('SELECT m.procedure_id, p.first_name, p.last_name, e.triage_notes, e.priority_level, s.first_name, s.last_name, m.procedure_name, m.procedure_timestamp, m.description, m.procedure_cost FROM medical_procedures as m, patients as p, emergency_visits as e, staff as s WHERE m.performed_by_staff_id = s.staff_id AND m.visit_id = e.visit_id AND e.patient_id = p.patient_id AND m.procedure_timestamp >= NOW()::date;')
print(records)
c.write_csv(datetime.now().strftime('%d-%m-%Y') + '-procedures.csv', records)


#