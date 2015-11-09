import subprocess
import os
import os.path

counter = 0
succeeded = 0
failed = 0
for file in os.listdir("."):
    if file.endswith(".in"):
        counter += 1
        print(" ## Starting %s ##\n" %file)
        output = subprocess.getoutput("java Main < " + file).strip(' \n').replace(' \n', '\n')
        print("Output:\n%s" %output)
        ans_content = ""
        with open(file[:-2] + "ans", 'r', encoding="utf-8") as answerfile:
        	ans_content = answerfile.read().strip(' \n').replace(' \n', '\n')
        print("\nAnswer:\n%s" %ans_content)

        if ans_content == output:
            print("%s succeeded" %file[:-2])
            succeeded += 1
        else:
            print("%s failed" %file[:-2])
            failed += 1

print("\n%d tests. %d succeeded. %d failed" %(counter, succeeded, failed))