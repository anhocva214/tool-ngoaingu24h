import requests
from pathlib import Path
import os
import json



def GetAllVideoInCourseById(id):
    headers = {
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8"
    }
    api = "https://ngoaingu24h.vn/get-childs-topics"
    data = {
        "courseId": id,
        "offset": 0,
        "userId": "tackecon"
    }
    response = requests.post(api, headers=headers, data=data).json()
    # des = response[0]["description"]
    # start = des.find("https://ngonngu.vncdn.vn")
    # end = des.find("m3u8")
    # print(des[start:end+4])


    r_name = requests.post("https://ngoaingu24h.vn/get-path-by-id", headers=headers, data={"courseId": id, "pathIds[]":-1, "topicId": 1}).json()
    name_course = r_name[0]["name"]
    try:
        os.mkdir(name_course)
        os.makedirs(name_course+"/videos")
    except:
        pass
    
    print(name_course)
    print("Tổng video : ", len(response))
    print("Đang tải...")

    

    videos = response
    link_file = open("./"+name_course+"/videos/links.txt", "w")
    i = 0
    for video in videos:
        i += 1
        name = video["name"]
        start = video["description"].find("https://ngonngu.vncdn.vn")
        end = video["description"].find("m3u8")
        url = video["description"][start:end+4]
        print(name)
        print(url)
        
        try:
            # doc_res = requests.get(url)
            # filename = Path("./"+name_course+"/videos/"+str(i)+" - "+name+".m3u8")
            # filename.write_bytes(doc_res.content)
        
            if len(url.strip()) > 0:
                item = {
                    "name": name,
                    "url": url
                }
                item = json.dumps(item)
                link_file.write(str(item)+"\n")
        except:
            pass

    link_file.close()



    print("Đã xong.")



GetAllVideoInCourseById("5958158015004672")
