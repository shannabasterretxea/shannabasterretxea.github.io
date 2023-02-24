#This code counts the character frequency in a text


#Open and read chosen text file
with open( 'lorem.txt', 'r') as input:
    text=input.read ()

#Loop the string to count each character and print each character with its frequency.
def main(): 
    if __name__ == "__main__":
        main()
    known = ''
    for char in text:
        new = known.count(char)
        if new == 0:
            known = known + str(char)
            count  = text.count(char)
            print(str(char) + ": " + str(count))
