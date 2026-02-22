class Solution:
    def binaryGap(self, n: int) -> int:
        # 10진수를 2인수로 먼저 바꿔야 함.
        # 그리고 1이랑 가장 먼 다른 1을 찾아야함.
        # 또 다른 1이 나오면 count를 reset하고 다시 세야함.
        binary = f'{n:b}'
        longest_distance = 0
        current_distance = 0

        for i in range(1, len(binary)):
            if binary[i] == "1":
                current_distance += 1
                if (current_distance >= longest_distance):
                    longest_distance = current_distance
                current_distance = 0
            else:
                current_distance += 1
        return longest_distance

                



        