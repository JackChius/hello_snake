#! python3

import webbrowser
import sys
import pyperclip

def printMe(str):#{ 
     print(str)
     return  
        #}
printMe('HAHA')

adre = ''
while adre != 'q':
    print('输入一个你想去的城市Please write your address!!')
    adre = input()
    # if len(sys.argv)>1:
    if adre == 'q':
        sys.exit()
    elif len(adre) > 1:
            # get address from command line
            # address = ''.join(sys.argv[1:])
            address = ''.join(adre)
    else:
            address = pyperclip.paste()

    webbrowser.open('https://ditu.amap.com/search?query=' + address +
                        '&city=440703&geoobj=112.74162%7C22.692559%7C114.478834%7C23.556407&zoom=10')

#  百度 http://map.baidu.com/?newmap=1&ie=utf-8&s=s%26wd%3D江门
#  待做功能 两地路线 驾车/公交
