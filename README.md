## web  po模式
- 基于pom模式 ui自动化框架模板 pytest+selenium3+allure
#### 目录结构如下
- [x] config 配置文件目录
- [x] data 存放测试数据 excel yaml
- [x] logs 存放日志文件
- [x] public 存放basepage和所有业务封装代码
- [x] report 生成allure报告
- [x] testcase 测试用例编写 
- [x] utils 封装各种数据处理

支持参数驱动、自定义钩子函数、网络异常检测、失败截图、失败重试
***
#### 运行
    python run.py
支持所有pytest 运行方式 
