import sys
import configparser
#from def_video import func_vid

from def_video import func_vid

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
    elif arg == "--video":
        func_vid()
        for i, arg in enumerate(args):
            rep["input"] = 'output'
            if arg == '-o':
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

        # my_video = arg.split('=')
        # print(my_video)
        # rep['input'] = my_video[1]


        #func_vid(rep["output"])


filters_arg = rep["filters"]
split_filters = rep['filters'].split('|')

