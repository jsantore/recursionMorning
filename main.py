
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

#print(factorial(5))

def is_palendrome(string):
    if string =='':
        return True
    if len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palendrome(string[1:-1])

def main():
    string_to_test = input("put in a string to test:")
    answer = is_palendrome(string_to_test)
    print(answer)

main()