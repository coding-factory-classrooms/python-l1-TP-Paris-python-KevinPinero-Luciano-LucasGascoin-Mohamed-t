import sys
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
args = sys.argv
rep = {
    'input': '',
    'output': '',
    'filters': ''
       }
for i, arg in enumerate(args):
    if arg == '-i':
        rep["input"] = args[i + 1]
    elif arg == '-o':
        rep["output"] = args[i + 1]
    elif arg == '-filters':
        rep["filters"] = args[i + 1]
    elif arg == '--config-file':
        rep['input'] = config['DEFAULT']['input']
        rep['output'] = config['DEFAULT']['output']
        rep['filters'] = config['DEFAULT']['filters']
        for i, arg in enumerate(args):
            if arg == '-i':
                rep["input"] = args[i + 1]
            elif arg == '-o':
                rep["output"] = args[i + 1]
            elif arg == '-filters':
                rep["filters"] = args[i + 1]
    elif arg == '--list-filters':
        print("Les filtres disponibles sont : grayscale, blur:(valeur) et dilate:(valeur)")


filters_arg = rep["filters"]
split_filters = rep['filters'].split('|')

