def with_lambda():
    palindrome = lambda string: string == string[::-1] 
    print(palindrome('ana'))

def without_lambda(string):
    print(string == string[::-1])

if __name__ == '__main__':
    palindrome("ana")
    with_lambda()
