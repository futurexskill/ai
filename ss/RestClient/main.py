import requests
import json
url="http://127.0.0.1:8005/courses"
post_url="http://127.0.0.1:8005/course"
#response = requests.get(url)
course_json=json.dumps({ "course_name": "New course 20", "author_name": "futurex", "course_section": { "section1":"Value", "section2":"Value3" }, "creation_date": "2021-03-20" })
response = requests.post(post_url,course_json)
print(response)
print(response.text)



