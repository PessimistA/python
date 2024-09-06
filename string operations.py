#counting part
import re
name = input("give the name of the txt file: ")
writing =""

with open(f"{name}.txt","r") as file2:
    writing = str(file2.read()) 

count_word = re.findall(r'[a-zA-Z]+',writing)  
count_letter = re.findall(r'\w',writing)
count_symbol = re.findall(r'[*-+%&^#!"\';.:,]',writing)

print(f"word count {len(count_word)}")
print(f"letter count {len(count_letter)}")
print(f"punctiotion count {len(count_symbol)}")