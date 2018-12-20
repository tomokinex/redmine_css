import base64
import sys
from PIL import Image
from io import BytesIO

print('user id:')
user_num = input()

print('path to image:')
image_file = input()

image = Image.open(image_file)
w, h = image.size
icon_size = 100

if w > h:
    new_w = icon_size
    new_h = h * icon_size / w
else:
    new_h = icon_size
    new_w = w * icon_size / h

image_resized = image.resize(map(int, (new_w, new_h)))

buffered = BytesIO()
image_resized.save(buffered, format='JPEG')
b64 = base64.b64encode(buffered.getvalue()).decode()

user_num = 103

write_lines = [f'a.user[href="/users/{user_num}"] {{',
               f'  background-image: url(data:image/jpeg;base64,{b64});',
               '  display: inlune-block;',
               '  height: 78px;',
               '  background-position: 0px 18px;',
               '  background-repeat: no-repeat;',
               '  background-size: 50px;',
               '}\n']

with open(f'twitter_style.css', 'a') as f:
    f.write('\n'.join(write_lines))
