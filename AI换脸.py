import json
import base64
import requests
import simplejson
from os import system

system("title "+"AI换脸")
a = input("请输入被换脸路径:")
b = input("请输入换脸的路径:")
c = input("请输入图片保存路径:")

def find_face(imagepath):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    data = {"api_key":'iv87VShzmGhNTggGwOD-BdRbfQO0oE6f',
            "api_secret":'Q_mX_RST4N6X21NsSz1x1h_5Eiu_TXzf',"image_url":imagepath,"return_landmark":1}
    files = {"image_file":open(imagepath,'rb')}
    response = requests.post(http_url,data=data,files=files)
    req_con = response.text
    this_dict = json.loads(req_con)
    faces = this_dict['faces']
    list0 = faces[0]
    rectangle = list0['face_rectangle']
    print(rectangle)
    return rectangle
def merge_face(image_url1,image_url2,image_url,number):
    ff1 = find_face(image_url1)
    ff2 = find_face(image_url2)
    rectangle1 = str(str(ff1['top'])+","+str(ff1['left'])+","+str(ff1['width'])+","+str(ff1['height']))
    rectangle2 = str(str(ff2['top'])+","+str(ff2['left'])+","+str(ff2['width'])+","+str(ff2['height']))
    print(rectangle1)
    print(rectangle2)
    f1 = open(image_url1,'rb')
    f1_64 = base64.b64encode(f1.read())
    f1.close()
    f2 = open(image_url2,'rb')
    f2_64 = base64.b64encode(f2.read())
    f2.close()
    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
    data ={"api_key":'iv87VShzmGhNTggGwOD-BdRbfQO0oE6f',
           "api_secret":'Q_mX_RST4N6X21NsSz1x1h_5Eiu_TXzf',
           "template_base64":f1_64,"template_rectangele":rectangle1,
           "merge_base64":f2_64,"merge_rectangle":rectangle2,"merge_rate":number}
    resp = requests.post(url_add,data=data)
    print(resp.text)
    req_con = resp.text
    req_dict = json.JSONDecoder().decode(req_con)
    result = req_dict['result']
    imgdata = base64.b64decode(result)
    file =  open(image_url,'wb')
    file.write(imgdata)
    file.close()
if __name__ == '__main__':
    image1 = r'%s' %a
    image2 = r'%s' %b
    image3 = r'%s' %c
    merge_face(image1,image2,image3,100)
