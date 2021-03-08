'''
SQL的模板，待传入参数
-- 收件省为空
'''
none_province_sql = '''SELECT 
    tbs.tradeMainOrderId AS '淘宝订单号',
    so.id AS  'OMS订单号',
    tbs.buyerNick AS '顾客ID',
    tbs.orderPaidTime AS '付款时间',
    tbs.receiverProvince AS '省份',
    so.province AS 'OMS省份',
    tbs.receiverCity AS '市',
    tbs.receiverDistrict AS '区',
    tbs.receiverAddress AS '详细地址',
    so.remark AS '备注',so.omsRemark AS '系统备注',
    SUM(oi.totalPrice+IFNULL(oi.taxFee,0)) AS '订单金额'
 FROM SalesOrder AS so FORCE INDEX(platformIdPaymentTimeIndex)
 JOIN ops.orderlist AS o ON o.salesOrderId = so.id AND o.type = 1 -- 已发货订单
 JOIN ops.orderlist_item AS oi ON oi.orderlistId = o.id AND o.isDeleted = 0 -- 产品明细行
 JOIN TbSalesOrder AS tbs ON tbs.tradeMainOrderId = oi.tbSalesOrderId AND tbs.orderStatus = 'TRADE_FINISHED' -- 订单交易完成
 JOIN Platform AS pf ON pf.pKey = so.platformId -- 店铺信息表
 WHERE so.paymentTime BETWEEN '{}' AND '{}'
 AND so.platformId IN('%s') -- 指定店铺
 AND tbs.receiverProvince IN('雪兰莪',
'槟榔屿',
'New South ',
'Alabama',
'Colorado',
'Florida',
'New Brunsw',
'New South ',
'New York',
'Ontario',
'Pulau Pina',
'Saskatchew',
'Victoria',
'Western Au',
'東京都',
'New York',
'New South ',
'Texas',
'Western Au',
'??',
'New South ',
'Quebec',
'Indiana',
'New South Wales',
'Massachusetts',
'Victoria',
'British Columbia',
'California',
'Connecticut',
'Massachusetts',
'New South Wales',
'Ontario',
'Queensland',
'South Australia',
'Tasmania',
'Victoria',
'เชยงใหม',
'愛知県',
'東京都',
'California',
'New South Wales',
'Victoria',
'Ontario',
'26  Ardmore  Bukit  Timah  Holland  Road',
'California',
'British Columbia',
'California',
'Ohio',
'Ontario')
 GROUP BY tbs.tradeMainOrderId;'''

if __name__ == '__main__':
    platforms = ('100087',)
    print(sql.format('2020-01-01','2020-01-02')%("','".join(platforms)))