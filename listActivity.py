from tabulate import tabulate
print("Student Records: ")
print("----------------------------------------------------")
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

header = studentRecord[0]
data = studentRecord[1:]

print(tabulate(data,headers=header, tablefmt="pretty"))

print("Task 1: Students having maths marks more than 50: ")
print("-----------------------------------------------------")


size = len(studentRecord)
for i in range(1,size):
    if(studentRecord[i][6]>=50): 
        print(f"{studentRecord[i][1]} scored more than 50 marks.")


# 2nd task
print("******--------------------*******-----------------------******--------------------\n")
print("Task 2 : Top 4 scorer of Maths: ")
print("--------------------------------")
inde = studentRecord[0].index("Maths")
print("Index for Maths: ",inde )

highMarks = []
# leftWith = []
for i in range(1,size):
    # if (studentRecord[i][6] not in highMarks):
    highMarks.append(studentRecord[i][6])
    # else:
    #     leftWith.append(studentRecord[i][6])

highMarks.sort(reverse=True)
# leftWith.sort(reverse=True)
print("High Marks:", highMarks)

count = 1

for mark in highMarks:
    for i in range(1, len(studentRecord)):
        if studentRecord[i][6] == mark:
            if count <= 4:
                print(f"{studentRecord[i][1]} is of age {studentRecord[i][3]} and secured {count} position.")
                count += 1
            else:
                break
    if count > 4:
        break


# For 2 conditions.
# highMarks = []
# # leftWith = []
# for i in range(1,size):
#     # if (studentRecord[i][6] not in highMarks):
#     highMarks.append(studentRecord[i][6])
#     # else:
#     #     leftWith.append(studentRecord[i][6])

# highMarks.sort(reverse=True)
# # leftWith.sort(reverse=True)
# print("High Marks:", highMarks)

# count = 1

# for mark in highMarks:
#     for i in range(1, len(studentRecord)):
#         if studentRecord[i][6] == mark and studentRecord[i][3]>13:
#             if count <= 4:
#                 print(f"{studentRecord[i][1]} is of age {studentRecord[i][3]} and secured {count} position.")
#                 count += 1
#             else:
#                 break
#     if count > 4:
#         break


# 3rd Task

lowMarks = []
print("******--------------------*******-----------------------******--------------------\n")
print("Task 3 : Bottom 3 scorer in Computers: ")
print("------------------------------")

for i in range(1,len(studentRecord)):
    lowMarks.append(studentRecord[i][8])

# leftMark = []
lowMarks.sort()
print("Low Marks:", lowMarks)
count = 0
for mark in lowMarks:
    for i in range(1, len(studentRecord)):
        if studentRecord[i][8] == mark:
            if count < 3:
                print(f"{studentRecord[i][0]} {studentRecord[i][1]} of age {studentRecord[i][3]} is among the bottom scorers in Computers.")
                count += 1
            elif lowMarks.count(mark) > 1:
                print(f"{studentRecord[i][0]} {studentRecord[i][1]} of age {studentRecord[i][3]} is among the bottom scorers in Computers.")
            else:
                break
    if count >= 3:
        break
