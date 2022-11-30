import json
from PIL import Image
import requests
import os
import shutil
from urllib.parse import urlparse
with open('./environmentspruned.json', 'r') as f:
    jsonthing = json.loads(f.read())

# Last Take on 29/11

checked = 0
total = len(jsonthing['messages'])

for x in jsonthing['messages']:
    checked += 1
    a = urlparse(x['url'])
    resp = requests.get(x['url'], headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}, stream=True)
    if resp.status_code:
        with open('./environmentsunprocessedimages/' + str(os.path.basename(a.path)), 'wb') as f:
            f.write(resp.content)
        imgfull = Image.open('./environmentsunprocessedimages/' + str(os.path.basename(a.path)))
        imgtopleft = imgfull.crop((0, 0, 512, 512))
        imgtopright = imgfull.crop((512, 0, 1024, 512))
        imgbottomleft = imgfull.crop((0, 512, 512, 1024))
        imgbottomright = imgfull.crop((512, 512, 1024, 1024))
    imgtopleft.save("./environmentsimages/" + str(os.path.basename(a.path))[:-4] + "_topleft.png")
    imgtopright.save("./environmentsimages/" + str(os.path.basename(a.path))[:-4] + "_topright.png")
    imgbottomleft.save("./environmentsimages/" + str(os.path.basename(a.path))[:-4] + "_bottomleft.png")
    imgbottomright.save("./environmentsimages/" + str(os.path.basename(a.path))[:-4] + "_bottomright.png")
    print(str(checked) + "/" + str(total))