import sys
args = sys.argv[1:]
if len(args) != 2:
    print("none")
else:
    try:
        start = int(args[0])
        end = int(args[1])
        if start <= end:
            result = list(range(start, end + 1))
        else:
            result = list(range(start, end - 1, -1))

        print(result)
    except ValueError:
        print("none")