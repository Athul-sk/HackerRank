# This code displays numbers from 1 to n(entered by user) in a single line
if __name__ == '__main__':
    n = int(input())
    result = ""
    for i in range(1,n+1):
        result += str(i)
    print(result)
