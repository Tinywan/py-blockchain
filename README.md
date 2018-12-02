### 区块

```
{
    "index":0, // 块索引
    "timestamp:"", // 时间戳
    "transactions":{ // 交易信息，一个数组
        "sender":"",
        "recipient":"",
        "amount":"100.00"
    },
    "proof":"", // 工作量证明
    "previous_hash":"" // 上一个区块的哈希值
}
```
## 接口调用  
#### 创建区块    
* 请求地址：`http://127.0.0.1:5000/transactions/new`
* 请求方式：`POST`
* 请求参数：
    ```
    {
        "sender":"Tinywan",
        "recipient":"Ai",
        "amount":100
    }
    ```
* 响应结果：
    ```
    {
        "message": "Transaction will be added to Block 2"
    }
    ```    
#### 获取所有的区块  
* 请求地址：`http://127.0.0.1:5000/chain`
* 请求方式：`GET`
* 响应结果：
    ```
    {
        "chain": [
            {
                "index": 1,
                "previous_hash": 1,
                "proof": 100,
                "timestamp": 1543666409.1956131,
                "transactions": []
            },
            {
                "index": 2,
                "previous_hash": "2247f6a2db347ae65c7568e09e6bdef246b2b18dbcdc94630832db78f5c99262",
                "proof": 35293,
                "timestamp": 1543666418.8082924,
                "transactions": [
                    {
                        "amount": 1,
                        "recipient": "7645ac7a096b4b3aafb9c211334d0f5d",
                        "sender": "0"
                    }
                ]
            },
            {
                "index": 3,
                "previous_hash": "266575731b70e8c4e3ee3808e72f9deb9c9f00ea6faeb9b33be018efa3f11e2a",
                "proof": 35089,
                "timestamp": 1543666421.0963986,
                "transactions": [
                    {
                        "amount": 1,
                        "recipient": "7645ac7a096b4b3aafb9c211334d0f5d",
                        "sender": "0"
                    }
                ]
            }
        ],
        "length": 7
    }
    ```
#### 挖矿   
* 请求地址：`http://127.0.0.1:5000/mine`
* 请求方式：`GET`
* 响应参数：
    ```
    {
        "index": 11,
        "message": "New Block Forged",
        "previous_hash": "59d1a9905710bee3e30b2ec5472aa73a671a5bf90dba7b17f19c94354a2f7009",
        "proof": [
            {
                "amount": 1,
                "recipient": "7645ac7a096b4b3aafb9c211334d0f5d",
                "sender": "0"
            }
        ],
        "transactions": [
            {
                "amount": 1,
                "recipient": "7645ac7a096b4b3aafb9c211334d0f5d",
                "sender": "0"
            }
        ]
    }
    ```    
#### 注册节点   
* 请求地址：`http://127.0.0.1:5000/node/register`
* 请求方式：`POST`
* 请求参数：
    ```
    {
        "nodes":["https://127.0.0.1:5004"]
    }
    ```    
* 响应结果：
    ```
    {
        "message": "New nodes had added",
        "total_nodes": [
            "127.0.0.1:5001",
            "127.0.0.1:5004",
            "127.0.0.1:5002"
        ]
    }
    ```        

## 需求环境
#### 新建目录
```
mkdir lesson01
cd lesson01
```
#### 安装 pipenv
```
pip install pipenv
```
#### 安装 flask 
```
pipenv install flask==0.12.2
```
> Windows 环境 `pip install flask`  

#### 安装 request
```
pipenv install request==2.18.4
```
> Windows 环境 `pip install request`      

## 知识点
* import与from import使用及区别
    * import语句 ： 
        * 描述：在开始使用一个模块中的函数之前，必须用import语句导入该模块。
        * 语法：`import module1[, module2[,... moduleN]]`
        * 案例：使用random模块ranint() 函数
            ```
            import random
            for i in range(5):
            print(random.randint(1, 10))
            ```
    * from import语句 ： 
        * 描述：这是导入模块的另一种形式，使用这种形式的 import 语句， 调用 模块中的函数时不需要 moduleName. 前缀
        * 语法：`from moduleName import name1[, name2[, ... nameN]]|*`
        * 案例：使用random模块ranint() 函数
        ```
        from random import *
        for i in range(5):
        print(randint(1, 10)) # 这里就不需要random.前缀了
        ```     
## 错误
错误1、`TypeError: 'dict' object is not callable`
```
self.last_block("index") + 1 修改为 self.last_block['index'] + 1
```
## 参考文档  
* [Python新利器之pipenv](https://www.jianshu.com/p/00af447f0005)
* [Flask 是一个 Python 实现的 Web 开发微框架](http://docs.jinkan.org/docs/flask/)