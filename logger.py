from datetime import datetime


log_file = 'imagefilter.log'
now = datetime.now()
timestamp = now.strftime('%d/%m/%Y %H:%M:%S')


def open_log(i):
    print(timestamp + ' ' + f'Opening image = {i}')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Opening image = {i}\n')


def wrong_open():
    print(timestamp + ' ' + 'The file is not an image')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + 'The file is not an image')


def filter_log(text):
    print(timestamp + '    ' + f'Applying a {text} filter')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Applying a {text} filter\n')


def save_log(i):
    print(timestamp + ' ' + f'Saving result image in = {i}')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Saving result image in = {i}\n')
