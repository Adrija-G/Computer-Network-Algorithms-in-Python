def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    try:
        distance = hamming_distance(string1, string2)
        print(f"Hamming distance between '{string1}' and '{string2}': {distance}")
    except ValueError as e:
        print(e)