def check_sum(num):
    num_str = str(num)
    checksum = 0
    for i in num_str:
        checksum += int(i)
    return checksum

print(check_sum(345))
