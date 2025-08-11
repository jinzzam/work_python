file_names = ["file1.py", "file2.txt", "file3.pptx", "file4.doc"]
list1 = []

for i in range(len(file_names)):
    list1.append(file_names[i].split("."))
    print(file_names[i],"=> 파일명 : %s 확장자 : .%s"%(list1[0][0], list1[0][1]))
    list1.clear()


for file_name in file_names : 
    arr = file_name.split('.')
    print("%s=> 파일명 : %s 확장자 : .%s"%(file_name,arr[0], arr[1]))