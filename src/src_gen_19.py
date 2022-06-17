from typing import List

def sat196(primes: str, s="This is a test of whether you would want to do such strange puzzles"):

    def is_prime(n):
        return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

    prime_words = primes.split()
    i = 0
    for word in s.split():
        if is_prime(len(word)):
            assert prime_words[i] == word
            i += 1

    return i == len(prime_words)
def sol196(s="This is a test of whether you would want to do such strange puzzles"):
    """Find the string consisting of all the words whose lengths are prime numbers

    "A bird in the hand is worth two in the bush" => "in the is worth two in the"
    """
    def is_prime(n):
        return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))

    return " ".join(w for w in s.split() if is_prime(len(w)))
# assert sat196(sol196())
