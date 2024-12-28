import database_access as db
import csv_access as c
from datetime import datetime

records = db.select('SELECT p.first_name, p.last_name, s.first_name, s.last_name, pv.recorded_at, pv.body_temperature, pv.blood_pressure_systolic, pv.blood_pressure_diastolic, pv.heart_rate, pv.respiratory_rate, pv.oxygen_saturation, pv.additional_observations FROM patient_vitals as pv, emergency_visits as v, patients as p, staff as s WHERE v.patient_id = p.patient_id AND pv.visit_id = v.visit_id AND s.staff_id = pv.recorded_by_staff_id AND pv.recorded_at >= NOW()::date')
print(records)
c.write_csv(datetime.now().strftime('%d-%m-%Y') + '-vitals.csv', records)