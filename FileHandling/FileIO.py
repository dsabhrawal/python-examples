#We will see examples for File operations

# Opening a file in read mode to display the content
data = open('data.txt','r') 

#print(data.readlines()) #Prints list of lines

#Print each line of file
for line in data:
    print(line)

for line in data.readlines():
    print(line)

data.close()

#---------------------------
#Opening the file in write mode
#File will be overwritten if file exist
data = open('data1.txt','w')

data.write('This is line 1 \n')
data.write('This is line 2 \n')
data.write('This is line 3 \n')
data.write('This is line 4 \n')

data.close()

#Open a file in append mode

data = open('data.txt','a')

data.write('I am appending this line')

data.close()
