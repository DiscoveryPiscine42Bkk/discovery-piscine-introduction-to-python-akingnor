import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for param in reversed(args):
        print(param)