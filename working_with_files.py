# setting up 
# it cleaner to work inside a folder  sofiles don't clutters your destop.

from pathlib import Path


workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace /"notes.txt"
file_path


# (A) create or overwrite using 'w'
# f =open(file_path, "w", encoding="utf-8")
# f.write("this is the first line in notes.txt\n")
# f.close()

# #(B) safe-create using 'x' (uncomment to try once)
# f = open(workspace /"created_once.txt", "x", encoding="utf-8")

# f.write("this file will only be created if it doesn't exist.\n")
# f.write("ridwan is a goat.\n")
# f.close()

# # open a file
# # opening a file prepares it for reading or writing.

# f = open(file_path, "w", encoding="utf-8") 
# f.write("Replaced the old content with this line.\n")
# f.close()

# write to a file
# writing put text into the file, write() does not add newlines  automatically(you add \n yoiurself)

f = open(file_path, "w", encoding="utf-8")
f.write("shopping list:\n")
f.write(" - Rice\n")
f.write(" - Beans\n")
f.write(" - Garri\n")
f.close()

# Append to a file
# append adds to the end without deleting  what's already there

f = open(file_path, "a", encoding="utf-8")
f.write(" - groundnut oil\n")
f.write(" - maggi\n")
f.close()


# Read from a file
# there are four common ways:
# . read() - whole file has one string
# .read(n) - first n characters
# .readline() - one line
# .readlines() - list of all lines

# read the whole file
f = open(file_path, "r", encoding="utf-8")
content = f.read()
f.close()
print(content)

# Read line-by-line 
f = open(file_path,"r", encoding="utf-8")
print("first line: ", f.readline().rstrip())
print("second line: ", f.readline().rstrip())
f.close()

# read line- by -line
f = open(file_path,"r" , encoding="utf -8")
lines = f.readlines()
f.close()
print("lines list:",[line.rstrip()for line in lines])


# iterate over lines (memory-friendly)
f = open(file_path, "r", encoding="utf-8")
for line in f:
    print("->", line.rstrip())
f.close()

# always close files opened with open(...).
# it flushes(saves any buffered data tyo disk).
#  It releases the OS handle so other programs can use the file.
# - It avoids weird bugs (especially on Windows).
# You have seen f.close() above. But there’s a better way…

# Use with `open(...) as f:` (best practice)
# The with statement automatically closes the file even if an error happens. This is the recommended way.

# write safely
with open(file_path, "w", encoding="utf-8") as f:
    f.write("my Todo list:\n")
    f.write(" - Revise python file handling\n")
    f.write(" - Practice Error handling within a function\n")
    f.write(" - Practice JSON  & CSV\n")


    # Append safely
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(" - Build a small project\n")

# with open(file_path, "x", encoding="utf-8")as f:
#     f.write("this is the first line in notes .txt")


