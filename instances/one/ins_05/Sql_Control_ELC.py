'''
SQL配置页面，完成SQL的处理和配置
字典dict：保存表名和sql
'''
from SQLS.Analysis.special_refund import special_refund_sql

from CONFS.platforms_conf import *

save_path = r'D:\Users\xuwenjie\Desktop\审计数据分析\指定退款ID'  # TODO 保存目录
workbook_name = '指定退款ELC.xlsx'  # TODO 工作簿名称

# TODO 具体时间的SQL
final_sql_01 = special_refund_sql.format('2018-01-01', '2018-12-31 23:59:59')
final_sql_02 = special_refund_sql.format('2019-01-01', '2019-12-31 23:59:59')
final_sql_03 = special_refund_sql.format('2020-01-01', '2020-12-31 23:59:59')

# TODO 具体查询数据库
FINAL_DATABASE = 'uco'

# TODO 执行的所有脚本和工作表名称
# TODO 环境和店铺环境保持一致
execute_plain = {
    # 类似一个脚本
    '特殊电话明细': {
        # 类似一个环境
        'ELC': {
            final_sql_01 % ("','".join(PLA_ENV['ELC'])),
            final_sql_02 % ("','".join(PLA_ENV['ELC'])),
            final_sql_03 % ("','".join(PLA_ENV['ELC'])),
        },
    }
}
