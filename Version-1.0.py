list = [[]]
patternList = [[]]
separator = '\t'
#Function to convert string to float (it had used for file entry)
def cnv_string2float(list):
    patternList=list
    for i in range(len(list)): 
        for j in range(len(list[i])): 
            patternList[i][j] = float(list[i][j]) 
    return patternList
#Class for read from file & out the resualt(input part of program)
class File_entry:
    fileAddress=''
    def __init__(self, fileAddress):
        self.fileAddress = fileAddress
    def read_file(self):
        f = open(self.fileAddress, "r")
        for line in f:
            list.append((line.replace("\n", "")).split(separator))
        f.close()
        patternList=cnv_string2float(list[1:])
        return patternList
    def get_pattern(self): return list
#Main part
if __name__ == '__main__':
    read = File_entry('E:\\Input.txt')
    patternList=read.read_file()
    num_weights=len(patternList[0])-1
    weight=[0]*num_weights
    b_weight=0
#Processing part & output of program
    for i in range(0,len(patternList)):
        for j in range(0,num_weights):
            weight[j]=weight[j]+patternList[i][j]*patternList[i][num_weights]
        b_weight=b_weight+patternList[i][num_weights]
    print('Weghits are : ' , weight)
    print('b is : ' , b_weight)

#To compute percentage error, first we decide to divide patterns to 2 subset that are above and below the line
    above_line=[[]], below_line=[[]]
    for i in range(0,len(patternList)):
        sum=0.0
        for j in range(0,num_weights):
            sum+=patternList[i][j]*weight[j]
        sum+=b_weight
        if sum>=0: above_line.append(patternList[i])
        else: below_line.append(patternList[i])
    print('Above line : ', above_line)
    print('Below line : ', below_line)
#Now it needs to just spify which side is for +1 resault & which side is for -1 resault 
    above_positive_res=0
    above_negative_res=0
    for i in range(1,len(above_line)):
        if above_line[i][2] == 1: above_positive_res+=1
        else: above_negative_res+=1
    below_positive_res=0
    below_negative_res=0
    for i in range(1,len(below_line)):
        if below_line[i][2] == 1: below_positive_res+=1
        else: below_negative_res+=1
#Now we need to determine sides
    side_above=''
    if (above_positive_res>=below_positive_res & above_negative_res>=below_negative_res & above_positive_res>=above_negative_res): side_above='+'
    elif (above_positive_res>=below_positive_res & above_negative_res>=below_negative_res): side_above='-'
    elif (above_positive_res>=below_positive_res): side_above='+'
    elif (above_negative_res<below_negative_res & below_positive_res<below_negative_res): side_above='+'
    elif(above_negative_res<below_negative_res): side_above='-'
    else: side_above='-'
    #Now we know the sides just compute percentage error
    if side_above=='+': sum_error = above_negative_res + below_positive_res
    else: sum_error = below_negative_res + above_positive_res
    percentage_error=(sum_error*100.0)/len(patternList)
    print('Percentage error is : ', percentage_error)

