import math

def merge_the_tools(string, k):
    # your code goes here
    if not string:
        return

    result = ''
    for i, ch in enumerate(string):
        if i > 0 and i % k == 0:
            if result:
                print(result)

            result = ''

        if ch not in result:
            result += ch

    if result:
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)