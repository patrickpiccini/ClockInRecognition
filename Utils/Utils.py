import os, random
from datetime import datetime



def userRandonId() -> str :
    """Generate a random number in to be a user_id"""
    number = random.randint(1,10000)
    return str(f'{number:0>5}')


def getDateTime() -> str:
    date_time_now = datetime.now()
    return date_time_now.strftime('%Y/%m/%d %H:%M')


def getDate() -> str:
    date_time_now = datetime.now()
    return date_time_now.strftime('%Y-%m-%d')