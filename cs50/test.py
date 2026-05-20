import re

text = "apple,banana;orange grape"

print(re.split(r"[,;\s]+", text, maxsplit=1), max([3]))