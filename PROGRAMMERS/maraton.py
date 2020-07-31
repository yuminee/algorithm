def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('no')
    
    l = len(participant)
    for i in range(l):
        if participant[i] != completion[i]:
            return participant[i]
