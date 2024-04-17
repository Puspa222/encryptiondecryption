**README**

## Encryption and Decryption of Messages

This Python script facilitates the encryption and decryption of messages using a custom algorithm. The algorithm is designed to obscure the original message in a unique and randomized manner for encryption, and then reverse the process for decryption.

### How it Works

#### Encryption Process

1. **Input**: The user provides a message to encrypt.
2. **Message Parsing**: The input message is split into individual words.
3. **Encryption**: 
    - For each word:
        - If the word has a length of 1:
            - Random characters are generated before and after the word.
        - If the word has a length of 2:
            - Random characters are generated before and after the reversed word.
        - If the word has a length greater than 2:
            - Random characters are generated at both ends, and the middle characters are reversed.
    - The encrypted message is constructed by concatenating the randomized characters and the encrypted words.
    
#### Decryption Process

1. **Input**: The user provides the encrypted message.
2. **Decryption**:
    - The encrypted message is split using a special delimiter into individual encrypted words.
    - For each encrypted word:
        - If the word has a length of 6, it's decrypted as is.
        - If the word has a length of 8, the middle characters are reversed.
        - If the word has a length greater than 8, the process is reversed from encryption.
    - The decrypted words are concatenated to form the original message.

### Usage

1. **Encryption**: Run the script and input the message you want to encrypt when prompted.
2. **Decryption**: Input the encrypted message when prompted.

### Customization

- The script utilizes randomization and string manipulation for encryption and decryption. Adjustments can be made to the algorithm for different levels of security and obfuscation.

### Requirements

- Python 

### Contributions

Contributions to improve the encryption algorithm, enhance user experience, or address any issues are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
