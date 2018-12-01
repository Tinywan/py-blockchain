# py-blockchain

#### 生成requirements.txt文件
```
pip freeze > requirements.txt
```

#### 安装requirements.txt依赖
```
pip install -r requirements.txt
```

#### 需求环境
###### 新建目录
```
mkdir lesson01
cd lesson01
```
###### 安装 pipenv
```
pip install pipenv
```
###### 安装 flask 
```
pipenv install flask==0.12.2
```
###### 安装 request
```
pipenv install request==2.18.4
```

###### 区块

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
[Python新利器之pipenv](https://www.jianshu.com/p/00af447f0005)
[Python新利器之pipenv](https://www.jianshu.com/p/00af447f0005)