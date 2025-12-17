# Banker's Algorithm logic

def is_safe(n, m, alloc, maxm, avail):
    need = [[maxm[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_seq = []
    work = avail[:]

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += alloc[i][j]
                    safe_seq.append(i)
                    finish[i] = True
                    found = True
        if not found:
            return False, []

    return True, safe_seq

