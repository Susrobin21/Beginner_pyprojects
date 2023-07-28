#python automation
#install schedule and requets library

from credentials import mobile_number 
import requests
import schedule
import time

def send_message():
    res = requests.post('https://textbelt.com/text', {
    'phone' : mobile_number,
    'key'   : 'textbelt',
    })

    print(res.json())

#schedule.every().day.at('18:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
