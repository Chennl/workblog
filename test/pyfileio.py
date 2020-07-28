with open('./test/2201.txt','r',encoding='utf8') as fin:
    lineno=1
    for line in fin:
        print(line)
        lineno= lineno + 1
        if lineno>50:
            break
       
 