import sys
args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    keyword = args[0]
    text = args[1]
    count = text.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)