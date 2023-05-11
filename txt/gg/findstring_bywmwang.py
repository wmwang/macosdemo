import os

searchWord = input("give me a search keyword:")
filepath = "C:\\Users\\isosoman\\Downloads\\"
print("filepath is ",filepath)
def findfile(input_filepath):
    for file in os.listdir(input_filepath):
        print("file  is ",file )
        if os.path.isfile(file):
            abs = os.path.abspath(file)
            print("abs_file_list:",abs)
            f = open(abs,'r')
            if searchWord in f.read:
                return abs
        else:
            abs = os.path.abspath(file)
            print("abs_dir_list:",abs)
            findfile(file)

findfile(filepath)
print("bye bye~~")
