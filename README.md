# Generate-Password

Generate-Password is a Python script designed to create random passwords with customizable length and character composition. The generated password includes a balanced mix of the following character types:

- 30% Uppercase Letters
- 30% Lowercase Letters
- 30% Digits
- 10% Punctuation

## Configuration

You can customize the password generation by adjusting the following variables in the script:

- `pass_num`: Total number of characters in the password.
- `digits_num`: Percentage of digits in the password.
- `uper_num`: Percentage of uppercase letters in the password.
- `lower_num`: Percentage of lowercase letters in the password.
- `punctuation_num`: Percentage of punctuation characters in the password.

## Dependencies

This script relies on the following Python modules:

- `string`: provides a collection of string constants, including digits, uppercase and lowercase letters, and punctuation.
- `random`: provides functions for generating random numbers and shuffling sequences.

## Suggestions for Improvement

- Unused Imports: Remove unnecessary imports and code, such as `str_uper_lower` and its shuffle.

- Password Generation Logic: Consider using `random.sample` for a more even distribution of characters.

- Password Length: Adjust rounding logic to ensure the total length matches the desired value.

- Unused Variable: Remove the unused variable `cods` at the end of the script.

## Generated Password Example

![Generated Password](https://user-images.githubusercontent.com/105138072/206670689-8e4ae5bd-190f-406a-be78-4c5f5dce8a11.png)

Feel free to customize and enhance the script based on your specific requirements. If you have any questions or need further assistance, don't hesitate to reach out!
