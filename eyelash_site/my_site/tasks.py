from conf.celery import app
import os
import datetime
@app.task
def backup_db():
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"backup_db_{date_string}.sql"
    os.system(f"sudo -u postgres pg_dump browdb > /root/backup_db/{filename}")

    return True

