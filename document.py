import requests
from pathlib import Path
import os
import json



def GetAllDocsInCourseById(id):
    headers = {
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8"
    }
    api = "https://ngoaingu24h.vn/get-documents-by-course-id"
    data = {
        "courseId": id,
        "offset": 0,
        "limit": 9999
    }
    response = requests.post(api, headers=headers, data=data).json()
    # print(response[4]["data"])
    # j = json.loads(response[4]["data"])
    # print(j)

    r_name = requests.post("https://ngoaingu24h.vn/get-path-by-id", headers=headers, data={"courseId": id, "pathIds[]":-1, "topicId": 1}).json()
    # print(r_name[0])
    name_course = r_name[0]["name"]
    try:
        os.mkdir(name_course)
        os.mkdir(name_course+"/documents")
    except:
        pass
    
    print(name_course)
    print("Tổng file : ", len(response))
    print("Đang tải...")

    

    docs = response
    for doc in docs:
        try:
            j = json.loads(doc["data"])
            name = j[0]["fileName"]
        except:
            name = doc["title"]
        try:
            url = doc["url"]
            name = name.replace("(","[").replace(")","]").replace("/","").replace(":","").replace('"',"")
            print(name)
            print(url)
            doc_res = requests.get(url)
            filename = Path("./"+name_course+"/documents/"+name)
            filename.write_bytes(doc_res.content)
        except:
            pass


    print("Đã xong.")



GetAllDocsInCourseById("5163948594692096")
