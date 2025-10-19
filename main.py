
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = list(map(int, input().split()))
    return numbers

def evenList(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = []
    N = len(numbers) // 2 + len(numbers) % 2
    for i in range(N):
        result.append(numbers.pop(i))
    return result

def main():
    numbers = getInput()
    retval = evenList(numbers)
    print(f'The numbers at the even index: {retval}')
    print(f'The remainder numbers in the original list: {numbers}')


if __name__ == '__main__':
    main()
