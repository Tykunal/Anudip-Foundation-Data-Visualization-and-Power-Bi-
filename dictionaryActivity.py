from tabulate import tabulate
studentRecord = [["stdId", "stdName", "standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"],
           ["std101", "Ashish Kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
           ["std102", "Abhishek kumar", "10th", 14, 85, 45, 48, 90, 45, 313],
           ["std103", "Aman", "10th", 15, 23, 56, 78, 78, 67, 302],
           ["std104", "Rahul", "10th", 14, 45, 67, 45, 45, 56, 258],
           ["std105", "Ruby", "10th", 13, 89, 67, 89, 93, 65, 403],
           ["std106", "Suman", "10th", 13, 90, 46, 67, 67, 67, 337],
           ["std107", "Saurabh", "10th", 15, 45, 23, 34, 45, 34, 181],
           ["std108", "Sumit", "10th", 14, 23, 45, 67, 78, 90, 303],
           ["std109", "Kamlesh", "10th", 15, 45, 56, 78, 99, 67, 345],
           ["std110", "Rohan", "10th", 15, 34, 12, 24, 45, 56, 171]
           ]

# Initialize an empty 2D dictionary
dict = {}
header = studentRecord[0]
k = 0
# Iterate over student records
for i in range(1, len(studentRecord)):
    tempDict = {}
    for j in range(len(header)):
        tempDict[header[j]] = studentRecord[i][j]
    dict[k] = tempDict
    k+=1

# print(dict)
print("Original Dictionary: \n")


# print(*header, end=" ")
# print("\n")
# print(tabulate([dict[key] for key in dict],  tablefmt="grid"))

# for i in range(len(header)):
#     print(header[i] , end=" ")

print("\n")
for i in range(len(dict)):
    for j in header:
        print(f"|{j}:{dict[i][j]}|", end=" ")
        # print(f"|{dict[i][j]}|", end=" ")
    print("\n-------------------------------------------------------")



# Display the students whose marks in English is greater than 50.

print("\nstudents whose marks in English is greater than 50: ")
print("-------------------------------------------------------")

for i in range(len(dict)):
    if(dict[i]["Maths"]> 50):
        print(dict[i]["stdName"] ,"is having marks in english greater than 50.")


print("\n Top 4 scorers of Maths: ")
print("-----------------------------")

highMarks = []
count = 1

for i in range(len(dict)):
    highMarks.append(dict[i]["Maths"])

highMarks.sort(reverse=True)
print(highMarks)


for mark in highMarks:
    for i in range(len(dict)):
        if dict[i]["Maths"] == mark:
            if count <= 4:
                print(dict[i]["stdName"] , f"is of age" ,dict[i]["Age"], f"and secured {count} position.")
                count += 1
            else:
                break
    if count > 4:
        break


# Task 3 Below 3 scorer in Computers.

print("\n Below 3 scorers of Computers: ")
print("-----------------------------")

lowMarks = []

for i in range(len(dict)):
    lowMarks.append(dict[i]["Computer"])

lowMarks.sort()
print(f"Low Marks: {lowMarks}")

count = 0

for mark in lowMarks:
    for i in range(len(dict)):
        if mark == dict[i]["Computer"]:
            if(count<3):
                print(dict[i]["stdName"], "is among below 3 scorer in Computers with", dict[i]["Computer"], "marks." )
                count+=1
            else: break

    if(count>3):
        break    