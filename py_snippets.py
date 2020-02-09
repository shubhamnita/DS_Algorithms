if __name__ == '__main__':
    marksheet=[]
    #set1 = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name,score])
        #set1.add(score)
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

			
################################################################
			---------formatting ways--------------------
			--------------------------------------------`
print(format((sum(student_marks[query_name])/len(student_marks[query_name])),'.2f'))
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))

########################################################################
################ Running input commands using eval #########################
if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        s = input().split(" ")
        cmd =s[0]
        args =s[1:]
        if cmd!="print":
            cmd+="("+",".join(args)+")"
            eval("l."+cmd)
        else:
            print(l)
        
########################################################################
####################   Occurence of sub-string in string  ####################################################

def count_substring(string, sub_string):
    ct=0
    for i in range(len(string)):
        if(string[i:i+len(sub_string)]==sub_string):
            ct+=1
    return ct

##################Usage of any ######################################################

print(any(c.isalnum() for c in str))


Links: 

https://overiq.com/sqlalchemy-101/crud-using-sqlalchemy-core/ 

https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/ 

 

https://nedbatchelder.com/code/cog/ 
