import main
import io
import sys
import re
import pytest

@pytest.mark.basic
def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3 4 5'
    sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = main.getInput()
    print(f'The list values {numbers}')
    ret = main.evenList(numbers)
    print(f'Your return values {ret}')
    print(f'The remainder numbers in the original list {numbers}')
    assert ret == [1, 3, 5]
    assert numbers == [2, 4]

@pytest.mark.edge
def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 3 5 4 2 7 8 1 2 5'
    sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = main.getInput()
    print(f'The list values {numbers}')
    ret = main.evenList(numbers)
    print(f'Your return values {ret}')
    print(f'The remainder numbers in the original list {numbers}')

    assert ret == [1, 5, 2, 8, 2]
    assert numbers == [3, 4, 7, 1, 5]

@pytest.mark.bonus
def test_main_3():
    numbers = [1] 
    print(f'The list values {numbers}')
    ret = main.evenList(numbers)
    print(f'Your return values {ret}')
    print(f'The remainder numbers in the original list {numbers}')

    assert ret == [1]
    assert numbers == []