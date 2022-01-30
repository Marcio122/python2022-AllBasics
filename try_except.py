try:
    x = int(input("Input an integer: "))
    print(x)

except:
    print("Value not an integer...Please try again")

#else:
    #print("nothing went wrong")
finally:
    print("try except finished")