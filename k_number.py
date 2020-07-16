#https://programmers.co.kr/learn/courses/30/parts/12198
#k
def solution(array, commands):
    a = len(commands)
    answer = [0] * a
    for i in range(0,a):
        x = commands[i][0]
        y = commands[i][1]
        z = commands[i][2]
        len_new = y-x + 1
        j = 0
        h = x -1
        new_array = [0] *  len_new
        while (j<len_new ) and (h<y):
            new_array[j] = array[h]
            j=j+1
            h=h+1

        new_array.sort()
        answer[i] = new_array[z-1]

    return answer

