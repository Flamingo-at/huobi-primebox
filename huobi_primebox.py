import time
import requests

from random import choice
from loguru import logger


def claim():
    task = 0
    card = 0
    try:
        with requests.Session() as client:
            while True:
                traceid = ''.join([choice('1234567890abcdef') for _ in range(32)])
                response = client.post(f'https://www.huobi.com/-/x/hbg/v1/prime-box/user/elfin/claim?x-b3-traceid={traceid}',
                                       json={
                                           "taskType": task,
                                           "date": date
                                       }, headers={'hb-pro-token': token})
                data = (response.json())['data']['resultFlag']
                if data == 0:
                    task += 1
                else:
                    card += 1
                    logger.info(f'{card} points')
                if task == 18:
                    break
                time.sleep(1)
    except:
        raise Exception()


def play():
    try:
        traceid = ''.join([choice('1234567890abcdef') for _ in range(32)])
        response = requests.post(f'https://www.huobi.com/-/x/hbg/v1/prime-box/red-packet-rain/play?x-b3-traceid={traceid}',
                                 json={
                                     "periodsNum": 1,
                                     "redPacketNum": 20
                                 }, headers={'hb-pro-token': token})
        if str(response.json()['data']['cardNum']) != '2':
            raise Exception()
        logger.info('+2 cards')
    except:
        raise Exception()


def main():
    try:
        if type == '1':
            claim()
        else:
            play()
    except:
        logger.error('Error')
        input()
    else:
        logger.info('Successfully')
        input()


if __name__ == '__main__':

    print("Bot Huobi primebox @flamingoat\n")

    type = input("Claim(1) or Play(2): ")
    if type == '1':
        date = input("Date(y-m-d): ")
    token = input("Token: ")
    print()

    main()
