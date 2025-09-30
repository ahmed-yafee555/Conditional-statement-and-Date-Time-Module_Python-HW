Marks = int(input("Enter a your marks."))


if Marks >= 32:
    print(f"Congratulations you passed the exam")
    if Marks >= 80:
        print(f"And nice you got A+")
        if Marks >= 100:
            print(f"You can't get more than 100")
        else:
            print(f" ")
    else:
        print(f"But, you didn't get an A+")
else:
    print(f"Alas! you failed")
    
boy = True
gender = ("boy" , "girl")[boy]
print("Farah is ", gender)
print("But, Foysal is not", gender)
