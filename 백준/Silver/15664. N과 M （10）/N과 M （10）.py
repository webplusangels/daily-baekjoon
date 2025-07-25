import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

def func(w, l):
    if len(l) == M:
        print(*l)
        return

    last_num = None

    for i in range(w, N):
        if N_list[i] != last_num:
            l.append(N_list[i])
            last_num = N_list[i]
            func(i+1, l)
            l.pop()

func(0, [])