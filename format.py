import os


folder_dir = "/Users/attorneyking/Documents/English ngoaingu24h/Xóa mù Tiếng Anh cấp tốc/videos"
files = os.listdir(folder_dir)

# print(files)

for file in files:
    # if file.find(".pdf") < 0:
    #     print(file)
    # print(file)
    old_name = file
    # while file.find("-") > 0 or file.find("/") > 0:
    # file = file.replace("-","_")
    file = file.replace(":", "").replace('"',"")
    # print(old_name, file.replace(" ", "_"))
    os.rename(folder_dir+"/"+old_name, folder_dir+"/"+file.replace(" ", "_"))
