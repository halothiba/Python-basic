marks = int(input("Enter your Marks: "))
if 0<= marks <= 100:
    if marks >= 75:
        print("Grade : A")
    elif marks >= 65:
        print("Grade : B")
    elif marks >= 55:
        print("Grade : C")
    elif marks >= 45:
        print("Grade : S")
    else:
        print("Grade : F")
else:
    print("Invalid marks! please enter marks between 0 and 100.")
    