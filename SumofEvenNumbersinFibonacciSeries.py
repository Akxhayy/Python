count = int(input("Enter number of test cases: "))
marker = 0
while marker<count:
    series = [0, 1]
    a = 0
    b = 1
    element = 0
    sum = 0
    withinlimit = []
    try:    
        value = int(input("Enter the value : "))
        if value < 0:
            print("The input value cannot be less than or equal to zero")
        elif value == 0:
            print("The output is 0")
        else:
            while series[-1] <= value:
                element = a+b
                a = b
                b = element
                series.append(element)
            print("Every element : ", series)
            print("Even elements : ", end = " ")
            del series[-1]
            for j in series[1:]:
                if j%2==0:
                    print(j, end = " ")
                    sum += j
            print(f"\nThe output is {sum}")
    except ValueError:
        print("The value is to be integer data type.")
    marker+=1