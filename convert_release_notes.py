import subprocess
import os

DOC_SRC_DIR = r'C:\\Users\\Raoul.Grolle\\RTD\\rtd-tutorial\\docs\\source\\Release_Notes\\Word-files'
DOC_TGT_DIR = r'C:\\Users\\Raoul.Grolle\\RTD\\rtd-tutorial\\docs\\source\\Release_Notes\\markdown'


def convert_all_docx_to_md(files):
    for i in range(len(files)):
        file = files[i]
        if " " in file:
             files[i] = os.rename(file, file.replace(" ", "_"))
             
        if file.endswith(".docx"):
                print(file)
                new_name = file.replace(".docx",".md")
                print(new_name)
                print(DOC_TGT_DIR)
                subprocess.run("pandoc " + file + " -o " + DOC_TGT_DIR + "\\"+ new_name + " -t markdown --extract-media=..\\markdown\\images")
                #subprocess.run("pandoc -f docx -t markdown_strict " + file + " -o " + DOC_TGT_DIR + "\\"+ new_name)
    return

def convert_html_tables_to_md():
     raise Exception("Not implemented")
os.chdir(DOC_SRC_DIR)
print('cwd: ' + os.getcwd())
files = os.listdir()
print(files)

if(os.path.exists(DOC_TGT_DIR)):
     convert_all_docx_to_md(files)
    
else:
    os.mkdir(DOC_TGT_DIR)
    convert_all_docx_to_md(files)

os.chdir(DOC_TGT_DIR)

md_files = os.listdir()