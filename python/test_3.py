s = [
    "AB",
    "ABC"
    "ABCD",
    "ABCDE",
]

print(max(map(len, s)))



# s = "-".join([*"ABCDEFGH"])
# print(s[-1:1:-3])



# s ="ABBBAAAAABBBBABBAAABBBBABAA"
# print(len(s.split("AA")))



# s = "ABCDEFGH"
# index = s.index("D")  # или s.find("D")
# print(index)  # Выведет: 3
# print(s.index('d'.upper()))



# mylist = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# a = sorted(mylist)
# a.reverse()

# b = mylist.copy()  
# b.sort()
# b.reverse()

# c = mylist.copy()  
# c.reverse()
# c.sort()

# d = sorted(mylist)  

# print("a:", a) 
# print("b:", b)  
# print("c:", c)  
# print("d:", d)  

# mylist_sorted_desc = sorted(mylist, reverse=True)
# print("Сортировка по убыванию:", mylist_sorted_desc)



# A = [1]
# B = A
# A.pop(0)
# print(A,B)