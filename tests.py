# for i in range(0 , 200 , 1):
#     print(i ,'\t=\t',chr(i))

#0 _ 64
#91 _ 96
#123 _ 126

# with open ('word.txt' , 'a' , encoding='utf-8') as file:
#     for i in range (0 , 65 , 1):
#         file.write (f"{chr(i)}\n")
#         #
#     for i in range (91 , 97 , 1):
#         file.write (f"{chr(i)}\n")
#         #
#     for i in range (123 , 127 , 1):
#         file.write (f"{chr(i)}\n")

# words = ['ali' , 'hssd' , 'bibi' , '0123456789'  , ',' , '+' , 'hos']
# with open ('word.txt' , 'r' , encoding='utf-8') as file :
#     for i in file.read():
#         for j in words :
#             if i in j:
#                 words.remove(j)

# word = ['ali' , 'reza']
# word += [' ']
# print (word)

# lst = ['hello' ,'ali', 'hello' , 'world' , 'hello']
# lst2 = []
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)
# print (lst2)

print('6ali'.replace('a', ''))