a = 89
def fun():
    global a
    a = 9
    print(a)

fun()
print(a)
# Global keyword is change the global variable ......