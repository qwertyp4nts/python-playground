from cs50 import get_string
import re


def main():
    h = get_string("Number: ")
    if re.search("^\d{13,16}$", h):
        if re.match("^[3][4|7](\d{13})$", h):
            if luhns_algorithm(h) is 1:
                print("AMEX")
        elif re.match("^[5][1-5](\d{14})$", h):
            if luhns_algorithm(h) is 1:
                print("MASTERCARD")
        elif re.match("^[4](\d{12}|\d{15})$", h):
            if luhns_algorithm(h) is 1:
                print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


def luhns_algorithm(h):
    h_length = len(h)
    array = []
    counter = 0
    for c in h:
        array.append(int(c))
        counter += 1
        
    sum = 0
    # multiply every 2nd number in the array (in reverse order) by 2
    for i in range(h_length-2, -1, -2):
        array[i] *= 2
        # add those products’ digits
        backToStr = str(array[i])
        for j in backToStr:
            sum += int(j)
        # print(array[i])
    
    # Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):
    for m in range(h_length-1, -1, -2):
        sum += array[m]
    # print(sum)
    
    if sum % 10 == 0:
        return 1
    return 0

  
main()