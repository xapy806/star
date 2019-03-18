from sqlite3 import Cursor
from datetime import date
from django.db import models

# Create your models here.
from content.models import Course
from user.models import User

#  订单编号字段  继承
#  ---1.救命啊，这是什么东东？？？ 一脸蒙蔽
#  ---2.硬着头皮上！

class OrderNumber(models.CharField):
    # 不用写 init ， 只是进行数据的存储
    def get_db_prep_value(self, value, connection, prepared=False):
        # value 是 字段值, 有值的话应该是之前的更新，没有值的话需要处理
        # connection 连接数据库
        # print('-----value----',value)
        if not value:  # 避免 更新时 重新生成 定单号
            # 创建游标  申明式类型的写法（运行起来后 解析器 根据它的值 动态的去解析它的类型） 。。。
            cursor:Cursor = connection.cursor()

            # 取出订单号最大的那个（从第一个位置开始取出第一个数）
            cursor.execute('select orn from t_order order by id desc limit 0,1')

            current_date = date.strftime(date.today(),'%Y%y%d')
            if cursor.rowcount > 0: # 没有记录时 rowcount = -1  ----> bool值显示为True
                orn = cursor.fetchone()[0]    # 返回元组
                date_, number = orn[:8], orn[8:]

                if date_ == current_date:
                    #  字符串填充：'1'.ljust(4,'0')  返回 '1000'
                    number = str(int(number)+1).rjust(4,'0')
                    # 必须返回 date_ 否则会报错？？？ 记得请教disen
                    return '%s%s' % (date_,number)
            # if row:

            # 如果说当前没有rowcount 数据，返回当前第一单
            # 如果有数据，但是时间不对，也返回当前第一单
            return '%s0001' % current_date

        return value


class Order(models.Model):

    pay_status_t = ((0, '未支付'), (1, '已支付'), (2, '正在支付'))

    # 自定义订单号？？？
    orn = OrderNumber(max_length=20,
                          verbose_name='定单号')

    title = models.CharField(max_length=100,
                             verbose_name='标题')

    pay = models.DecimalField(verbose_name='支付金额',
                                max_digits=10,
                                decimal_places=2)

    create_time = models.DateTimeField(verbose_name='下单时间',
                                    auto_now_add=True)

    update_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True)

    pay_type = models.IntegerField(verbose_name='订单状态',
                                     choices=pay_status_t,
                                     default=0)

    user_id = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='用户ID',
                             null=True)

    def __str__(self):
        return self.title

    @property  # 把一个方法变成属性
    def pay_status_name(self):
        return self.pay_status_t[self.pay_type][1]

    class Meta:
        db_table = 't_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              verbose_name='订单')

    course = models.ForeignKey(Course,
                             on_delete=models.CASCADE,
                             verbose_name='课程')

    cnt = models.IntegerField(verbose_name='数量',
                              default=1)

    price = models.DecimalField(verbose_name='单价',
                                max_digits=10,
                                decimal_places=2)

    def __str__(self):
        return self.order.orn

    class Meta:
        db_table = 't_order_item'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
