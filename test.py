import requests

BASE = "http://127.0.0.1:5000/"


data = [{"tag_number": 101, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 102, "overall_bsv": 2,"feed": "normal" },
        {"tag_number": 103, "overall_bsv": 5,"feed": "normal" },
      {"tag_number": 104, "overall_bsv": 1,"feed": "normal" },
        {"tag_number": 10, "overall_bsv": 2,"feed": "normal" },
        {"tag_number": 1033, "overall_bsv": 3,"feed": "normal" },
        {"tag_number": 101, "overall_bsv": 2,"feed": "normal" },
        {"tag_number": 1022, "overall_bsv": 4,"feed": "normal" },
        {"tag_number": 1011, "overall_bsv": 1,"feed": "normal" },
        {"tag_number": 1056, "overall_bsv": 1,"feed": "normal" }]


for i in range(len(data)):
    response = requests.put(BASE + "BSV_value/" + str(i), data[i])
    print(response.json())


#get request and get response and print it
# response = requests.delete(BASE + "video/1")
# print(response)

input()

#get request and get response and print it
response = requests.get(BASE + "BSV_value/3")
print(response.json())
input()
#get request and get response and print it
response = requests.patch(BASE + "BSV_value/1",{"tag_number": 101, "overall_bsv": 2,"feed": "normal"})
print(response.json())