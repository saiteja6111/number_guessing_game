#scope
#local vs global

#global scope

enemies = 1
def increase_enemies():
    #local scope
    enemies =  2
    print(f"enemies inside function : {enemies}")

increase_enemies()
print(f"enemies outside function : {enemies}")

#global constants

#it should be written in the upper case only ALL_CAPS

PI = 3.14

def sum(a):
    a = a + PI
    print(a)

sum(10)


