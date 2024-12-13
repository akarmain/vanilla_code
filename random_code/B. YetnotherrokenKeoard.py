def main():
    input_string = input()
    typed_string = []
    last_lowercase = -1  # Index of the last lowercase letter
    last_uppercase = -1  # Index of the last uppercase letter

    for char in input_string:
        if char == 'b' and last_lowercase != -1:
            # Remove the last lowercase letter
            typed_string.pop(last_lowercase)
            # Update last lowercase index
            last_lowercase = next((i for i in range(len(typed_string) - 1, -1, -1) if typed_string[i].islower()), -1)
        elif char == 'B' and last_uppercase != -1:
            # Remove the last uppercase letter
            typed_string.pop(last_uppercase)
            # Update last uppercase index
            last_uppercase = next((i for i in range(len(typed_string) - 1, -1, -1) if typed_string[i].isupper()), -1)
        elif char not in ['b', 'B']:
            typed_string.append(char)
            # Update last lowercase/uppercase index if applicable
            if char.islower():
                last_lowercase = len(typed_string) - 1
            elif char.isupper():
                last_uppercase = len(typed_string) - 1

    return ''.join(typed_string)


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
