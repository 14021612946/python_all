# f=open("score.txt","w+",encoding="utf-8")
# f.write("罗恩:23:35:44\n")
# f.write("哈利:60:77:68:88:90\n")
# f.write("赫敏:97:99:89:91:95:90\n")
# f.write("马尔福:100:85:90\n")
# f.close()
f=open("scores.txt","r+",encoding="utf-8")
lines=f.readlines()
f.close()
results=[]
for line in lines:
    data=line.split()
    sum=0
    for score in data[1:]:
        sum+=int(score)
    result='%s:%d\n'%(data[0],sum)
    results.append(result)
output=open('result.txt',"w+",encoding="utf-8")
output.writelines(results)
output.close()
