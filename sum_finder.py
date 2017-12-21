

def sum_finder(numbers, wishedsum, partial=[]):
    s = sum(partial)
    
    if s == wishedsum:
        print("sum(%s)=%s" % (partial, wishedsum))
    if s >= wishedsum:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        sum_finder(remaining, wishedsum, partial + [n])


###Import txt File with numbers###
def open_file():
    with open("lotsofnumbers.txt","r") as f:
        numbers = f.read().splitlines()
        numbers = list(map(int, numbers))
    return numbers


numbers = open_file()


###sumfinder(input, result)###
sum_finder(numbers, 44)

print("done.")
