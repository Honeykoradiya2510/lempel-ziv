from struct import unpack

# taking the path of compressed file as an input and stored it a variable named in_file
in_file='C:/Users/User/Desktop/Masters/Sem-4/Information_Transmission_System/Project/sample.lzw'

#taking number of bits
n = 256

# determining the maximum size of dictionary.
table_size = pow(2,int(n))

#opening our input file   
file = open(in_file, "rb")

compressed_data = []
next_code = 256

#determining a variable to store decompressed data
decompressed_data = ""
string = ""

while True:
    #reading the compressed file and stored it a variable named processed_data
    processed_data = file.read(2)
    d = len(processed_data)
    if d != 2:
        break
    (data, ) = unpack('>H', processed_data)
    compressed_data.append(data)

# determining the size of dictionary.
dictionary_size = 256
dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

# Lempel-Ziv Decompression algorithm
for code in compressed_data:
    if not (code in dictionary):
        dictionary[code] = string + (string[0])
    decompressed_data += dictionary[code]
    if not(len(string) == 0):
        dictionary[next_code] = string + (dictionary[code][0])
        next_code += 1
    string = dictionary[code]

# storing the decompressed string into a file.
out = in_file.split(".")[0]
decompressed_file = open(out + "_decoded.txt", "w")
#original data will be written in output file
for data in decompressed_data:
    decompressed_file.write(data)
    
decompressed_file.close()
file.close()
