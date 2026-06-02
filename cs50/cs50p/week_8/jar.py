class Jar:
    def __init__(self, capacity=12):
        self.cookies = []
        self._capacity = capacity

        if capacity < 0:
            raise ValueError

    def __str__(self):
        return len(self.cookies) * "🍪"

    def deposit(self, n):
        for i in range(n):
            self.cookies.append("🍪")

        else:
            if len(self.cookies) > self._capacity:
                raise ValueError("Full")

    def withdraw(self, n):
        if len(self.cookies) < n:
                raise ValueError("Empty")

        for i in range(n):
            self.cookies.remove("🍪")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return len(self.cookies)
