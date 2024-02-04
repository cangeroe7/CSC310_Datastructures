import string
import random


class CeasarCypherEncryption:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits
        self.charDict = {char: i for i, char in enumerate(self.chars)}

    # Creates a random string of the given length out of lower/upper case letters and digits
    def createString(self, length):
        return ''.join(random.choice(self.chars) for _ in range(length))

    # Creates a list of amount random strings of given length with createString function
    def randomStrings(self, length, amount):
        return [self.createString(length) for _ in range(amount)]

    # Encrypts the given message by given steps in the given direction if there is a space it skips that charachter
    def encryptMessage(self, message, direction, steps):
        encryptedMessage = ""
        for char in message:
            if char == " ":
                continue
            index = self.charDict[char]
            newIndex = (index + direction * steps) % 62
            encryptedMessage += self.chars[newIndex]
        return encryptedMessage

    # Randomly decides a direction and amount of steps (-1 and 1 instead of 0 and 1, so I can multiply the steps by the direction)
    # uses randomStrings to create a list of random strings and then using list comprehension and the encryptMessage function
    # it encrypts the messages and prints them
    def encryptRandomStrings(self, length, amount):
        direction = random.choice([-1, 1])
        steps = random.randint(1, 9)
        messages = self.randomStrings(length, amount)
        encryptedMessages = [self.encryptMessage(
            message, direction, steps) for message in messages]
        print(f"Normal messages: \n{messages}\n\n")
        print(f"Encrypted messages: \n{encryptedMessages}\n")


if __name__ == "__main__":
    test = CeasarCypherEncryption()
    test.encryptRandomStrings(7, 50)
    print("shift 'abcdefg ABCDEFG 0123456' right by 2:",
          test.encryptMessage("abcdefg ABCDEFG 0123456", 1, 2))
    print("shift 'abcdefg ABCDEFG 0123456' left by 2:",
          test.encryptMessage("abcdefg ABCDEFG 0123456", -1, 2))
