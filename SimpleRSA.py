from Crypto.Util import number
import random

class RSA:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.e = 0
        self.d = 0
        self.n = 0

    def generatePrimes(self):
        n_length = 128
        while True:
            p = number.getPrime(n_length)
            q = number.getPrime(n_length)
            if p != q:
                break
        self.p = p
        self.q = q

    def gcd(self,a,b):
        while b > 0:
            a, b = b, a % b
        return a

    def generateKeys(self):
        self.generatePrimes()
        self.n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        e = random.randrange(1, phi)
        g = self.gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = self.gcd(e, phi)
        self.e = e
        self.d = self.modInverse(self.e, phi)

    def modInverse(self, a, m):
        m0 = m
        y = 0
        x = 1
        if (m == 1):
            return 0
        while (a > 1):
            q = a // m
            t = m
            m = a % m
            a = t
            t = y
            y = x - q * y
            x = t
        if (x < 0):
            x = x + m0
        return x

    def encrypt(self, m):
        cipher = [pow(ord(char), self.e, self.n) for char in m]
        return cipher

    def decrypt(self, c):
        message = [chr(pow(char, self.d, self.n)) for char in c]
        return ''.join(message)

rsa = RSA()
m = 'asdafasdf'
print(m)
rsa.generateKeys()
c = rsa.encrypt(m)
print(c)
d = rsa.decrypt(c)
print(d)
