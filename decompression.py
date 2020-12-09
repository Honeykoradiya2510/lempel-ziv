from struct import unpack

# taking the path of compressed file as an input and stored it a variable named in_file
in_file='C:/Users/User/Desktop/Masters/Sem-4/Information_Transmission_System/Project/sample.lzw'

#taking number of bits
n_bits = 256

# determining the maximum size of dictionary.
table = pow(2,int(n_bits))

#opening our input file   
file = open(in_file, "rb")

#variable to store processed data
c_data = []

bits = 256

#determining a variable to store decompressed data
actual_data = ""

#defining null string
s = ""

# determining the size of dictionary.
d_size = 256
dictionary = dict([(a, chr(a)) for a in range(d_size)])

while True:
    #reading the compressed file and stored it a variable named processed_data
    processed_data = file.read(2)
    d = len(processed_data)
    if d != 2:
        break
    (data, ) = unpack('>H', processed_data)
    c_data.append(data)

# Lempel-Ziv Decompression algorithm
for symbol in c_data:
    if not (symbol in dictionary):
        dictionary[symbol] = s + (s[0])
        actual_data += dictionary[symbol]
    if len(s) != 0:
        dictionary[bits] = s + (dictionary[symbol][0])
        bits += 1
    s = dictionary[symbol]

# storing the decompressed string into a file.
output = in_file.split(".")[0]
decompressed_file = open(output + "_decoded.txt", "w")

#original data will be written in output file
for info in actual_data:
    decompressed_file.write(info)
    
decompressed_file.close()
file.close()
