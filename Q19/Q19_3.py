# Write your code here!
# Your code must give results for word counts on all
# three sample texts given to get full points.

def lenword(str):
    arrstr = str.split()
    return len(arrstr)

def wordcountintxt(txt):
    f = open(txt, "r")
    str = f.read()
    return lenword(str)

print(wordcountintxt("sample_text_1.txt"))
print(wordcountintxt("sample_text_2.txt"))
print(wordcountintxt("sample_text_3.txt"))