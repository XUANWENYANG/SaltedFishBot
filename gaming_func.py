# -*- coding: utf-8 -*-
# Author:       Amove
# vision 1.1 zero 修改支持高分辨

import time
import datetime
from window_operate import *
import threading
import os
pic_dic={}
pic_path="./pic"
pic_dir=os.listdir(pic_path)
print(pic_dir)
for i in pic_dir:
    img1=cv2.imread(pic_path+"/"+i)
    pic_dic[i.split(".")[0]]=img1
print(pic_dic)
    
lian_ji_flag=0    

# 创建互斥锁
mutex = threading.Lock()

def lianji_rountin_long(hwnd):
    print("连击线程已上线...",datetime.datetime.now())
    rect = win32gui.GetWindowRect(hwnd)
    x,y=rect[0],rect[1]
    w,h=rect[2] - x,rect[3] - y
    while True:
        print("连击线程心跳...",datetime.datetime.now())
        # time.sleep(60*60*8) # 两小时
        with mutex:  # 获取互斥锁
            lian_ji(hwnd,h,w)


def fuben_tower_rountin(hwnd):
    print("咸将塔线程已上线...",datetime.datetime.now())
    while True:
        print("咸将塔线程心跳...",datetime.datetime.now())
        time.sleep(60*60*3) # 三小时
        with mutex:  # 获取互斥锁
            fuben_tower(hwnd,h,w)
            
def shoucai_rountin_long(hwnd):
    print("收菜线程已上线...",datetime.datetime.now())
    while True:
        print("收菜线程心跳...",datetime.datetime.now())
        time.sleep(60*60*8) # 两小时
        with mutex:  # 获取互斥锁
            shoucai(hwnd,h,w)
            
#为了黑市活动设置短时间的
def shoucai_rountin_short(hwnd):
    print("收菜线程已上线...",datetime.datetime.now())
    while True:
        print("收菜线程心跳...",datetime.datetime.now())
        time.sleep(60*60*2) # 两小时
        with mutex:  # 获取互斥锁
            shoucai(hwnd,h,w)
            
                        
def shoucai(hwnd,h,w):
    time.sleep(1.5)
    # perform_background_move(hwnd,0.35*w,0.86*h,3)  #划开锁屏（无法保证在首页）
    time.sleep(2)
    # 43/450 345/844
    perform_background_click(hwnd,0.0856*w,0.408*h,) # 收益按钮
    time.sleep(0.7)
    # 303/450 676/844
    perform_background_click(hwnd,0.67*w,0.8*h,5) # 升级按钮
    time.sleep(0.7)
    # 154/450 669/844
    perform_background_click(hwnd,0.34*w,0.792*h) # 领奖励按钮
    time.sleep(1.5)


            
def fuben_tower(hwnd,h,w):
    time.sleep(1.5)
    # perform_background_move(hwnd,0.35*w,0.86*w,3)  #划开锁屏（无法保证在首页）
    time.sleep(0.7)
    #413/450 795/844
    perform_background_click(hwnd,0.917*w,0.942*h) # 副本按钮
    time.sleep(2)
    #225/450 233/844
    perform_background_click(hwnd,0.3*w,0.276*h) # tower 按钮
    time.sleep(2)
    
    for i in range(0,10):
        #238/450 788/844
        perform_background_click(hwnd,0.529*w,0.934*h) # 挑战按钮
        time.sleep(1)
         #51/450 717/844
        perform_background_click(hwnd,0.11*w,0.849*h,3) # 跳过按钮
        time.sleep(4)

    time.sleep(1.5)
     #39/450 807/844
    perform_background_click(hwnd,0.0867*w,0.956*h,2) # 退出按钮
    time.sleep(1)
     #230/450 792/844
    perform_background_click(hwnd,0.511*w,0.938*h,2) # 返回案板首页
    time.sleep(5)


def lian_ji(hwnd,h,w):
    # show_window(hwnd)
    lian_ji_flag=1
    while(lian_ji_flag):
        # time.sleep(1)
        perform_background_click1(hwnd,0.47*w,0.52*h,1) # 副本按钮


