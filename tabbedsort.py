import copy

max_size=100

def get_sortable(lines):
    results=[]
    resultline=[""]*max_size
    
    for line in lines:
       leading_whitespaces=len(line) - len(line.lstrip())#warning, spaces and tabs are equivlent
       print leading_whitespaces
       resultline[leading_whitespaces]=line.lstrip()
       for x in range(leading_whitespaces+1,max_size):
            resultline[x]=""

       results.append(copy.copy(resultline))
       print resultline
       #find the first entry
       #overright the remaining tabs until max size 
       



    return results
