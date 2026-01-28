#   Executing a statement
for EachPass in range (7): # Header of the loop
    print("live", end = "") # Loop body 

#   Count controled loops
for count in range (6):
    print(count, end = "")

#   Loop errors: off-by-one-error
# It's a logic error not a syntax one
for amount in range (1,4):
    print(amount)

#   Traverse through a sequence of data
print(list (range(6)))
print (list (range(1,7)))

#   Steps in range 
print(list (range(1,6,2)))


