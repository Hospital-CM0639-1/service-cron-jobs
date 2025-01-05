import database_access as db
import datetime
import os
import subprocess

def dump_backup():    
    env = db.env
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y')
    backup_file = f"{env['backup_dir']}/_backup_{timestamp}.sql"
    os.makedirs(env['backup_dir'], exist_ok=True)
    command = [
        'pg_dump',
        '-h', env['host'],
        '-p', str(env['port']),
        '-U', env['user'],
        '-F', 'c',             # Custom format
        '-b',                  # Include large objects
        '-v',                  # Verbose mode
        '-f', backup_file,
        'hospital'
    ]

    try:
        # Run the command
        subprocess.run(command, check=True, env={"PGPASSWORD": env['password']})
        print(f"Backup successful! Saved to {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Backup failed: {e}")

dump_backup()