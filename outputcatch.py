import subprocess
import os
import os.path
for file in os.listdir(""):
    if file.endswith(".in"):
        output = subprocess.getoutput("java -jar test.jar " + file)
        expected_answer = ""
        with open(file[:-3] + "ans", 'r') as answerfile:
            expected_answer = answerfile.read()

        if output == expected_answer:
            print(file, "succeeded")
        else:
            print(file, "failed")



