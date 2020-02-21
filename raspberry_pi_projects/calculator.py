from ssdisp import seven_segment_display as display

if __name__ == "__main__":
    a = int(input("First integer: "))
    display(a)
    b = int(input("Second integer: "))
    display(b)
    input("a + b = ?")
    sum_num = a + b
    display(sum_num)
