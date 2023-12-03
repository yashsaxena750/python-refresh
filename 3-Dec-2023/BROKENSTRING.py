# function for checking strings starts
def str_check():
    t = int(input())  # taking user input

    # for loop start
    for _ in range(t):

        # defining required variables
        sz = int(input())
        strn = input()
        hf = int(sz / 2)

        # logic to check half string if same
        if strn[:hf] == strn[hf:]:
            print("YES")
        else:
            print("NO")
    # for loop ens here


# function for checking strings ends

# calling function
str_check()
