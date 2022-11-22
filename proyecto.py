import tkinter as tk
import requests
import json
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

API_KEY = '0v2IzxVpfiOGIzKUsnQnmt50RsrdMw4E4HqbkYrV'
root = tk.Tk()
root.title("NASA photo of the day")
root.geometry("900x800")
root['background'] = '#48047d'
URL = 'https://api.nasa.gov/planetary/apod'


def getData(params):
    response = requests.get(URL, params=params)
    json_data = json.loads(response.text)
    return json_data


def getAuthor(data):
    if 'copyright' in data:
        return f"Author: {data['copyright']}"
    else:
        return f"Author: unknown"


def getDescription(data):
    if 'explanation' in data:
        return f"Description: {data['explanation']}"
    else:
        return f"Description: unknown"


def getTitle(data):
    if 'title' in data:
        return f"Title: {data['title']}"
    else:
        return f"Title: unknown"


def isImage(data):
    if data['media_type'] == 'image':
        displayImage(getImage(data))
    else:
        return f"Invalid image format"


def getImage(data):
    img_url = data['url']
    return img_url


def displayImage(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()

    img = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo, width=600, height=400)
    label.image = photo
    label.pack()


def displayLabels(author, title, description):
    lblAuthor = tk.Label(text=author)
    lblAuthor.pack(pady=20)
    lblTitle = tk.Label(text=title)
    lblTitle.pack(pady=20)
    lblDescription = tkst.ScrolledText(master=root, wrap=tk.WORD, width=100, height=8)
    lblDescription.pack(pady=20)
    lblDescription.insert(tk.INSERT, description)


def main():
    date = input("Enter a valid date for the photo (YYYY-MM-DD): ")
    parameters = {
        'date': {date},
        'hd': 'True',
        'api_key': API_KEY
    }
    data = getData(parameters)
    displayLabels(getAuthor(data), getTitle(data), getDescription(data))
    isImage(data)
    print(getData(parameters))


if __name__ == "__main__":
    main()
    root.mainloop()