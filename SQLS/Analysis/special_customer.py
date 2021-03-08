'''
SQL的模板，待传入参数
-- 特殊顾客ID
'''
special_customer_sql = '''
SELECT pf.`name` AS '店铺',
so.platformOrderId AS '销售单号',so.id AS 'OMS订单号',
so.paymentTime AS '付款时间',YEAR(so.paymentTime) AS '付款年份',
so.platformCustomerId AS '顾客ID',
CASE WHEN IFNULL(so.recipientMobile,'')='' THEN so.recipientPhone ELSE so.recipientMobile END AS '收件电话',
so.province AS '省',so.city AS '市',so.district AS '区',so.address AS '详细地址',
GROUP_CONCAT(p.productCode,'(',p.`name`,')') AS '订单明细',
SUM(oi.totalPrice+IFNULL(oi.taxFee,0)) AS '订单金额'
FROM SalesOrder AS so FORCE INDEX(platformCustomerIdIndex)
JOIN ops.orderlist AS o ON o.salesOrderId = so.id AND o.type = 1 -- 已发货订单
JOIN ops.orderlist_item AS oi ON oi.orderlistId = o.id AND o.isDeleted = 0 -- 产品明细行
JOIN Product AS p ON p.productCode = oi.productCode
JOIN TbSalesOrder AS tbs ON tbs.tradeMainOrderId = oi.tbSalesOrderId AND tbs.orderStatus = 'TRADE_FINISHED' -- 订单交易完成
JOIN Platform AS pf ON pf.pKey = so.platformId -- 店铺信息表
WHERE so.paymentTime BETWEEN '{}' AND '{}'
AND so.platformId IN('%s') -- 指定店铺
AND so.platformCustomerId IN('小象优品go',
'麦克疯33',
'小象采购',
'常州象源123',
'yscg003')
GROUP BY so.id;'''

if __name__ == '__main__':
    platforms = ('100087',)
    print(special_customer_sql.format('2020-01-01','2020-01-02')%("','".join(platforms)))