Algorithm: Lempel-Ziv <br>
Programming Files: compression.py and decompression.py <br>
Input File: sample.txt <br>
Programming language: Python 3.6 <br>
Software Used: Spyder <br>
Output of compression.py: sample.lzw <br>
Output of decompression.py: sample_decoded.txt <br>

Compression: The input file is compressed using the compression.py file. The size of sample input file is 73kb and the output i.e,compressed file(sample.lzw) is of 24kb. The data we get in the compressed file are the ascii values of the original data. The compressed file generated is in non-readable format.

Decompression: Compressed file is taken as input in decompression.py file. The output file generated is same as the original file which is taken as an input in compression.py file. The ascii values of the compressed file is converted to its original format using the decompression algorithm of lempel-ziv.

Run file in command prompt:
1. Set the directory to location where the file is stored in command prompt.
2. To run compression.py write - python compression.py sample.txt("input text file") 256(number of bits)
3. To run decompression.py write - python decompression.py sample.txt("input text file") 256(number of bits)

Run file in Spyder:
1. Mention the path of the file in input variable and number of bits(which should be taken as input). 
2. Click on start symbol to run compression.py file. The path of the file and its directory will appear in the console.
3. Similary, for decompression, mention the path of the file in input variable and number of bits(which should be taken as input).
4. Click on start symbol to run decompression.py file. The path of the file and its directory will appear in the console.

After successful execution of the compression.py, we will get sample.lzw(compressed file) file in the folder. Similarly, after execution of decompression.py, we will get sample_decoded.txt(original file) file. 
