# Encrypt this

## Acknowledgments:

I thank [yvonne-liu](https://www.codewars.com/users/yvonne-liu) for the idea and for the example tests :)


## Description:

Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

1. Your message is a string containing space separated words.
2. You need to encrypt each word in the message using the following rules:
    * The first letter must be converted to its ASCII code.
    * The second letter must be switched with the last letter
3. Keepin' it simple: There are no special characters in the input.


## Examples:
```
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
```
