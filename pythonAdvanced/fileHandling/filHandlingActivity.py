# l = ["hero", "dashing boy", "genious", "intelligent boy"]
# vowels = ["a", "e", "i", "o", "u"]
# r = [" ", "." ]
# v = 0
# c = 0
# n = 0

# ------------------------------------------------------------------------
# Searching a word
# with open("binaryData.txt", "rb") as file: # Always make sure to change the priority like r or w or a
    # inp = input("Enter the word to be search for: ")
    # for line in file:
    #     if inp.lower() in line.lower():
    #         print(line.strip())
# ------------------------------------------------------------------------
# finding number of vowels , consonants and numbers in a file.
    # for line in file:
    #     for i in line:
    #         if i in r:
    #             continue 
    #         elif i in vowels:
    #             v+=1
    #         elif i.isnumeric():
    #             n+=1
    #         else:
    #             c+=1
    # print(f"Vowels: {v}, Consonants: {c} and nums: {n}")
# ------------------------------------------------------------------------
# Enter id, name and marks of student till the user want.
    # lst = [[],[],[]]

    # while(1):
    #     i = input("Enter your id: ")
    #     n = input("Enter your name: ")
    #     m = int(input("Enter your marks: "))
    #     lst[0].append(i)
    #     lst[1].append(n)
    #     lst[2].append(m)
    #     wish = input("Would you like to continue?[y/n]: ")
    #     if wish.lower() == "no":
    #       break

    # pickle.dump(lst, file)
    # print("Binary File has been created!")
# ------------------------------------------------------------------------
# Code for marks greater than 90 in a binary file.

    # data = pickle.load(file)
    # for i in range(len(data[2])):
    #     if data[2][i] > 90:
    #         print(f"{data[1][i]} has marks greater than 90.")

# ------------------------------------------------------------------------

#Count Words 
# with open("kunal.txt", "w") as file:
#     file.write("Kunal is a good programmer")

# print("Writing File Closed!\n")

# with open("kunal.txt", "r") as file:
#     count = 1
#     # data = file.read(1)
#     # print(data)

#     for line in file:
#         for i in line:
#             if i == " ":
#                 count+= 1
#     print(f"There are {count} words.")

# print("Reading File Closed!\n")

# -------------------------------------------------
# Count the occurrence of word "INDIA" in a file named "india.txt"

# with open("india.txt", "w") as file:
#     while(1):
#         inp = input("Enter the desired text: ")
#         if(inp.lower() == "no" ): break
#         file.write(inp)

# print("Writing to the File india.txt is completed.")

# count = 0
# word = ""

# with open("india.txt", "r") as file:
#     for line in file:
#         size = len(line)
#         for i in range(size):
#             if line[i] == " ":
#                 if word.upper() == "INDIA":
#                     count +=1
#                 else:
#                     word = ""
#             elif i == size-1 :
#                 word += line[i] 
#                 if word.upper() == 'INDIA':
#                     count+=1                               
#             else:
#                 word+=line[i]        
#     print(f"There are {count} INDIA words present.")

#2nd Approach
 
    # word = "INDIA"
    # for line in file:
    #     newLine = line.upper()
    #     count = newLine.count("INDIA")

    # print(f"There are {count} words present for {word} word.")
# print("Reading File Closed!")
        
# ---------------------------------------------------------------------------------
# count and display the lines starting with T in a text file story.txt 

# with open("story.txt", "w") as file:
#     while(1):
#         inp = input("Enter the desired text (if written no or n then condition will break): ")
#         if inp.lower() == "no" or inp.lower() == "n": 
#             break 
#         else:
#             file.write(inp+"\n")

# print("Writing file is closed!")

# with open("story.txt", "r") as file:
#     count = 0
#     for line in file:
#         line_upper = line.upper()  # Rename variable to avoid conflict with built-in str
#         if line_upper.startswith("T"):
#             count += 1
#             print(line)
#     print(f"There are {count} lines present in the story.txt file that start with 'T'.")        

# print("Reading file is closed!")

# ------------------------------------------------------------------------------------------------
# display the words starting with i in file word.txt

# with open("word.txt", "w") as file:
#     while(1):
#         inp = input("Enter the desired words (if written no or n then condition will break): ")
#         if inp in ["no", "n"]: break
#         else : file.write(inp+"\n")

# print("Writing file is closed!")

# with open("word.txt", "r") as file:
#     count = 0
#     for line in file: 
#         words = line.split()
#         for word in words:
#             if word.lower().startswith("i"):
#                 count+=1
#                 print(f"{word} starts with i.")

# print("Reading file is closed!")

# -------------------------------------------------------------------------------------
# display the lines having more than 5 words present in a single line in the file notes.txt .

# with open("notes.txt", "w") as file:
#     while(1):
#         inp = input("Enter the desired words (if written no or n then condition will break): ")
#         if inp in ["no", "n"]: break
#         else : file.write(inp+"\n")

# print("Writing file is closed!")

# with open("notes.txt", "r") as file:
#     for line in file:
#         words = line.split()
#         for word in words:
#             if len(word)>4:
#                 print(f"{line}")
#                 break

# print("Reading file is closed!")