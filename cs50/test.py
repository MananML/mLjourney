class Vault:
    def __init__(self, galleons=0, sickles = 0, knuts = 0) -> None:
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        return Vault(galleons, sickles, knuts)
    
    def __str__(self) -> str:
        return f"{self.galleons}, {self.sickles}, {self.knuts}"
                 

potter = Vault(100, 30, 90)
wesley = Vault(1, 2, 3)

total = potter + wesley

print(total)
