# BitkubAndBinance
ลุงทดสอบแล้วเรื่อง Bitkub API สามารถส่งคำสั่งไปซื้อและขายได้

ใครอยากดูคลิปที่ลุงสอนวันก่อน ลุงอธิบายไว้ 4 ชั่วโมงได้ในนี้: https://youtu.be/dyqBpTtzk1o

Source Code: https://github.com/UncleEngineer/BitkubAndBinance
คู่มือการใช้ API: https://github.com/bitkub/bitkub-official-api-docs/blob/master/restful-api.md#post-apimarketplace-ask

ถ้าจะเขียนให้สั่งซื้อ สั่งขาย ให้ดูโค้ดจากไฟล์...

1- ส่งคำสั่งซื้อ: bitkubbuy.py 
2- ส่งคำสั่งขาย: bitkubsell.py

โดย API KEY , API SECRET นำมาจากลิ้งค์นี้ https://www.bitkub.com/publicapi
"จะซื้อขายได้ต้องเปิดสิทธิ์การเข้าถึงเป็น WRITE" นำไปใส่ในตัวแปร

apikey = 'afadaasafsdfasdfafadaasafsdfasdf' 
apisecret = b'afadaasafsdfasdfafadaasafsdfasdf'

(ห้ามลบตัว b ออกหน้ารหัส ของ apisecret)

ปล. บอกไว้ก่อน ลุงไม่สอนเทรดนะจ๊ะ ใครเทรดตามลุงส่วนใหญ่เจ๊งทุกราย 555 ลุงสอนแค่เทคนิคการเขียนโปรแกรมเท่านั้น ....ถ้านำโค้ดไปใช้เกิดเจ๊งขึ้นมา อย่าโทษลุงนะจ๊ะ  แต่ถ้านำโค้ดไปใช้แล้วได้กำไร แบ่งให้ลุงสัก 1 BTC ก็พอแล้ว ลุงไม่เอาเยอะ 555

ปล2. พวก Crypto ถ้าคุณไม่เข้าใจมันจริงๆ คุณเหมือนกับ "นักเล่นน้ำเต้าปูปลา" คนที่เข้าใจเท่านั้นถึงจะเรียกว่า "นักลงทุน" ....วิทยายุทธด้านนี้ ไม่ได้อ่านหนังสือเล่มละ 150 บาทแล้วเดียวแล้วรวยเลยเหมือนคำพูดหน้าปกนะจ๊ะ นะจ๊ะ ตะเตือนไต....๕๕๕๕

Follow: https://facebook.com/UncleEngineer/
