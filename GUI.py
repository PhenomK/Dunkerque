#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
import redis

windows = tk.Tk()
windows.title('神龙/神灯测试小工具')
windows.geometry('500x350')

tk.Label(windows,text='Dragon1:').place(x=30,y=30)
tk.Label(windows,text='Dragon2:').place(x=30,y=60)
tk.Label(windows,text='Dragon3:').place(x=30,y=90)
tk.Label(windows,text='Dragon4:').place(x=30,y=120)
tk.Label(windows,text='Dragon5:').place(x=30,y=150)
tk.Label(windows,text='activity id:').place(x=280,y=30)
tk.Label(windows,text='         uid:').place(x=280,y=60)
tk.Label(windows,text='    rule id:').place(x=280,y=90)
tk.Label(windows,text='Qty:').place(x=170,y=30)
tk.Label(windows,text='Qty:').place(x=170,y=60)
tk.Label(windows,text='Qty:').place(x=170,y=90)
tk.Label(windows,text='Qty:').place(x=170,y=120)
tk.Label(windows,text='Qty:').place(x=170,y=150)

var_dragon1 = tk.StringVar()
var_dragon2 = tk.StringVar()
var_dragon3 = tk.StringVar()
var_dragon4 = tk.StringVar()
var_dragon5 = tk.StringVar()
var_qty1 = tk.StringVar()
var_qty2 = tk.StringVar()
var_qty3 = tk.StringVar()
var_qty4 = tk.StringVar()
var_qty5 = tk.StringVar()
var_activityid = tk.StringVar()
var_uid = tk.StringVar()
var_ruleid = tk.StringVar()
var_redis = tk.StringVar()
var_redis.set(1)

tk.Entry(windows,textvar=var_dragon1,width=7).place(x=100,y=33)
tk.Entry(windows,textvar=var_dragon2,width=7).place(x=100,y=63)
tk.Entry(windows,textvar=var_dragon3,width=7).place(x=100,y=93)
tk.Entry(windows,textvar=var_dragon4,width=7).place(x=100,y=123)
tk.Entry(windows,textvar=var_dragon5,width=7).place(x=100,y=153)
tk.Entry(windows,textvar=var_activityid).place(x=350,y=33)
tk.Entry(windows,textvar=var_uid).place(x=350,y=63)
tk.Entry(windows,textvar=var_ruleid).place(x=350,y=93)
tk.Entry(windows,textvar=var_qty1,width=7).place(x=210,y=33)
tk.Entry(windows,textvar=var_qty2,width=7).place(x=210,y=63)
tk.Entry(windows,textvar=var_qty3,width=7).place(x=210,y=93)
tk.Entry(windows,textvar=var_qty4,width=7).place(x=210,y=123)
tk.Entry(windows,textvar=var_qty5,width=7).place(x=210,y=153)
text = tk.Text(windows,width=68,height=8)
text.place(x=10,y=230)

def redis_ad():
    var = var_redis.get()
    return var

tk.Radiobutton(windows,text="秀色",var=var_redis,value={'host':'192.168.83.35','port': 6379,'db':4},command=redis_ad).place(x=30,y=200)
tk.Radiobutton(windows,text="乐嗨",var=var_redis,value={'host':'192.168.83.35','port':6379,'db':8},command=redis_ad).place(x=80,y=200)
tk.Radiobutton(windows,text="红人",var=var_redis,value={'host':'192.168.84.130','port':6379,'db':4},command=redis_ad).place(x=130,y=200)
tk.Radiobutton(windows,text="嗨秀",var=var_redis,value={'host':'192.168.84.134','port':6379,'db':8},command=redis_ad).place(x=180,y=200)
tk.Radiobutton(windows,text="蜜疯",var=var_redis,value={'host':'192.168.84.148','port':6379,'db':9},command=redis_ad).place(x=230,y=200)


def five_dragon():
    pool = redis.ConnectionPool(**eval(redis_ad()))
    r = redis.Redis(connection_pool=pool)
    r.hmset("activity:"+var_activityid.get()+":"+var_ruleid.get()+":"+var_uid.get()+"",{var_dragon1.get(): var_qty1.get(),
                        var_dragon2.get(): var_qty2.get(), var_dragon3.get(): var_qty3.get(),var_dragon4.get(): var_qty4.get(),var_dragon5.get(): var_qty5.get()})

    text.insert(0.0,redis_ad()+"activity:"+var_activityid.get()+":"+var_ruleid.get()+":"+var_uid.get()+"\n")



tk.Button(windows,text='Send',command=five_dragon).place(x=350,y=140)

windows.mainloop()