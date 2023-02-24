## Auto file sorter 2023

import  os, shutil # shell utilities
path = r"C:\...../"
cwfolder = os.listdir(path)

##create folders 
folder_names = ['csv files','image files','text files','pdf files']
for file in range(len(folder_names)):
    if not os.path.exists(path+folder_names[file]):
        #print(path + folder_names[file])
        os.makedirs(path+folder_names[file])

### move the files to right folders        
for file in cwfolder:
    if '.csv' in file and not os.path.exists(path + 'csv files/'+file):
        shutil.move(path+file,path+'csv files/'+file)
    elif '.JPG' in file and not os.path.exists(path + 'image files/'+file):
        shutil.move(path+file,path+'image files/'+file)
    elif '.png' in file and not os.path.exists(path + 'image files/'+file):
        shutil.move(path+file,path+'image files/'+file)
    elif '.txt' in file and not os.path.exists(path + 'text files/'+file):
        shutil.move(path+file,path+'text files/'+file)
    elif '.pdf' in file and not os.path.exists(path + 'pdf files/'+file):
        shutil.move(path+file,path+'pdf files/'+file)
