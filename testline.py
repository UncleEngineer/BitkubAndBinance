#testline.py

from songline import Sendline
# pip install songline
token = 'bgClpKkgX4c4o0k0pAMLmd7pfSgSotcGpHAF0tT8N43'
messenger = Sendline(token)

messenger.sendtext('สวัสดีจ้าาาา')

messenger.sticker(3,1,'บิทคอยราคาต่ำแล้ว! 5000 บาทต่อเหรียญ')

messenger.sendimage('https://www.altcoinbuzz.io/wp-content/uploads/2018/10/Ontwerp-zonder-titel-4.png')
