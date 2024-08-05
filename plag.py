from difflib import SequenceMatcher

with open("testfile1.txt") as file1, open("testfile2.txt") as file2:
    f1data=file1.read()
    f2data=file2.read()
    percent=SequenceMatcher(None,f1data,f2data).ratio()
    print(percent*100)
