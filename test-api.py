
# -*- coding: utf-8 -*
#!/user/bin/python3

import threading
import sys, time
from numpy import *
import requests, json
import csv



if len(sys.argv) > 1 :
    counter = int(sys.argv[1])
else:
    counter = 5
img_num=1

def text2image():
    # url = "http://106.55.247.196:8501/api/predict/"
    url = "http://127.0.0.1:8501/api/predict/"
    # data = {
    #     "prompt": "A digital illustration of a steampunk library with clockwork machines, 4k, detailed, trending in artstation, fantasy vivid colors",
    #     "steps": 20,
    #     "num_images": 1
    # }
    data = '{"fn_index":0,"data":["A digital illustration of a medieval town, 4k, detailed, trending in artstation, fantasy",' + str(img_num) + ',20,512,512,7.5,0,true,"PNDM"],"session_hash":"p151xhy7s0s"}'
    headers = {"Content-Type": "application/json"}
    ret = requests.post(url=url, headers=headers, data=data)
    result = json.loads(ret.text)
    # print(f"duration: {result.get('duration')}")
    # print(f"image: {result.get('image_urls')}")
    return 'duration' in result



timing = []

class TestThread(threading.Thread):
    def __init__(self, threadId, name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name


    def run(self):
        print("开始线程: " + self.name)
        start_time = time.time()
        if text2image():
            end_time = time.time()
            duration = end_time - start_time
            timing.append(duration)
            print("[v]线程结束: " + self.name + ", 耗时: %.3f秒"%duration)
        else:
            print("[x]线程没有正确返回: " + self.name)
        # except Exception as err:
        #     print(f"[x]线程异常: {self.name}, {err}")

time_str = time.strftime("%Y%m%d%H%M%S", time.localtime())
f = open(f"test-result-{img_num}-{time_str}.csv", "w", encoding="UTF8")
writer = csv.writer(f)
header = ['QPS', '请求成功', '最短用时', '最长用时', '平均用时', '中位用时']
writer.writerow(header)


for counter in range(1, 5):
    print(f">>>>>>>>>>>>>开始测试[QPS={counter}]>>>>>>>>>>>>")
    workerThreads = []
    for i in range(counter):
        thread = TestThread(i, f"Thread-{i}")
        workerThreads.append(thread)

    for thread in workerThreads:
        thread.start()

    for thread in workerThreads:
        thread.join()

    print(f"<<<<<<<<<<<<测试结束[QPS={counter}]<<<<<<<<<<<<")
    print("*********测试结果**********")    
    print("线程数: %d"%len(workerThreads))
    print("成功返回: %d"%len(timing))
    print("最短耗时: %.3f秒"%min(timing))
    print("最长耗时: %.3f秒"%max(timing))
    print("平均耗时: %.3f秒"%mean(timing))
    print("中位数: %.3f秒"%median(timing))
    row = [counter, len(timing), min(timing), max(timing), mean(timing), median(timing)]
    writer.writerow(row)
    timing.clear()

f.close()

# print(">>>>>>>>>>>>>开始测试>>>>>>>>>>>>")
# workerThreads = []
# for i in range(counter):
#     thread = TestThread(i, f"Thread-{i}")
#     workerThreads.append(thread)

# for thread in workerThreads:
#     thread.start()

# for thread in workerThreads:
#     thread.join()

# print("<<<<<<<<<<<<测试结束<<<<<<<<<<<<")
# print("*********测试结果**********")
# print("线程数: %d"%len(workerThreads))
# print("成功返回: %d"%len(timing))
# print("最长耗时: %.3f秒"%max(timing))
# print("最短耗时: %.3f秒"%min(timing))
# print("平均耗时: %.3f秒"%mean(timing))
# print("中位数: %.3f秒"%median(timing))

