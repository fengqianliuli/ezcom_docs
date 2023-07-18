
# 概述

![https://en.cppreference.com/w/cpp/14](https://img.shields.io/badge/language-C%2B%2B14-brightgreen)
![https://xmake.io/#/zh-cn/](https://img.shields.io/badge/xmake-v2.7.9-blue)


## EZcom是什么

EZcom是一个轻量化、API易用的C++通信库

EZcom使用protobuf进行序列化，底层封装了ZMQ进行通信，并原生支持ZMQ的IPC和TCP通信模式。

因此EZcom需要依赖的三方库有：
- [protobuf (>=3.6.0)](https://github.com/protocolbuffers/protobuf)
- [libzmq (>=4.3.2)](https://github.com/zeromq/libzmq)

## EZcom支持什么

- 支持跨域、跨设备tcp网络通信
- client-server模式下支持connect回调获取当前连接状态
- 支持的通信模式
  - 同步-异步请求回复/超时机制
  - 发布-订阅消息模式/topic机制
- 支持基本数据类型的自动序列化
  - int32
  - int64
  - uint32
  - uint64
  - float
  - double
  - bool
  - string
- 支持用户自定义数据结构的强制序列化，利用reinterpret_cast强制转换。需要两端字节对齐

## EZcom的架构设计图

![架构图](../_static/images/structure_diagram.png)




