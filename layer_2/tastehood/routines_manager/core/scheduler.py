""" Based on webserver will create automated tasks through 'schedule' tool """

from crontab import CronTab
import time
import requests
from routines_manager.routines.resource_rountines import switch_light_status

def add_task(name: str, shelf: int, mqtt: str, value: bool):
    cron = CronTab(user='root')
    task = cron.new(command=f'python {name} --shelf {shelf} --mqtt {mqtt} --value {value}')
    task.day.every(1)








