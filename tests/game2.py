


#myFile=open("newFile.txt", "w")
#myFile.write("what a looney tune !")

#gamewords = open("newFile.txt", "r")
#gamewords



#a_dictionary = {}
#a_file = open("newFile.txt", "r")
#for line in a_file:
#    key, value = line.split()



#    a_dictionary[key] = value




#file_variable = open('newFile.txt',"r")
#all_lines_variable = file_variable.readlines()

#file_variable.readlines(0)

#fileName=open("newFile.txt","r")
#lines = [i for i in fileName.readlines()]


funct=[]
variable1 = open("newFile.txt", "r")
funct = variable1.read().splitlines()
variable1.close()
print(funct)
