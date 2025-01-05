import database_access as db
import csv_access as c
from datetime import datetime

records = db.select("SELECT staff_id, first_name, last_name, email, phone_number, role, department, specialization, hire_date, is_active FROM staff	WHERE hire_date >= CURRENT_DATE - INTERVAL '1 month';")
out_list = []
for r in records:
    r = list(r)
    if(r[-1]):
        r[-1] = 'Active'
    else:
        r[-1] = 'Not active'
    out_list.append(r)
print(out_list)
c.write_csv(datetime.now().strftime('%d-%m-%Y') + '-staff.csv', out_list)