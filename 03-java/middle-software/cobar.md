## cobar相关

---

####  附录


* [源代码](https://github.com/alibaba/cobar)

* [源码阅读笔记](cobar-sourcecode.md)

* [常见问题](https://github.com/alibaba/cobar/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E7%AD%94)

---

#### 简介

Cobar是关系型数据的分布式处理系统，它可以在分布式的环境下看上去像传统数据库一样为您提供海量数据服务。

Cobar遵循MySQL协议，访问Cobar的方式与访问MySQL数据库完全相同。

#### Cobar解决的问题

**注意事项 **

1.请注意表的拆分方式,一张表水平拆分多份到不同的库中,而不是放入同一个库中。


#### 逻辑层次图

![image](img/7.png)

* dataSource:数据源,表示一个具体的数据库连接,与一个物理存在的schema一一对应。 
* dataNode:数据节点,由主、备数据源,数据源的HA以及连接池共同组成,可以将一个dataNode理解为一 个分库。
* tableRule:路由规则,用于判断SQL语句被路由到具体哪些 datanode执行。 
* schema:cobar可以定义包含拆分表的schema(如schema1),也可以定义无拆分表的schema(如 schema2)。
* 以上层次关系具有较强的灵活性,用户可以将表自由放置不同的datanode,也可将不同的datasource放置在 同一MySQL实例上。
#### 使用手册

Cobar的主要目录如下:

```
bin #包含Cobar的启动、重启、停止等脚本文件 
conf #包含Cobar所有配置文件
```
Cobar的所有配置文件全部放在conf目录中,进入conf目录,可以看到:

```
schema.xml #schema,dataNode,dataSource相关配置 
rule.xml #分布式规则定义
```

* dataSource

数据源是一个具体的后端数据连接的表示

```
<dataSource name="ds_shard_master"  type="mysql"> 
	<property name="location">
	</property>
```

上例中配置了4个数据源,数据源名称分别为ds_shard_master[0]、ds_shard_master[1]、 ds_shard_master[2]、ds_shard_master[3],按照用户location中配置的顺序,对应关系如下:

| 数据源名称| 数据源地址| 
| ------------ | ------------- | 
| ds_shard_master[0]| 192.168.0.4:3306/shard  | 
| ds_shard_master[1]| 192.168.0.4:3306/shard1 | 
| ds_shard_master[2]| 192.168.0.4:3306/shard2 | 
| ds_shard_master[3]| 192.168.0.4:3306/shard3  | 

* dataNode

数据节点由主、备数据源,心跳,连接池等配置组成

```
<dataNode name="dn_shard"> 
	<property name="dataSource">
	</property>
</dataNode>
```
数据节点的主备对应关系如下:

|节点名称 |主数据源|备数据源
|dn_shard[1]|ds_shard_master[1]|ds_shard_slave[1]

* schema

schema定义了Cobar展示给用户的schema，schema由dataNode以及rule.xml中定义的路由规则共同组成。


```
// 所有除tb1,tb2,tb3,tb4之外表的访问都路由到dn_shard[0]去执行
<schema name="db_shard" dataNode="dn_shard[0]">
</schema>
```

* rule.xml 




// tableRule名称
<tableRule name="tb1Rule">
</tableRule>


	</rule>
	//当SQL语句中只有val,无id字段时,匹配此规则,id参数设置为null



system主要是系统参数定义，包括服务端口、管理端口、处理器个数、线程池等

<property name="managerPort">9066</property>




<property name="processorHandler">8</property> 





