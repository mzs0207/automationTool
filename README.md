# automationTool
# 系统架构
客户端--服务端 或 客户端--代理服务器--服务端(多机房)
客户端通过post方式传递数据给服务端，使用https加密

# 角色功能
服务端：存储监控项数据、判断报警阈值、发送报警、web展示数据、
建立分配调度任务

客户端：采集数据、实现调度任务
代理服务器：中转数据



# 参考资料
实现过程参考以下相关资料，感谢。
http://blog.csdn.net/taiyang1987912/article/details/44850999
http://www.cnblogs.com/cmsd/p/3838269.html