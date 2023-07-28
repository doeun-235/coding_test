'''
let A,B are non-decreasing and n(A) == n(B) == N
(A=[a1,...,a(N-1),aN], B=[b1,...,b(N-1),bN])

use : min_prod(A,B) == a1 * bN + ... + aN * b1
(The proof is on the end of a code.)
'''

def solution(A,B):
    A= sorted(A)
    B= sorted(B,reverse=True)
    return sum(list(map(lambda i : A[i]*B[i], list(range(len(A))))))

'''
-WANT to SHOW-
P : min_prod(A,B) == a1 * bN + ... + aN * b1

1) if N == 1
a1 b1 + a2 b2 >= a1 b2 + a2 b1 since a1(b1-b2) >= a2(b1-b2)

2) if P holds when N == M-1, then P hold when N == M
min_prod(A,B) = min(a1bN + min_prod([a2,...],[b1,...b(N-1)]),
					..., a1b1 + min_prod([a2,...],[b2,...]))

let G(i): = a1bi + min_prod(A without a1 , B without bi)
WANT to SHOW : i<j -> G(i) >= G(j)
since, min_prod(A without a1, B without bi) = 
	if i != N  : a2bN + a3b(N-1) + ... + a(N-i+1) b(i+1) + a(N-i+2) b(i-1)
    				+ ... + aNb1
	if i == N  : a2b(N-1) + aNb1

G(i) - G(j) = (a1bi + a(N-j+2)bj + a(N-j+3)b(j-1) + ... +a(N-i+1)b(i+1))
				- (a1bj + a(N-j+2)b(j-1) + ... + a(N-i)b(i+1)+a(N-i+1)bi)
= a1(bi-bj) + a(N-j+2)(bj-b(j-1)) + ... + a(N-i+1)(b(i+1)-bi)
>= a1(bi-bj) + a1(bj-bi) = 0

Thus, P holds.
'''
