def minJumps(self, arr, n):
   #code here
   if len(arr) == 1:
       return 0
   if arr[0] == 0:
       return -1

   curr = 0
   jump = 1
   if arr[curr] + curr>=n-1:
       return jump
   while curr<n-1:
       mx = -1
       mxi = curr + arr[curr]
       j = curr+1
       while j<n and j<=mxi:
           if (arr[j]+j)>=mx:
               curr = j
               mx = arr[j]+j
           j+=1
       if curr<n-1 and arr[curr] == 0:
           return -1
       if arr[curr] + curr>=n-1:
           return jump+1
       jump+=1
   return jump

print(minJumps([1,3,5,0,0,0,0,0,0,0,0], 11))
print(minJumps(list(map(int, "32 54 12 52 56 8 30 44 94 44 39 65 19 51 91 1 5 89 34 25 58 20 51 38 65 30 7 20 10 51 18 43 71 97 61 26 5 57 70 65 0 75 29 86 93 87 87 64 75 88 89 100 7 40 37 38 36 44 24 46 95 43 89 32 5 15 58 77 72 95 8 38 69 37 24 27 90 77 92 31 30 80 30 37".strip().split())),
               84))
