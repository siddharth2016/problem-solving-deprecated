class Solution:
    def genFibNum(self, a, b, c, n, m):
        # code here
        
        def G(n):
            #print(F)
            power(F, n-2)
            return sum(F[0])%m
        
        def power(F, n):
            if n==0 or n==1:
                return
            
            power(F, n//2)
            multiply(F, F)
            
            M = [[a, b, c],
                [1, 0, 0],
                [0, 0, 1]]
                
            if n%2==1:
                multiply(F, M)
        
        def multiply(F, M):
            x = (F[0][0]*M[0][0]+F[0][1]*M[1][0]+F[0][2]*M[2][0])%m
            y = (F[0][0]*M[0][1]+F[0][1]*M[1][1]+F[0][2]*M[2][1])%m
            z = (F[0][0]*M[0][2]+F[0][1]*M[1][2]+F[0][2]*M[2][2])%m
            
            q = (F[1][0]*M[0][0]+F[1][1]*M[1][0]+F[1][2]*M[2][0])%m
            p = (F[1][0]*M[0][1]+F[1][1]*M[1][1]+F[1][2]*M[2][1])%m
            r = (F[1][0]*M[0][2]+F[1][1]*M[1][2]+F[1][2]*M[2][2])%m
            
            s = (F[2][0]*M[0][0]+F[2][1]*M[1][0]+F[2][2]*M[2][0])%m
            t = (F[2][0]*M[0][1]+F[2][1]*M[1][1]+F[2][2]*M[2][1])%m
            u = (F[2][0]*M[0][2]+F[2][1]*M[1][2]+F[2][2]*M[2][2])%m
            
            F[0][0] = x
            F[0][1] = y
            F[0][2] = z
            F[1][0] = q
            F[1][1] = p
            F[1][2] = r
            F[2][0] = s
            F[2][1] = t
            F[2][2] = u
        
        F = [[a,b,c],
            [1,0,0],
            [0,0,1]]
        #print(F)
        if n==1 or n==2:
            return 1%m
        return (G(n)%m)