
import random
import openai
from PIL import Image, ImageDraw, ImageFont
import os
import schedule
import time
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag




def create_text():
    openai.api_key = ""

    duygular = [
        "öfke",
        "kaygı",
        "mutluluk",
        "Acıma",
        "Aşağılama",
        "Beklenti",
        "Çekingenlik",
        "Gurur",
        "Hayal kırıklığı",
        "Heves",
        "İlgisizlik",
        "Kafa karışıklığı",
        "Sabır",
        "Sıkıntı",
        "Umut",
        "Yalnızlık"
    ]

    duygu = random.choice(duygular)
    prompt = f"{duygu} duygusu ile ilgili anlamlı bir söz yazar mısın?"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    max_tokens=200
    )
    
    texts = response["choices"][0]["text"].split(" ")

    indent = len(texts)//2
    if indent != 1:
        for b in range(indent):
            if b ==indent-1 and indent >0:
                continue
            texts.insert(3+b*4, "\n")

    text = " ".join(texts)
    if "-" in text:
        x = text.split("-")
        text= x[0] + "\n" + "-" + x[1]
    
    print(text)
    return [text, duygu]

def create_post(text):
    path = os.path.dirname(__file__)
    img = Image.open(r"")  #background image
    width,height = img.size
    print(int(width/15))
    font = ImageFont.truetype("Arial.ttf", int(width/15))
    d1 = ImageDraw.Draw(img, mode='RGBA')
    w, h = d1.textsize(text[0], font)


    
    y_start = (height - h) / 2

    texts = text[0].split('\n')

    for x in texts:
        d1.text((width/2, y_start+int(width/15)), x, fill = (0, 0, 0), font = font, anchor = 'ms')
        y_start += int(width/15)*1.1
    
    save_path = (f"post/{random.randrange(1000000,99999999)}_{text[1]}.jpg")
    img = img.convert('RGB')
    img.save(save_path)
    return (save_path, text[1])




def main():
    path, feeling = create_post(create_text())
    cl.photo_upload(path, f"#{feeling}")





if __name__ == "__main__":
    cl = Client()
    cl.login("", "")
    schedule.every().day.at("13:00").do(main)
    schedule.every().day.at("14:00").do(main)
    schedule.every().day.at("15:00").do(main)
    schedule.every().day.at("18:00").do(main)
    schedule.every().day.at("21:00").do(main)
    schedule.every().day.at("00:00").do(main)

    while True:
        schedule.run_pending()
        time.sleep(15)








