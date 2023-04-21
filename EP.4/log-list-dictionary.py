Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py
Traceback (most recent call last):
  File "C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py", line 12, in <module>
    addata('น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาท')
TypeError: addata() takes 0 positional arguments but 1 was given

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py
Traceback (most recent call last):
  File "C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py", line 12, in <module>
    adddata('น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาท')
TypeError: adddata() takes 0 positional arguments but 1 was given

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py
Traceback (most recent call last):
  File "C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py", line 12, in <module>
    adddata('น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาท')
TypeError: adddata() takes 0 positional arguments but 1 was given

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py
Traceback (most recent call last):
  File "C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py", line 23, in <module>
    readdata()
  File "C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py", line 15, in readdata
    with open('add-data.txt',endoding='utf-8') as file:
TypeError: 'endoding' is an invalid keyword argument for open()

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py
['น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาทลูกอม 5 บาทดินสอ 10 บาทปากกา 10 บาท\n', 'ยางลบ 10 บาท\n']

= RESTART: C:/Users/1000285397/Desktop/Python 101/EP.4/writefile.py
น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาทลูกอม 5 บาทดินสอ 10 บาทปากกา 10 บาท
ยางลบ 10 บาท

box = []
box.append('ปากกา')
box.append('ปากกา')
box.append('ปากกา')
box.append('ดินสอ')
box.append('ยางลบ')
print(box)
['ปากกา', 'ปากกา', 'ปากกา', 'ดินสอ', 'ยางลบ']
print(box[3])
ดินสอ
print(box[4])
ยางลบ
print(box[-2])
ดินสอ
brand = {'pen':['Lamy','Pentel','Fiber-castel'],'pencil':['hourse','staedtler'],'eraser':'ยางลบ2สี'}
print(brand['pen'])
['Lamy', 'Pentel', 'Fiber-castel']
print(brand['pen'][1])
Pentel
print(brand['pencil'][0])
hourse
print(brand['eraser'][0])
ย
print(brand['eraser'])
ยางลบ2สี
print(box)
['ปากกา', 'ปากกา', 'ปากกา', 'ดินสอ', 'ยางลบ']
print(len(box))
5
print(brand.keys())
dict_keys(['pen', 'pencil', 'eraser'])
print(brand.values())
dict_values([['Lamy', 'Pentel', 'Fiber-castel'], ['hourse', 'staedtler'], 'ยางลบ2สี'])
for b in box:
    print(b)

    
ปากกา
ปากกา
ปากกา
ดินสอ
ยางลบ
for br in brand.keys():
    print(br)

    
pen
pencil
eraser
for br in brand.values():
...     print(br)
... 
...     
['Lamy', 'Pentel', 'Fiber-castel']
['hourse', 'staedtler']
ยางลบ2สี
>>> for br in brand:
...     print(br)
... 
...     
pen
pencil
eraser
>>> for br in brand.items():
...     print(br)
... 
...     
('pen', ['Lamy', 'Pentel', 'Fiber-castel'])
('pencil', ['hourse', 'staedtler'])
('eraser', 'ยางลบ2สี')
>>> 
>>> len(bran)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    len(bran)
NameError: name 'bran' is not defined. Did you mean: 'brand'?
>>> len(brand)
3
