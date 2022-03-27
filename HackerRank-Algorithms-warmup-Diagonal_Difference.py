def diagonalDifference(arr):
    # Initialize Primary diagonal value as Zero
    prim_diag_val = 0

    # This for loop is to get the 1st row 1st value, 2nd row second value and so on... and add those values
    for i in range(0, n):
        prim_val = arr[i][i]
        prim_diag_val += prim_val
            
    # Initialize Secondary diagonal value as Zero
    sec_diag_val = 0

    # This ind variable is to get second index of array [0][2] here, we got 0 from loop and 2 from the formula j = ind - i
    ind = n - 1

    # This for loop does the same as previous for loop as reverse.. e.g., 1row last value, second row last second value and so on....
    for i in range(0, n , 1):
        j = ind - i
        sec_val = arr[i][j]
        sec_diag_val += sec_val
    
    # Perform the difference between primary and secondary diagonal and store absolute Solution value in the variable 'Solution', then return it to the called function
    Solution = prim_diag_val - sec_diag_val
    return abs(Solution)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    # This for loop is to convert the input into a list
    # A line from the user consists of some numbers seperated by spaces are converted into list
    # Then it will added to the another list.. simply we can say it as 2D Array 
    for _ in range(n):
        lst = list(map(int, input().rstrip().split()))

        # This if else part is to check number of integers in a line matches with the 'n' value
        if len(lst) == n:
            arr.append(lst)
        else:
            print("Invalid number of inputs")
            break

    # To look at the 2D Array(arr) use print function
    # print(arr)

    
    result = diagonalDifference(arr)
    print(result)
    
