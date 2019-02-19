import os
def rename_files():
    '''change the file name'''
    
    #get the current working directory path
    saved_path = os.getcwd()

    #change the cwd to file containing folder
    os.chdir("/home/vashu/Desktop")

    #get all the file names from the Desktop folder
    file_list = os.listdir("/home/vashu/Desktop")
    print(file_list)

    #for each file in the folder, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(file_name.maketrans('','','0123456789')))
    
    #return back to the previous working directory
    os.chdir(saved_path)
    
rename_files()