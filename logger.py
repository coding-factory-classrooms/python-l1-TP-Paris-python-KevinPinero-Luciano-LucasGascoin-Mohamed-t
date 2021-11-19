from datetime import datetime


log_file = 'imagefilter.log'
now = datetime.now()
timestamp = now.strftime('%d/%m/%Y %H:%M:%S')


def open_log(i):
    """[get the timestamp function, open an imagefilter.log to add the path(image file) with timestamp]

    Args:
        i ([source path]): [all images]
    """
    print(timestamp + ' ' + f'Opening image = {i}')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Opening image = {i}\n')


def filter_log(text):
    """[get the timestamp function, write the applied filter in imagefilter.log with timestamp]

    Args:
        text ([string]): [applied filter (gray / blur / dilate)]
    """
    print(timestamp + '    ' + f'Applying a {text} filter')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Applying a {text} filter\n')


def save_log(i):
    """[get the timestamp function, open an imagefilter.log to add the path(image file) in the output directory with timestamp]

    Args:
        i ([source exit path]): [image exit way]
    """
    print(timestamp + ' ' + f'Saving result image in = {i}')
    with open(log_file, 'a') as f:
        f.write(timestamp + ' ' + f'Saving result image in = {i}\n')