import csv

def write_csv(filepath, dict):
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dict)

def append_csv(filepath, dict):
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dict)

def write_text(filepath, text):
    with open(filepath, 'w') as f:
        f.write(text)

def append_text(filepath, text):
    with open(filepath, 'a') as f:
        f.write(text)