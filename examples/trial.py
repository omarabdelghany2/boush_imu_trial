import os.path


import json

with open("/home/omar/Adafruit_Python_BNO055/aloooooo", 'w') as cal_file:
    json.dump([1,2,3], cal_file)


print(os.path.exists("/home/omar/Adafruit_Python_BNO055/aloooo"))