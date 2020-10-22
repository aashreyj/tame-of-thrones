import sys

# initial definition of constants used in code
# changing these will change constants throughout the module
RULING_KINGDOM_NAME = 'SPACE'
ALLIES_REQUIRED = 3
NUMBER_OF_CHARACTERS = 26
FIRST_CHARACTER = 'A'
FAILURE_MESSAGE = "NONE\n"


# utility function to get emblem of kingdom given the kingdom name
def get_kingdom_emblem(kingdom_name):
    kingdom_emblem = {
        'SPACE': 'GORILLA',
        'ICE': 'MAMMOTH',
        'LAND': 'PANDA',
        'AIR': 'OWL',
        'WATER': 'OCTOPUS',
        'FIRE': 'DRAGON',
    }
    # return emblem from kingdom-emblem mapping
    return kingdom_emblem[kingdom_name]


# class to define a Message
class Message:
    # constructor method
    def __init__(self, message_content):
        self.message_content = message_content

    # method returns a dictionary containing the counts of all characters present
    # in the message text body
    def get_char_map(self):
        characters_in_decrypted_message = {}  # dictionary to be returned as hash table

        # iterate over content of decrypted message
        for character in self.message_content:
            # if it is present in the dictionary, increment its count
            if character in characters_in_decrypted_message:
                characters_in_decrypted_message[character] += 1
            else:
                # else insert character in dictionary with initial count 1
                characters_in_decrypted_message[character] = 1

        # return prepared dictionary
        return characters_in_decrypted_message


# class to define a Kingdom
class Kingdom:
    # constructor method
    def __init__(self, kingdom_name, kingdom_emblem):
        self.__kingdom_name = kingdom_name
        self.__kingdom_emblem = kingdom_emblem

    # getter method to return name of Kingdom
    def get_name(self):
        return self.__kingdom_name

    # method that allows a kingdom to decrypt the incoming message
    # using the number of characters in its emblem as the cipher key
    def decrypt(self, encrypted_message):
        decrypted_message = str()

        # number of shifts required, based on the number of characters in the Kingdom's emblem
        caesar_cipher_shifts = len(self.__kingdom_emblem)

        # iterate over the content of the encrypted message
        # and decrypt it using Caesar Cipher rotation
        for character in encrypted_message.message_content:
            # at first, the distance of the character from 'A' is determined
            # as encryption required forward shift by 'key' steps, decryption will take backward shift by same amount
            # backward movement by 'key' steps is equivalent to forward movement by 26 - key steps
            # final result is obtained by taking mod 26 since we may go beyond range of alphabets
            # character is obtained by adding ASCII value of character
            offset_of_character = ord(character) - ord(FIRST_CHARACTER)
            shifts_required = NUMBER_OF_CHARACTERS - caesar_cipher_shifts
            reverse_offset = ord(FIRST_CHARACTER)
            decrypted_message += chr(((offset_of_character + shifts_required) % NUMBER_OF_CHARACTERS) + reverse_offset)
        return decrypted_message

    # method that lets the kingdom decide if it wants to give allegiance to sender kingdom
    # by checking if the decrypted message contains all characters of the receiver kingdom's
    # emblem or not
    def give_allegiance(self, decrypted_message):

        # dictionary to store counts of characters
        characters_in_decrypted_message = decrypted_message.get_char_map()

        # iterate over characters of the kingdom's emblem
        for character in self.__kingdom_emblem:
            # if current character is not present in the original dictionary at all, or for the given number of times
            # the process fails, and the receiver kingdom does not ally with the sender kingdom
            if character not in characters_in_decrypted_message or characters_in_decrypted_message[character] == 0:
                return False
            # if the character is found, its count is decremented by 1
            characters_in_decrypted_message[character] -= 1

        # if iteration is complete, then the allegiance is given
        return True


# class to define allied kingdoms
class Allies:
    # constructor method
    def __init__(self):
        self.__allied_kingdoms = list()

    # method to add new ally to the list of allied kingdoms
    def add_new_ally(self, ally_kingdom_name):
        if ally_kingdom_name not in self.__allied_kingdoms:
            self.__allied_kingdoms.append(ally_kingdom_name)

    # to check if the ruling kingdom was able to get sufficient allies or not
    def are_allies_sufficient(self):
        if len(self.__allied_kingdoms) >= ALLIES_REQUIRED + 1:
            return True
        else:
            return False

    # if the ruling kingdom is able to gather sufficient allies
    # then the names of all ally kingdoms are printed to the console
    def print_allies(self):
        for index in range(len(self.__allied_kingdoms) - 1):
            sys.stdout.write(str(self.__allied_kingdoms[index]) + ' ')
        sys.stdout.write(str(self.__allied_kingdoms[-1] + '\n'))


# main function
def main():
    # get input file location from command line and open the input file in reading mode
    input_file_location = sys.argv[1]
    input_file = open(str(input_file_location), 'r', encoding='utf-8')

    # RULING_KINGDOM_NAME kingdom is the ruling kingdom and will send messages to all other kingdoms
    ruler_kingdom = Kingdom(RULING_KINGDOM_NAME, get_kingdom_emblem(RULING_KINGDOM_NAME))

    # list of kingdoms that have given their allegiance to the ruling kingdom
    allied_kingdoms = Allies()
    allied_kingdoms.add_new_ally(ruler_kingdom.get_name())

    # read the input file line by line
    for line in input_file:
        # convert lines to list
        line_list = [str(word) for word in line.split()]
        kingdom_name = str(line_list[0])  # first word on each line is the name of the receiver Kingdom
        line_list.pop(0)  # it is removed from the list to process the message

        # iterate over the words in the list to make a single string
        message_content = str()
        for word in line_list:
            message_content += word

        # kingdom object to represent the current receiver kingdom
        kingdom = Kingdom(kingdom_name, get_kingdom_emblem(kingdom_name))

        # message object to represent the currently encrypted message
        encrypted_message = Message(message_content)

        # message object to represent the message that has been decrypted by the receiving kingdom
        decrypted_message = Message(kingdom.decrypt(encrypted_message))

        # check if the kingdom is ready to give its allegiance to the ruling kingdom
        # if so, add the kingdom name to that list of ally kingdoms
        if kingdom.give_allegiance(decrypted_message):
            allied_kingdoms.add_new_ally(kingdom.get_name())

    # display the result of the operation to the console
    if allied_kingdoms.are_allies_sufficient():
        allied_kingdoms.print_allies()
    else:
        sys.stdout.write(FAILURE_MESSAGE)

    # close the input file after processing
    input_file.close()


# execute the main method
if __name__ == "__main__":
    main()
