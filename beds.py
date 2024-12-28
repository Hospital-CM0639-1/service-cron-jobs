import database_access as db
import csv_access as c
from datetime import datetime

filename = datetime.now().strftime('%d-%m-%Y') + '-beds.csv'

c.write_text(filename, 'OCCUPIED\n')
records = db.select("SELECT b.bed_id, p.first_name, p.last_name, e.triage_notes, e.priority_level, b.ward_section, b.bed_number, b.current_status, b.last_cleaned_timestamp FROM hospital_beds as b, emergency_visits as e, patients as p WHERE b.current_visit_id = e.visit_id AND p.patient_id = e.patient_id;")
c.append_csv(filename, records)

c.append_text(filename, 'AVAILABLE\n')
records = db.select("SELECT bed_id, ward_section, bed_number, current_status, last_cleaned_timestamp FROM public.hospital_beds WHERE current_visit_id IS NULL;")
c.append_csv(filename, records)