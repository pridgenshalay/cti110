first_int = int(input())
second_int = int(input())
if first_int > second_int:
    print("Second integer can't be less than the first.")
else:
    while first_int <= second_int:
        print(first_int, end=' ')
        first_int += 5
    print()
