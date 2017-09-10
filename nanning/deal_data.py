import matplotlib.pyplot as plt
import json
f = open('./data.json')
data = f.read()
datas = json.loads(data)
datas.reverse()
length = len(datas)
arg1, arg2 = datas[0]['create_time'], datas[length-1]['create_time']

ax1 = plt.subplot(311)
plt.xlabel('ultrasonic1:   [{}] - [{}]'.format(arg1, arg2))
plt.ylabel('cm')
plt.plot([i for i in range(len(datas))], [d['ultrasonic1'] for d in datas])
ax2 = plt.subplot(312)
plt.xlabel('ultrasonic2:   [{}] - [{}]'.format(arg1, arg2))
plt.ylabel('cm')
plt.plot([i for i in range(len(datas))], [d['ultrasonic2'] for d in datas])
ax3 = plt.subplot(313)
plt.xlabel('average:       [{}] - [{}]'.format(arg1, arg2))
plt.ylabel('cm')
plt.plot([i for i in range(len(datas))], [d['waste_height'] for d in datas])

plt.show()
