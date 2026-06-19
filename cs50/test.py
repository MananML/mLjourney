import argparse

p = argparse.ArgumentParser(description="Meow like a cat")
p.add_argument("-n", default=1, help="number of times to meow", type=int)
args = p.parse_args()

for _ in range(int(args.n)):
    print("Meow")