from struct import pack

# taking a path of input text file and stored in variable named in_file
in_file = 'C:/Users/User/Desktop/Masters/Sem-4/Information_Transmission_System/Project/sample.txt'

#taking number of bits
n = 256

#determining maximum size of table
table_size = pow(2,int(n))   

#opening our input file   
file = open(in_file)

#reading our input file and stored it in a variable named data                 
data = file.read()                      

# initializing the size of dictionary.
dictionary_size = 256                   
dictionary = {chr(a): a for a in range(dictionary_size)}    

#defining null string
string = ""             

#determining a variable to store compressed data
processed_data = []    

# Lempel-Ziv compression algortihm
for symbol in data:                     
    #get input symbol and stored it a variable named value
    value = string + symbol 
    
    #if the value is already present in dictionary then it will be stored in a variable else it will append in dictionary
    if value in dictionary: 
        string = value
    else:
        processed_data.append(dictionary[string])
        d_length = len(dictionary)
        if(d_length <= table_size):
            dictionary[value] = dictionary_size
            dictionary_size += 1
        string = symbol

if string in dictionary:
    processed_data.append(dictionary[string])

# storing the compressed data into a file
out = in_file.split(".")[0]
compressed_file = open(out + ".lzw", "wb")

#processed data will be written in compressed file 
for info in processed_data:
    compressed_file.write(pack('>H',int(info)))
    
compressed_file.close()
file.close()
