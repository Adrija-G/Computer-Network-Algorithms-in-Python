def crc_remainder(data, divisor):
    data += "0" * (len(divisor) - 1)
    data = list(data)
    divisor = list(divisor)
    
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == '1':
            for j in range(len(divisor)):
                data[i + j] = str(int(data[i + j]) ^ int(divisor[j]))
    
    remainder = "".join(data)[-len(divisor) + 1:]
    return remainder

def crc_check(data, divisor):
    remainder = crc_remainder(data, divisor)
    
    return all(bit == '0' for bit in remainder)

def main():
    data = input("Enter the data bits: ")
    divisor = input("Enter the divisor (generator polynomial): ")

    remainder = crc_remainder(data, divisor)
    print("CRC Remainder:", remainder)

    is_valid = crc_check(data + remainder, divisor)
    if is_valid:
        print("CRC Check Passed: No Error Detected")
    else:
        print("CRC Check Failed: Error Detected")

if __name__ == "__main__":
    main()
