import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    T = int(data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        S = data[idx+2]
        idx += 3
        
        P = []
        C = []
        for _ in range(m):
            P.append(int(data[idx]))
            C.append(data[idx+1])
            idx += 2
            
        if m == 0:
            out.append("0")
            continue
            
        base_match = [0] * m
        for i in range(m):

            actual_q = P[i] - 1
            if 0 <= actual_q < n and S[actual_q] == C[i]:
                base_match[i] = 1
                
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i+1] = pref[i] + base_match[i]
            
        max_correct = pref[m]
        
        possible_ds = set()
        for i in range(m):
            for q_idx in range(n):
                if S[q_idx] == C[i]:
                    possible_ds.add(P[i] - (q_idx + 1))
                    

        possible_ds.discard(0)
        
        for d in possible_ds:

            match_d = [0] * m
            valid_d = [False] * m
            for i in range(m):
                target_q = P[i] - d
                if 1 <= target_q <= n:
                    valid_d[i] = True
                    if S[target_q - 1] == C[i]:
                        match_d[i] = 1
            
            
            dp_1 = -1000000
            dp_2 = -1000000
            
            if valid_d[0]:
                dp_1 = match_d[0]
            
            current_max = max(pref[m], dp_1 + (pref[m] - pref[1]))
            
            for i in range(1, m):
                next_dp_1 = -1000000
                next_dp_2 = -1000000
                

                if valid_d[i]:

                    if dp_1 >= 0:
                        next_dp_1 = dp_1 + match_d[i]

                    if P[i-1] < P[i] - d:
                        val = pref[i] + match_d[i]
                        if val > next_dp_1:
                            next_dp_1 = val
                            

                if dp_2 >= 0:
                    next_dp_2 = dp_2 + base_match[i]

                if dp_1 >= 0 and (P[i-1] - d < P[i]):
                    val = dp_1 + base_match[i]
                    if val > next_dp_2:
                        next_dp_2 = val
                        
                dp_1 = next_dp_1
                dp_2 = next_dp_2
                
                ans = max(dp_1 + (pref[m] - pref[i+1]), dp_2 + (pref[m] - pref[i+1]))
                if ans > max_correct:
                    max_correct = ans
                    
        out.append(str(max_correct))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()