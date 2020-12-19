def MMC(R,C):
    for r in range(len(R)):
        MMC[r][r] = 0

    for c in range(1,len(R)):
        for r in range(c-1,-1,-1):
            MMC[r][c] = infinity
            for k in range(r,c):
                subprob = MMC[r][k] + MMC[k][c] + R[r]C[k]C[c]
                if subprob < MMC[r][c]:
                    MMC[r][c] = subprob
                    
