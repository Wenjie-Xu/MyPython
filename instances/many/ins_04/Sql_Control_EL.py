'''
SQL配置页面，完成SQL的处理和配置
字典dict：保存表名和sql
'''
from SQLS.ITDD.sql_12b import sql_01, sql_02

from CONFS.platforms_conf import *

save_path = r'D:\Users\xuwenjie\Desktop\ITDD'  # TODO 保存目录
workbook_name = '(#12b)年度同一下单人金额.xlsx'  # TODO 工作簿名称

# TODO 具体时间的SQL
final_sql_01 = sql_01.format('2018-01-01', '2018-12-31 23:59:59','2018-01-01', '2018-12-31 23:59:59')
final_sql_02 = sql_01.format('2019-01-01', '2019-12-31 23:59:59','2019-01-01', '2019-12-31 23:59:59')
final_sql_03 = sql_01.format('2020-01-01', '2020-12-31 23:59:59','2020-01-01', '2020-12-31 23:59:59')

# TODO 具体查询数据库
FINAL_DATABASE = 'uco'

# TODO 执行的所有脚本和工作表名称
# TODO 环境和店铺环境保持一致
execute_plain = {
    # 类似一个脚本
    '年度同一下单人金额': {
        # 类似一个环境
        'EL': {
            final_sql_01 % ("','".join(PLA_ENV['EL'])) + sql_02,
            final_sql_02 % ("','".join(PLA_ENV['EL'])) + sql_02,
            final_sql_03 % ("','".join(PLA_ENV['EL'])) + sql_02,
        },
        'ELC': {
            final_sql_01 % ("','".join(PLA_ENV['ELC'])) + sql_02,
            final_sql_02 % ("','".join(PLA_ENV['ELC'])) + sql_02,
            final_sql_03 % ("','".join(PLA_ENV['ELC'])) + sql_02,
        },
        'UCO': {
            # 类似一个代码片段
            final_sql_01 % ("','".join(PLA_ENV['UCO'])) + sql_02,
            final_sql_02 % ("','".join(PLA_ENV['UCO'])) + sql_02,
            final_sql_03 % ("','".join(PLA_ENV['UCO'])) + sql_02,
        },
        'YY': {
            final_sql_01 % ("','".join(PLA_ENV['YY'])) + sql_02,
            final_sql_02 % ("','".join(PLA_ENV['YY'])) + sql_02,
            final_sql_03 % ("','".join(PLA_ENV['YY'])) + sql_02,
        },
        '3PL':{
            final_sql_01 % ("','".join(PLA_ENV['3PL'])) + sql_02,
            final_sql_02 % ("','".join(PLA_ENV['3PL'])) + sql_02,
            final_sql_03 % ("','".join(PLA_ENV['3PL'])) + sql_02,
        },
    }
}
