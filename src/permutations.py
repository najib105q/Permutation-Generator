count = 0

def permute(prefix, remaining):
    global count

    if not remaining:
        count += 1
        print(prefix)
        return

    for i in range(len(remaining)):
        permute(
            prefix + remaining[i],
            remaining[:i] + remaining[i + 1:]
        )

while True:
    print("\nPermutation Generator")
    print("---------------------")
    print("1. Generate Permutations")
    print("2. Quit")

    choice = input("\nChoice: ")

    if choice == "2":
        print("\nGoodbye!")
        break

    if choice != "1":
        print("Invalid choice!")
        continue

    word = input("\nWord: ")

    count = 0

    print("\nPermutations:\n")
    permute("", word)

    print(f"\nTotal permutations: {count}")