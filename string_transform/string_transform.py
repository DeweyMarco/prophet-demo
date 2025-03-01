import re
import hashlib
import base64

def complex_string_transform(input_string):
    """
    Performs multiple complex transformations on a given string.

    Args:
        input_string: The string to transform.

    Returns:
        The transformed string.

    Example:
        Input:  "This is a test string 1234."
        Output: "LjQzMjEgVGFWZUdmIGdGckcgTiBGdiBmVnVHZDgxNmMxNGU="
    """

    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    reversed_string = input_string[::-1]
    swapped_string = "".join(
        char.upper() if i % 3 == 0 else char.lower()
        for i, char in enumerate(reversed_string)
    )

    shift = len(input_string) // 2
    shifted_string = "".join(
        chr((ord(char) - ord("a") + shift) % 26 + ord("a")) if "a" <= char <= "z"
        else chr((ord(char) - ord("A") + shift) % 26 + ord("A")) if "A" <= char <= "Z"
        else char
        for char in swapped_string
    )

    inserted_string = ""
    for char in shifted_string:
        inserted_string += char

    regex_pattern = r"([aeiouAEIOU])([0-9])"
    regex_replacement = r"\2\1" 
    regex_string = re.sub(regex_pattern, regex_replacement, inserted_string)

    hash_object = hashlib.sha256(regex_string.encode())
    hash_hex = hash_object.hexdigest()
    truncated_hash = hash_hex[:8]  

    final_string = regex_string + truncated_hash

    encoded_string = base64.b64encode(final_string.encode()).decode('utf-8')

    return encoded_string

# Example usage:
test_string = "This is a test string 1234."
transformed_string = complex_string_transform(test_string)
print(f"Original string: {test_string}")
print(f"Transformed string: {transformed_string}")