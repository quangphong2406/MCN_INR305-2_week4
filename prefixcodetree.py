class PrefixCodeTree:

    def __init__(self):
        self.symbol = ""
        self.right = None
        self.left = None
        
    def insert(self, codeword, symbol):
        for b in codeword:
            if b==1:
                if self.right is None: 
                    self.right = PrefixCodeTree()
                self = self.right
            else:
                if self.left is None: 
                    self.left = PrefixCodeTree()
                self = self.left
        self.symbol = symbol

    def decode(self, encodedData, datalen):
        node = self 
        decodeData = ""
        binlist = ""
        for byte in encodedData:
            binlist += f'{byte:0>8b}'
        print(binlist)
        for b in range(datalen):
            if binlist[b] == '1': 
                node = node.right
            else:
                node = node.left
            if node.symbol != "": 
                decodeData += node.symbol
                node = self
        return decodeData

codeTree = PrefixCodeTree()

codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1]
}

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

print(codeTree.decode(b'\xd2\x9f\x20', 21))
