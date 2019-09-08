import subprocess

for i in range(1,10):
    i = str(i)
    bashCommand = "diff chpart"+i+"a.txt chpart"+i+"p.txt"

    with open("chpart"+i+"d.txt","wb") as out, open("stderr.txt","wb") as err:
        subprocess.Popen(bashCommand.split(),stdout=out,stderr=err)

    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()
    #" > chpart"+i+"d.txt"
    #print(output)
    #print(error)
