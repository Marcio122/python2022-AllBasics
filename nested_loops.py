#nested loops = the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
 #   for j in range(columns):
  #      print(symbol, end="")
   # print()

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(my_list[1][1])
for list in my_list:
    for row in list:
        print(row)
    #print(my_list)