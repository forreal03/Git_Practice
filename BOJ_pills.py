import sys
input = sys.stdin.readline

ways_w_h = [[-1] * 31 for _ in range(31)]
ways_w_h[0][1] = 1

def pop_pills(whole_pills, half_pills):
    if ways_w_h[whole_pills][half_pills] == -1:
        ways = 0
        if whole_pills > 0:
            ways += pop_pills(whole_pills - 1, half_pills + 1)
        if half_pills > 0:
            ways += pop_pills(whole_pills, half_pills -1)
        ways_w_h[whole_pills][half_pills] = ways
    else:
        ways = ways_w_h[whole_pills][half_pills]
    return ways

while(True):
    N = int(input())
    if N == 0:
        break
    else:
        answer = pop_pills(N, 0)
        print(answer)