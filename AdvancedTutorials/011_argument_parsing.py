import sys

#sys.argv[0]  # The name of the script
#sys.argv[1]  # The first argument

#print(sys.argv)

# python 011_argument_parsing.py test.txt Hello
""" filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message) """

# optional arguments    
import getopt

# python 011_argument_parsing.py -f hello.txt -m 'Hello World'
filename = 'test.txt'
message = 'Hello World'
opts, args = getopt.getopt(sys.argv[1:],"f:m:",['filename','message'])

for opt, arg in opts:
    if opt in ['-f', '--filename']:
        filename = arg
    elif opt in ['-m', '--message']:
        message = arg

with open(filename, 'w+') as f:
    f.write(message)