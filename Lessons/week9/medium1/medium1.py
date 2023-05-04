def lottery(ticket, win):

    return 'Winner!' if sum(chr(n) in s for s, n in ticket) >= win else 'Loser!'


print(lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2))


def solution(i, e, s):
    for x in range(len(i)):
        if i[x] == e:
            i[x] = s
    return i


print(solution([3, 4, 7, 4, 1], 4,  0))
