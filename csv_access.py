import csv

def write_csv(filepath, dict):
    with open('/app/reports/'+filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dict)

def append_csv(filepath, dict):
    with open('/app/reports/'+filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dict)

def write_text(filepath, text):
    with open('/app/reports/'+filepath, 'w') as f:
        f.write(text)

def append_text(filepath, text):
    with open('/app/reports/'+filepath, 'a') as f:
        f.write(text)