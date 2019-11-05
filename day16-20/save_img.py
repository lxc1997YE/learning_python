from bs4 import BeautifulSoup
import requests
import os
import time
from tomorrow import threads

cur_path = os.path.dirname(os.path.realpath(__file__))

def get_img_urls():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
    fengjing = r.content
    soup = BeautifulSoup(fengjing, "html.parser")
    imags = soup.find_all(class_="lazy")
    return imags

@threads(5)
def save_img(imgUrl):
    try:
        jpg_rl = imgUrl["data-original"]
        title = imgUrl["title"]
        print(title)
        print(jpg_rl)
        print("")
        save_file = os.path.join(cur_path, "jpg")
        if not os.path.exists(save_file): os.makedirs(save_file)

        with open(os.path.join(save_file, title + '.jpg'), "wb") as f:
            f.write(requests.get(jpg_rl).content)
    except:
        pass

if __name__ == '__main__':
    t1 = time.time()
    image_urls = get_img_urls()
    for i in image_urls:
        save_img(i)

    t2 = time.time()
    print("总耗时：%.2f 秒" % (t2 - t1))
