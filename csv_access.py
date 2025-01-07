import csv

reports_path = "/app/reports/"
def write_csv(filepath, dict):
    with open(reports_path + filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dict)

def append_csv(filepath, dict):
    with open(reports_path + filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dict)

def write_text(filepath, text):
    with open(reports_path + filepath, 'w') as f:
        f.write(text)

def append_text(filepath, text):
    with open(reports_path + filepath, 'a') as f:
        f.write(text)