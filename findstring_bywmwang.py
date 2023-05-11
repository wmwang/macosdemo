import os

searchWord = input("give me a search keyword:")
path = "./txt"
print("filepath is ",path)
def findfile(path):
    print("input_filepath is ",path)
    for file in os.listdir(path):
        if os.path.isfile(file):
            abs = os.path.abspath(file)
            f = open(abs,'r')
            if searchWord in f.read():
                print("i find the file:",abs)
        else:
            abs = os.path.abspath(path+"\\"+file)
            print("abs_dir_list:",abs)
            findfile(abs)

findfile(path)
print("bye bye~~")
