def check_digit_in_string(n):
    flag = True
    counts_of_dot = 0
    counts_of_minuses = 0
    for i in n:
        if i not in "1234567890.-":
            flag = False
        elif i in "-" and i != n[0]:
            flag = False
        elif i in "-" and counts_of_minuses > 1:
            flag = False
        elif i in "-":
            counts_of_minuses += 1
        elif i in ".":
            counts_of_dot += 1
    if counts_of_dot > 1 or counts_of_minuses > 1:
        flag = False
    if flag == False:
        print(" You have written an incorrect number:", n)
    else:
        if n.isdigit():
            print("You have written a positive even number:", n)
        else:
            if float(n) % 1 != 0:
                if float(n) < 0:
                    print("You have written a negative odd number:", n)
                else:
                    print("You have written a positive odd number:", n)
            else:
                print("You have written a negative even number:", n)


check_digit_in_string(input())