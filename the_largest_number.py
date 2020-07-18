#주어진 리스트에서 가장 큰 수 찾기.
#원소는 0이상 1000이하
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
