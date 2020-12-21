from django.db import models


# Create your models here.
class interface(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    url = models.CharField(max_length=32, null=True)  # 链接地址不含头部
    type = models.DecimalField(max_digits=5, decimal_places=2, null=True)  # 请求类型
    body = models.CharField(max_length=300, null=True)  # 请求体
    result = models.CharField(max_length=300, null=True)  # 返回内容
    res = models.CharField(max_length=10, null=True)  # 结果
    time = models.DateField(null=True)  # 最近一次请求时间
