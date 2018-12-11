import copy

max_size=20

def get_content(infilename):
        with open(infilename) as f:
                content = f.readlines()
        return [s for s in content if s.strip()]#strip the blank lines


def get_sortable(lines):
    results=[]
    resultline=[""]*max_size
    for line in lines:
       leading_whitespaces=len(line) - len(line.lstrip())#warning, spaces and tabs are equivlent
       resultline[leading_whitespaces]=line.lstrip()
       for x in range(leading_whitespaces+1,max_size):
            resultline[x]=""
       results.append(copy.copy(resultline))
       
    return results

def get_sorted(lines):
    lines=get_sortable(lines)
    results=sorted(lines, key=lambda x: "".join(x)) 
    return results

def pretty_print_lines(lines):
    for line in lines:
        leading=""
        saveme=""
        for element in line:
            if (element != ""):
                saveme=element.strip()
                leading+="\t"
            else:
                print leading+saveme
                break


if __name__=="__main__":
    pretty_print_lines(get_sorted(get_content('tabbedsort.input')))
