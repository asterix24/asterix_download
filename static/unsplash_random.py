#!/bin/env python

import requests
import sys
import os
import re

ACCESS_KEY="MkxrS9IWmaiKI_Waqt0efE_0npaNszZo9A0uyeSWX48"
QUERY="flower,astronomy,space,technology,abstract,abstract+art"
URL="https://api.unsplash.com/photos/random/?client_id={access_key}&query={quey}t&orientation=landscape&fit=clip"


resp = requests.get(URL.format(access_key=ACCESS_KEY, quey=QUERY))

if resp.status_code != 200:
    print("unable to get info {}".format(resp.status_code))
    sys.exit(1)

data = resp.json()

urls = data.get("urls", None)
if urls is None:
    print("No urls found in reply")
    sys.exit(1)
print(urls)

img_url = urls.get('regular', None)
if img_url is None:
    print('No regular url found in reply {}'.format(img_url.status_code))
    sys.exit(1)

print(img_url)
img_reply = requests.get(img_url)

if img_reply.status_code != 200:
    print("Unable to get imgage {}".format(img_reply.status_code))
    sys.exit(1)

with open("/var/www/html/blog.asterix.cloud/images/unsplash.jpeg", 'wb') as o:
    o.write(img_reply.content)

print(dir(img_reply))

desc = data.get("description", "")
print(desc)

links = data.get("links", None)
if links is None:
    print("No links found in reply")
    sys.exit(1)

html = links.get("html", "")
print(html)

logo_found = False
IMG_TAG="<img id=\"rdmimg\" class=\"logo-image\" src=\"images/unsplash.jpeg\" title=\"{title}\" width=\"200px\" alt=\"{alt}\"/>"


INDX_FILE="/var/www/html/blog.asterix.cloud/index.html"
f = None
with open(INDX_FILE, 'r') as o:
    f = re.sub(r"<img.*id=\"rdmimg\".*\/>", IMG_TAG.format(title=desc, alt=html),
            o.read(), flags=re.DOTALL)
    print(f)

if f is not None:
    with open(INDX_FILE, 'w') as o:
        o.write(f)

