import itertools


def odd_nums(max):

        for num in range ( 1, max + 1):

                if num % 2 == 0:
                    continue
                else: 
                    yield num

odd_nums2=[num for num in range ( 1, 15 + 1) if num%2>0]

if __name__ == "__main__":
    odd_nums(max)
