from datetime import datetime
#from core import list_img
#from core import path


log_file = 'imagefilter.log'
now = datetime.now()
timestamp = now.strftime('%d/%m/%Y %H:%M:%S')


def open_log(i):
    print(timestamp + ' ' + f'Opening image = {list_img[i]}')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Opening image = {list_img[i]}\n')


def wrong_open():
    print(timestamp + ' ' + 'The file is not an image')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + 'The file is not an image')


def filter_log(text):
    print(timestamp + '    ' + f'Applaying a {text} filter')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Applaying a {text} filter\n')


def save_log():
    print(timestamp + ' ' + f'Saving result image in = {"CLI"}')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Saving result image in = {"CLI"}\n')
