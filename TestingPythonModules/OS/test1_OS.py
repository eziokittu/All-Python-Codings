import os

# 1
print("---------------------- 01 -----------------------")
# os.getcwd() - Here cwd is a short form for the current working directory.
# The function returns us the path of the directory we are currently in.
# It is important to know about our directory because when we are trying to
# import a file in python, the compiler searches for it in our current directory.
print("Current working directory -", os.getcwd(), "\n")

# 2
print("---------------------- 02 -----------------------")
# dir(os) - It gives us a list of all the functions the OS module is composed of.
print("List of all the functions -\n", dir(os), "\n")

# 3
print("---------------------- 03 -----------------------")
# os.chdir() - It is used in case we want to change our directory.
# The new path is sent inside the parenthesis.
# If we want to access some files or folders from some other directory, we can use it.
os.chdir("D:\Coding Stuff, Editing\Visual Studio Python Codings\Test, Practice")
print("Current working directory -", os.getcwd())
os.chdir("D:\Coding Stuff, Editing\Visual Studio Python Codings")
print("Current working directory -", os.getcwd(), "\n")

# 4
print("---------------------- 04 -----------------------")
# os.listdir( ) - If we want to output the names of all the directories
# at a certain location, we can use this function.
print("list of files in dir -", os.listdir("D:\Coding Stuff, Editing\Visual Studio Python Codings\TestingPythonModules"))
print("list of files in dir -", os.listdir("D:\Coding Stuff, Editing\Visual Studio Python Codings\Test, Practice"), "\n")

# 5
print("---------------------- 05 -----------------------")
# os.rename() - To rename an already existing directory, we use this.
# We send the current name and new name of our directory as parameters.
try:
    os.rename("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/test_1.txt", 
    "D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/test_2.txt")
    print("test_1.txt changed to test_2.txt - using 'rename' function", "\n")
except:
    os.rename("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/test_2.txt", 
    "D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/test_1.txt")
    print("test_2.txt changed to test_1.txt - using 'rename' function", "\n")

# 6
print("---------------------- 06, 07 -----------------------")
# os.mkdir() - To create a new directory or folder.
# The name is sent as a parameter inside the parenthesis.
try:
    os.mkdir("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/FolderCreatedUsing_mkdir")
    print("A new directory created - FolderCreatedUsing_mkdir -- using 'mkdir' function")
    print("Run the program again to delete this directory -- using 'rmdir' function\n")

# 7
# os.rmdir() - It deletes an empty directory.
except:
    os.rmdir("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/FolderCreatedUsing_mkdir")
    print("Directory deleted - FolderCreatedUsing_mkdir -- using 'rmdir' function")
    print("Run the program again to create a new directory - FolderCreatedUsing_mkdir -- using 'mkdir' function\n")

# 8
print("---------------------- 08, 09 -----------------------")
#os.makedirs() - To make more than on directory simultaneously.
try:
    os.makedirs("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/test1/test2/test3")
    print("New directories created - test1/test2/test3 -- using 'makedirs' function")
    print("Run the program again to delete this directories -- using 'removedirs' function\n")

# 9
# os.removedirs() - We can remove all directories within a directory by using removedirs(). 
# [NOTE] - keeps on deleting the parent folders unitl a parent folder is non empty
except:
    os.removedirs("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/test1/test2/test3")
    print("Directories deleted - test1/test2/test3 -- using 'removedirs' function")
    print("Run the program again to create a new directories - test1/test2/test3 -- using 'makedirs' function\n")

# 10
print("---------------------- 10 -----------------------")
# os.environ.get() - It will return us the environment variable.
# The environment variable must be set, or the function will return null.
print(os.environ.get("PATH"))
# print(os.environ())
# 11
print("---------------------- 11 -----------------------")
# os.path.join() - It joins one or more path components.
# We can join the paths by simply using a + sign, but the benefit of using this function
# is that we do not have to worry about extra slashes between the components.
# [NOTE] - it only prints the joined path and does not change the path
print("Using 'os.path.join' -", os.path.join("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/folder_join" ,
"file_join.txt")+"\n")

# 12
print("---------------------- 12 -----------------------")
# os.path.exists() - It returns us a Boolean value, i.e., either true or false.
# It is used to check whether a path exists or not. If it does, then the output will be true, otherwise false.
print("Using 'os.path.exists()' on this path -",
os.path.exists("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/test1_OS.py"))
print("Using 'os.path.exists()' on another path (which does not exist) -",
os.path.exists("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/DoesNotExist.py"), "\n")

# 13
# os.path.is...() - It returns true if the path is an existing regular file.
# os.path.isabs, os.path.isfile, os.path.isdir, os.path.islink
print("---------------------- 13 -----------------------")
print(os.path.isabs("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS"))
print(os.path.isfile("D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/OS/file_join.txt"),"\n")

# 14
# print(os.getppid()) # not important to know now