import sys

def downcase_it(s):
    return s.lower()

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for param in args:
        print(downcase_it(param))