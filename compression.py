from struct import pack

# taking a path of input text file and stored in variable named in_file
in_file = 'C:/Users/User/Desktop/Masters/Sem-4/Information_Transmission_System/Project/sample.txt'

#taking number of bits
n = 256

#determining maximum size of table
table = pow(2,int(n))   

#opening our input file   
file = open(in_file)

#reading our input file and stored it in a variable named data                 
actual_data = file.read()                      

# initializing the size of dictionary.
d_size = 256                   
dictionary = {chr(a): a for a in range(d_size)}    

#defining null string to append the symbols in dictionary
string = ""             

#determining a variable to store compressed data
processed_data = []    

# Lempel-Ziv compression algortihm
for character in actual_data:                     
    #get input symbol and stored it a variable named value
    value = string + character 
    
    #if the value is already present in dictionary then it will be stored in a variable else it will append in dictionary
    if value in dictionary: 
        string = value
    else:
        processed_data.append(dictionary[string])
        d_length = len(dictionary)
        if(d_length <= table):
            dictionary[value] = d_size
            d_size += 1
        
        string = character

if string in dictionary:
    processed_data.append(dictionary[string])

# storing the compressed data into a file
output = in_file.split(".")[0]
compressed_file = open(output + "_compressed.lzw", "wb")

#processed data will be written in compressed file 
for info in processed_data:
    compressed_file.write(pack('>H',int(info)))
    
compressed_file.close()
file.close()
