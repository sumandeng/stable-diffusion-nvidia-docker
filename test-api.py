
# -*- coding: utf-8 -*
#!/user/bin/python3

import threading
import sys, time
from numpy import *
import requests, json



if len(sys.argv) > 1 :
    counter = int(sys.argv[1])
else:
    counter = 5

# accessToken = getAccessToken(accessKey, secretKey)


def text2image():
    url = "http://127.0.0.1:8501/api/predict/"
    # data = {
    #     "prompt": "A digital illustration of a steampunk library with clockwork machines, 4k, detailed, trending in artstation, fantasy vivid colors",
    #     "steps": 20,
    #     "num_images": 1
    # }
    data = '{"fn_index":0,"data":["A digital illustration of a medieval town, 4k, detailed, trending in artstation, fantasy",1,20,512,512,7.5,0,true,"PNDM"],"session_hash":"p151xhy7s0s"}'
    headers = {"Content-Type": "application/json"}
    ret = requests.post(url=url, headers=headers, data=data)
    result = json.loads(ret.text)
    # print(f"task id: {result.get('task_id')}")
    # print(f"image: {result.get('image_urls')}")



timing = []

class TestThread(threading.Thread):
    def __init__(self, threadId, name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name


    def run(self):
        print("开始线程: " + self.name)
        start_time = time.time()
        text2image()
        end_time = time.time()
        duration = end_time - start_time
        timing.append(duration)
        print("[v]线程结束: " + self.name + ", 耗时: %.3f秒"%duration)
        # except Exception as err:
        #     print(f"[x]线程异常: {self.name}, {err}")

print(">>>>>>>>>>>>>开始测试>>>>>>>>>>>>")
workerThreads = []
for i in range(counter):
    thread = TestThread(i, f"Thread-{i}")
    workerThreads.append(thread)

for thread in workerThreads:
    thread.start()

for thread in workerThreads:
    thread.join()

print("<<<<<<<<<<<<测试结束<<<<<<<<<<<<")
print("*********测试结果**********")
print("线程数: %d"%len(workerThreads))
print("成功返回: %d"%len(timing))
print("最长耗时: %.3f秒"%max(timing))
print("最短耗时: %.3f秒"%min(timing))
print("平均耗时: %.3f秒"%mean(timing))
print("中位数: %.3f秒"%median(timing))

