'''
SQL的模板，待传入参数
-- 包材订单明细
'''
bc_sql = '''SELECT 
		oi.tbSalesOrderId AS '淘宝单号',
		pf.`name` AS '店铺',
		so.platformCustomerId AS '顾客ID',
		so.paymentTime AS '付款时间',
		p.productCode AS '产品编码',
		p.`name` AS '产品名称',
		oi.totalPrice+IFNULL(oi.taxFee,0) AS '产品金额'
	FROM SalesOrder AS so FORCE INDEX(platformIdPaymentTimeIndex)
	JOIN ops.orderlist AS o ON o.salesOrderId = so.id AND o.type = 1 -- 已发货订单
	JOIN ops.orderlist_item AS oi ON oi.orderlistId = o.id AND o.isDeleted = 0 -- 产品明细行
	JOIN TbSalesOrder AS tbs ON tbs.tradeMainOrderId = oi.tbSalesOrderId AND tbs.orderStatus = 'TRADE_FINISHED' -- 订单交易完成
	JOIN Product AS p ON p.productCode = oi.productCode -- 产品信息表
	JOIN Platform AS pf ON pf.pKey = so.platformId -- 店铺信息表
	WHERE so.paymentTime BETWEEN '{}' AND '{}'
	AND so.platformId IN('%s')
	AND p.salesType = 50;'''

if __name__ == '__main__':
    platforms = ('100087',)
    print(sql.format('2020-01-01','2020-01-02')%("','".join(platforms)))