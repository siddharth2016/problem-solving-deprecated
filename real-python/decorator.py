from datetime import datetime

def log_datetime(func):
    '''Log the date and time of a function'''
    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper

@log_datetime
def daily_backup():
    print('Daily backup job has finished.') 

daily_backup()