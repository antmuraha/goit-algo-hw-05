def build_shift_table(pattern):
    """Creating a shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)
    # For each character in the substring, we set an offset equal to the length of the substring
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # If the character is not in the table, the offset will be equal to the length of the substring
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    # Creating an offset table for a pattern (substring)
    shift_table = build_shift_table(pattern)
    # Initializing the starting index for the main text
    i = 0

    # We go through the main text, comparing it with the subtext
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # We start from the end of the substring

        # Compare characters from the end of a substring to its beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Moving to the beginning of the substring

        # If the entire substring matches, return its position in the text
        if j < 0:
            return i  # Substring found

        # Shift index i based on the shift table
        # This allows you to "jump" over non-matching parts of the text
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # If the substring is not found, return -1
    return -1


if __name__ == "__main__":
    text = "Being a developer is not easy"
    pattern = "developer"

    position = boyer_moore_search(text, pattern)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")
