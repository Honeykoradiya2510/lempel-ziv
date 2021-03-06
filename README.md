<b>Implementation of Lempel Ziv algorithm</b>

<b> Algorithm:</b> Lempel-Ziv <br>
<b> Programming Files: </b> compression.py and decompression.py <br>
<b> Input File: </b> sample.txt <br>
<b> Programming language: </b> Python 3.6 <br>
<b> Software Used: </b> Spyder <br>
<b> Output of compression.py: </b> sample_compressed.lzw <br>
<b> Output of decompression.py: </b> sample_decompressed.txt <br>

<b> Compression: </b> The input file is compressed using the compression.py file. The size of sample input file is 73kb and the output i.e,compressed file (sample_compressed.lzw) is of 24kb. The data we get in the compressed file are the ascii values of the original data. The compressed file generated is in non-readable format.

<b> Decompression: </b> Compressed file is taken as input in decompression.py file. The output file generated is same as the original file which is taken as an input in compression.py file. The ascii values of the compressed file is converted to its original format using the decompression algorithm of lempel-ziv. The decompressed file is same as the actual input file i.e,sample.txt.

<b> Run file in command prompt: </b> 
1. Set the directory to location where the file is stored in command prompt.
2. To run compression.py write - python compression.py sample.txt ("input text file") 256 (number of bits)
3. To run decompression.py write - python decompression.py sample_compressed.lzw ("input text file") 256 (number of bits)

<b> Run file in Spyder: </b> 
1. Mention the path of the file in input variable and number of bits(which should be taken as input). 
2. Click on start symbol to run compression.py file. The path of the file and its directory will appear in the console.
3. Similary, for decompression, mention the path of the file in input variable and number of bits(which should be taken as input).
4. Click on start symbol to run decompression.py file. The path of the file and its directory will appear in the console.

After successful execution of the compression.py, we will get sample_compressed.lzw (compressed file) file in the folder. Similarly, after execution of decompression.py, we will get sample_decompressed.txt (original file) file. The generated output files are shown below in the folder: 

![Screenshot (15)](https://user-images.githubusercontent.com/45633319/101669246-ae717380-3a1f-11eb-9f78-036f32c8766b.png)
<br><br>
The image of input sample file is shown below: 

![Screenshot (8)](https://user-images.githubusercontent.com/45633319/101059549-64d6e380-355c-11eb-9049-3bcca367c1f5.png)
<br><br>
The image of the compressed file is shown below. It includes ascii value of the original text which is in non-readable format.

![Screenshot (12)](https://user-images.githubusercontent.com/45633319/101669012-533f8100-3a1f-11eb-8b03-e89a1b532589.png)

