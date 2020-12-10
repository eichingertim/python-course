def check_sum(num):
    checksum = 0
    for i in str(num):
        checksum += int(i)
    return checksum

print(check_sum(345))
