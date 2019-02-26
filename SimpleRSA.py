from Crypto.Util import number
import random

class RSA:
    def __init__(self):
        self.p, self.q = __generatePrimes()
        self.e = 0
        self.d = 0
        self.n = self.p * self.q

    def __generatePrimes():
        n_length = 1024
        while True:
            p = number.getPrime(n_length)
            q = number.getPrime(n_length)
            if p != q:
                return p,q

    def gcd(a,b):
        """Compute the greatest common divisor of a and b"""
        while b > 0:
            a, b = b, a % b
            return a

    def lcm(a, b):
        """Compute the lowest common multiple of a and b"""
        return a * b / gcd(a, b)

    def __generateKeys(self):
        phi = lcm(self.p, self.q)
        self.e = random.randint(2, tn - 1)
        self.d = __multiplicative_inverse(self.e, phi)

    def __multiplicative_inverse(e, phi):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi

        while e > 0:
            temp1 = temp_phi/e
            temp2 = temp_phi - temp1 * e
            temp_phi = e
            e = temp2
            x = x2- temp1* x1
            y = d - temp1 * y1
            x2 = x1
            x1 = x
            d = y1
            y1 = y
            if temp_phi == 1:
                return d + phi

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        return pow(c, self.d, self.n)
