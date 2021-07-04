import os
import json

course = "Xóa mù Tiếng Anh cấp tốc"
input = open('./'+course+"/videos/links.txt", "r")
links = input.readlines()
output = "./"+course+"/videos/"
# files = os.listdir('./'+course+'/videos')

# print(files)
for link in links:
    # print(files[i])
    item = json.loads(link.replace("\n", ""))
    filename = item["name"].replace(":","").replace("\\","")
    url = item["url"]
    command = "ffmpeg -i '"+url+"' -q:v 1 '"+filename.replace(" ", "_")+".mp4'"
    print(command)
    # print(os.path.abspath(output+filename))
    os.system(command)


# item = links[0].replace("\n", "")
# print(json.loads(item)["name"])
# os.system("ffmpeg -i "+links[0].replace("\n","")+" "+"out.mp4")


input.close()