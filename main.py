import morse
import unittest

class TestMorse(unittest.TestCase):
    tree = morse.MorseTree()
    tree.createTree()
    
    def test_encode_us(self):
        self.assertEqual(self.tree.encode('us'), '..- ...')#test encode
        
    def test_decode_us(self):
        self.assertEqual(self.tree.decode('..- ...'), 'us')#test decode (without-capilization) - should fail
        
    def test_decode_us_working(self):
        self.assertEqual(self.tree.decode('..- ...'), 'US')#test decode (with-capilization)
        
    def test_encode_sos(self):
        self.assertEqual(self.tree.encode('SOS'), '... --- ...')#test encode
        
    def test_decode_sos(self):
        self.assertEqual(self.tree.decode('... --- ...'), 'SOS')#test decode (with-capilization)
        
    def test_encode_HW(self):
        self.assertEqual(self.tree.encode('HELLO WORLD!'), '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--')#test decode
        
    def test_decode_HW(self):
        self.assertEqual(self.tree.decode('.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--'), 'HELLO WORLD!')
        
    def test_encode_NewSymbols(self):
        self.assertEqual(self.tree.encode("H,ELL .O?:(WO'+ R)$-D"), '.... --..-- . .-.. .-.. / .-.-.- --- ..--.. ---... -.--. .-- --- .----. .-.-. / .-. -.--.- ...-..- -....- -..')#test new characters
        
    def test_decode_NewSymbols(self):
        self.assertEqual(self.tree.decode('.... --..-- . .-.. .-.. / .-.-.- --- ..--.. ---... -.--. .-- --- .----. .-.-. / .-. -.--.- ...-..- -....- -..'), "H,ELL .O?:(WO'+ R)$-D")#test new characters
        
    def test_decode_incorrect(self):
        self.assertEqual(self.tree.encode("This shouldn't be working due to the incorrect morse code"), "- .... .. ... / ... .... --- ..- .-.. -.. -. .----. - / -... . / .-- --- .-. -.- .. -. --. / -.. ..- . / - --- / - .... . / .. -. -.-. --- .-. .-. . -.-. - / -- --- .-. ... . -.-. --- -.. .")#on purposely is missing the last space - should fail
        
    print("2 fails expected")

if __name__ == '__main__':
    unittest.main()