def lian_ji_cancel(hwnd,h,w):
    show_window(hwnd)
    lian_ji_flag=0
 

def daily_test(hwnd,h,w):
    show_window(hwnd)
    time.sleep(1.5)
    # perform_background_move(hwnd,0.35*w,0.86*w,3)  #划开锁屏（无法保证在首页）
    # time.sleep(1.5)
    #413/450 795/844
    perform_background_click(hwnd,0.917*w,0.942*h) # 副本按钮
    time.sleep(1)
    #225/450 233/844
    perform_background_click(hwnd,0.3*w,0.476*h) # 咸王考验按钮
    time.sleep(1)

    perform_background_click(hwnd,0.511*w,0.908*h,1) # 点击挑战按钮
    time.sleep(1)
    perform_background_click(hwnd,0.11*w,0.849*h,2) # 跳过按钮
    time.sleep(1)
    perform_background_click(hwnd,0.511*w,0.758*h,) # 点击确认
    time.sleep(1)
    perform_background_click(hwnd,0.0867*w,0.956*h,2) # 退出按钮
    time.sleep(1)
     #230/450 792/844
    perform_background_click(hwnd,0.511*w,0.938*h,2) # 返回案板首页
    time.sleep(5)
    
def judge_jar(hwnd,x,y,w,h):
    show_window(hwnd)
    perform_background_click(hwnd,0.917*w,0.802*h) # 客厅按钮
    time.sleep(1)
    #905 1674
    position1,_=shot1(x+0.05*w,y+0.555*h,0.071*w,0.0448*h,"jar1")
    position2,_=shot1(x+0.05*w,y+0.615*h,0.071*w,0.0448*h,"jar2")
    position3,_=shot1(x+0.05*w,y+0.67*h,0.071*w,0.0448*h,"jar3")
    is_find_gold=0
    is_find_silver=0
    is_find_cooper=0
    if(position1-pic_dic["position1_none"]==0):
        is_find_gold=1
        is_find_silver=1
        is_find_cooper=1
    elif(position1-pic_dic["position1_gold_noopen"]==0):
        if(position2-pic_dic["position2_none"]==0):
            is_find_silver=1
            is_find_cooper=1
        elif(position1-pic_dic["position2_sliver_noopen"]==0): 
            if(position2-pic_dic["position3_none"]==0 ):
                 is_find_cooper=1
            elif(position2-pic_dic["position3_copper_open"]==0):
                #点掉copperjar找
                is_find_cooper=1
        elif(position1-pic_dic["position2_sliver_open"]==0):
            #点掉sliverjar找
            is_find_silver=1
            if(position2-pic_dic["position3_none"]==0 ):
                 is_find_cooper=1
            elif(position2-pic_dic["position3_copper_open"]==0):
                #点掉copperjar找
                is_find_cooper=1
    elif(position1-pic_dic["position1_gold_open"]==0):
        #点掉goldjar找
        is_find_gold=1
        if(position2-pic_dic["position2_none"]==0):
            is_find_silver=1
            is_find_cooper=1
        elif(position1-pic_dic["position2_sliver_noopen"]==0): 
            if(position2-pic_dic["position3_none"]==0 ):
                 is_find_cooper=1
            elif(position2-pic_dic["position3_copper_open"]==0):
                #点掉copperjar找
                is_find_cooper=1
        elif(position1-pic_dic["position2_sliver_open"]==0):
            #点掉sliverjar找
            is_find_silver=1
            if(position2-pic_dic["position3_none"]==0 ):
                 is_find_cooper=1
            elif(position2-pic_dic["position3_copper_open"]==0):
                #点掉copperjar找
                is_find_cooper=1
    
    # perform_background_click(hwnd,0.917*w,0.902*h) # 副本按钮
    for num in range(10):
        if(is_find_cooper==0 and is_find_gold==0 and is_find_silver==0):
            break
        jar_list=[]
        for i in range(8):
            jar,_=shot1(x+0.05*w,y+0.555*h,0.071*w,0.0448*h,"isjar"+i)
            # if(is_find_gold==1){
                
            # }
            # if(is_find_silver==1){
                
            # }
            # if(is_find_cooper==1){
                
            # }
           
       