import re

my_str = '''<div>
        <p>【职位描述】<br>1、负责数据后台服务的架构设计、开发、优化；<br><br>【任职要求】<br>1、本科以上学历，计算机相关专业；<br>2、3年以上python开发经验；<br>3、熟悉Unix、Linux操作系统原理及常用工具；<br>4、熟悉TCP/IP协议、进程间通讯编程，熟悉Unix/Linux下常用架构设计方法；<br>5、熟悉Mysql数据库，熟悉NoSQL存储，熟悉面向对象设计；<br>6、具备全面的软件知识结构认知（操作系统、软件工程、设计模式、数据结构、数据库系统、网络安全）；<br>7、具备良好的分析解决问题能力，能独立承担任务，有系统进度把控能力</p>
        </div>'''

result = re.sub("</?[a-zA-Z1-6]+>", "", my_str)
print(result.strip())