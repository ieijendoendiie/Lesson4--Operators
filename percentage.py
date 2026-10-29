print("Enter your marks for 4 subjects")
math = int(input("Enter math marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))
hindi = int(input("Enter hindi marks: "))


sum = math+science+english+hindi
print("Total marks: ", sum)

average = (sum/400)*100
print(end= "Percentage is: ")
print(average)