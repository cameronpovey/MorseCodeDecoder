class Node():
    def __init__(self,value=''):
        self.value = value
        self.left = None
        self.right = None
        

class MorseTree():
    def __init__(self):
        self.root = Node()
        
    #just to create the initial tree
    def createTree(self):
        morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '+': '.-.-.', '/': '-..-.', '=': '-...-', '.': '.-.-.-', '(': '-.--.', ')': '-.--.-', ',': '--..--', '?': '..--..', "'": '.----.', ':': '---...', '-': '-....-', '/': '-..-.', '!': '-.-.--', '@': '.--.-.', ';': '-.-.-.', '&': '.-...', '_': '..--.-', '"': '.-..-.', '$': '...-..-', ' ': '/'}
        for x in morseCode: #loops through the dict
            cur = self.root
            for char in morseCode[x]: #loops through each "morse"
                if char == '.':
                    if cur.left == None:
                        cur.left = Node()
                    cur = cur.left
                    
                elif char == '-':
                    if cur.right == None:
                        cur.right = Node()
                    cur = cur.right
            
            #check if node is taken
            if cur.value == "":
                cur.value = x
            else:
                print("Error, atleast 2 characters have the same code")
                exit()
            
    #pre order traversal
    def getMorse(self, node, character, code):
        if node == None:
            return False
        
        elif node.value == character:
            return True
        
        else:
            if self.getMorse(node.left, character, code):
                print(code)
                code.insert(0, ".")
                return True
            elif self.getMorse(node.right, character, code):
                code.insert(0, "-")
                return True

    #encode function
    def encode(self, message):
        encodedMessage = ''
        morse = []
        node = self.root
                
        for char in message.upper():
            print(char)
            if char == " ":
                encodedMessage += "/ "
            else:
                self.getMorse(node, char, morse)
                encodedMessage += "".join(morse) + " "
                morse = []
                
        return encodedMessage.rstrip()
    
    #decode function
    def decode(self, message):
        cur = self.root
        decodedMessage = ''
        
        #loop through each stroke
        for char in message:
            
            if char == '.' and cur.left != None:
                cur = cur.left
                
            elif char == '-' and cur.right != None:
                cur = cur.right
                
            elif char == ' ':
                #at a space log letter
                decodedMessage = decodedMessage + cur.value
                cur = self.root
        
        #when end ofmessage
        decodedMessage = decodedMessage + cur.value
        return decodedMessage
    
    def printTree(self, node=None, level=0, tag=""):
        if node is None:
            node = self.root

        if node.value != '':
            print(' ' * level + tag + node.value)
        else:
            print(' ' * level + tag + ' ')

        if node.right:
            self.printTree(node.right, level + 5, tag="R- ")
            
        if node.left:
            self.printTree(node.left, level + 5, tag="L- ")
    

tree = MorseTree()
tree.createTree() #shortcut to create tree quicker
print(tree.encode("Hello World!"))
print(tree.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--"))
tree.printTree(tag="ROOT")
