number_of_beans = 140

ans = input("Guess the number of beans in the jar:")
ans = int(ans)

if ans == number_of_beans:
    print("congrats you were right")
elif ans < number_of_beans - 50:
    print("Thats way to low")
elif ans < number_of_beans:
    print("A little low")
elif ans > number_of_beans + 50:
    print("Thats way to high")
else:
    print("A little high")
