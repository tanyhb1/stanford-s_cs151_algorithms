from math import ceil, floor, sqrt
import timer
def main():
    a = [1,2,3,4]
    b = [4,3,2,1]
    if set(a) ==  set(b):
        print(set(a)-set(b))
if __name__ == '__main__':
    main()