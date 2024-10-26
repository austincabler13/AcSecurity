import os
import shutil
from datetime import datetime, timedelta

def backup_directory(source_dir, backup_dir):
    # Ensure the backup directory exists
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Create a timestamped backup folder
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_subdir = os.path.join(backup_dir, f'backup_{timestamp}')
    os.makedirs(backup_subdir)

    # Copy the contents of the source directory to the backup directory
    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(backup_subdir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    print(f'Backup completed successfully. Backup stored in: {backup_subdir}')

def cleanup_old_backups(backup_dir, days=7):
    now = datetime.now()
    cutoff = now - timedelta(days=days)

    for folder in os.listdir(backup_dir):
        folder_path = os.path.join(backup_dir, folder)
        if os.path.isdir(folder_path):
            folder_time = datetime.fromtimestamp(os.path.getctime(folder_path))
            if folder_time < cutoff:
                shutil.rmtree(folder_path)
                print(f'Deleted old backup: {folder_path}')

if __name__ == "__main__":
    source_directory = os.path.dirname(os.path.abspath(__file__))
    backup_directory = os.path.join(source_directory, 'backups')
    backup_directory(source_directory, backup_directory)
    cleanup_old_backups(backup_directory)
