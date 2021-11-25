import os

from PIL import Image
from sqlalchemy import false
path = 'D:\\py\\flaskProject\\static\\images\\story'
for a,b,rs in os.walk('D:\\py\\flaskProject\\static\\images\\story'):
     print(rs)
img_list = []
for i in rs:
    img_list.append(path+'\\'+i)
print(img_list)
k = 0
for i in img_list:
    img = Image.open(i)
    img = img.resize((1920, 1080), Image.ANTIALIAS)
    img.save(rs[k])
    k = k+1

# img = Image.open('G:\\py_project\\flaskProject\\static\\images\\avatar\\%d.png')
# for i in range(9,22):
#     print(s.format(i))
#     path = s.format(i)
#     img = Image.open(path)
#     width = img.size[0]   # 获取宽度
#     height = img.size[1]   # 获取高度
#     img = img.resize((int(width*0.25), int(height*0.25)), Image.ANTIALIAS)
#     img.save(str(i)+'.png')



# for a,b,rs in os.walk('D:\\py\\flaskProject\\img_deal'):
#     print(rs)
#
# for i in rs:
#     if i.endswith('py', 0, len(i))==False:
#         img = Image.open(i)
#         width = img.size[0]  # 获取宽度
#         height = img.size[1]  # 获取高度
#         img = img.resize((int(width*0.9), int(height * 0.75)), Image.ANTIALIAS)
#         s = i.split('\\')[-1]
#         s_s = s.split('.')[0] + 'small.' + s.split('.')[-1]
#         img.save(s_s)
#
#         s_b =s.split('.')[0]+'big.'+s.split('.')[-1]
#         # img = img.resize((int(width * 4), int(height *4)), Image.ANTIALIAS)
#         # img.save(s_b)
#         print(s_b,s_s)
#         # img.save('genshin.png')