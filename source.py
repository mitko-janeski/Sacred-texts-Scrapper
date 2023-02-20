# pip install beautifulsoup4
# pip install pillow

import requests
from bs4 import BeautifulSoup
from PIL import Image
import requests
from io import BytesIO
import os.path
from PIL import Image
import requests
from io import BytesIO
import os.path

def fetch_image(url,file_name):
    print(url)
    response = requests.get(url)     
    img = Image.open(BytesIO(response.content))
#   width, height = img.size
#   print(f"Image height is {height} and width is {width}")
    #****************************************************CHANGE THIS TO YOUR PATH***********************************************
    save_path = 'C:\\Users\\PC1\\Desktop\\ANCIENTTEXTS\\images\\'
    img.save(save_path+file_name)

def fetch_all_images(img_tags):
    image_base_url="https://sacred-texts.com/mas/morgan/img/"
#     img_tags=soup.find_all('img')
    filter=['cdinfo.jpg']
    for tag in img_tags:
        image_name=tag.get('src').split("/")[-1]
        if image_name not in filter:
            image_url=image_base_url+image_name
            fetch_image(image_url,image_name)

base_url='https://sacred-texts.com/mas/morgan/morg'
for index in range(0,19):
    f = open("source.txt", "a")
    if index<10:
        index="0"+str(index)
    url=f"{base_url}{index}.htm"
    print(url)
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    # print(soup.prettify)
    paras = soup.find_all('p')
    for element in paras:
        print(element)
        if "morg" not  in str(element):
            f.write(str(element))
            f.write("\n")
    f.write("\n")
    f.close()
    img_tags=soup.find_all('img')
    fetch_all_images(img_tags)