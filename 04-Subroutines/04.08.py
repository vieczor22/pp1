#8.	Define a function that displays integer numbers from 1 to N. Then call the function and display numbers from 1 to 15.

def display_integers (N):
    for x in range(1, N + 1):
        print(x, end=" ") 

display_integers(15)
print()
display_integers(25)
