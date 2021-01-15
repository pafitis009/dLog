import os
import random
from Crypto.Util.number import bytes_to_long, getPrime


def ZKdLogProof(x , g , p, N = 100):
    bits = random.getrandbits(N)
    t = os.urandom(N)
    s = []

    for i in range(N):
        s.append((t[i] + (1 if (bits & pow(2,i)) else 0)*x)%(p-1))
    
    return [bits, s, t]

def verify(y, g, p, bits, s, t, N = 100):
    for i in range(N):
        lhs = pow(g, s[i], p)
        rhs = ((y if (bits & pow(2,i)) else 1)*pow(g, t[i], p))%p

        if lhs != rhs:
            return False

    return True


if __name__ == "__main__":
    p = getPrime(10) #getting a random prime of 10 bits
    g = random.randint(2, p-1)  #generator  
    x = 30  # our secret
    y = pow(g, x, p)

    # We want to prove that we know that g^x = y (mod p)

    proof = ZKdLogProof(x, g, p)

    # returns 3 lists of bits b, randomnesses r, and x^r

    bits = proof[0]
    s = proof[1]
    t = proof[2]

    Result = verify(y, g, p, bits, s, t)

    if(Result):
        print("The proof is correct!")
    else:
        print("The proof is not correct")

