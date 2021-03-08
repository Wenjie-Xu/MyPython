'''
02 - 订单渠道
'''
from SQLS.ITDD.common import date_limit

sql_01 = '''-- 2、订单渠道
SELECT 
YEAR(tbs.orderConsignTime) AS '年份',
MONTH(tbs.orderConsignTime) AS '月份',
pf.businessType AS '订单渠道（平台）',
SUM(((tbso.itemAmount*tbso.itemPrice) - IFNULL(tbso.itemDiscountFee,0) - IFNULL(tbso.partMjzDiscount,0)
  + IFNULL(tbso.adjustFee,0))/100 + IFNULL(tbso.taxFee,0))  AS '订单总金额',
COUNT(DISTINCT tbs.tradeMainOrderId) AS '订单总数量',
COUNT(DISTINCT tbs.buyerNick) AS '消费者（下单人ID）总数量'
FROM TbSalesOrder AS tbs 
JOIN TbSubOrder AS tbso ON tbso.tradeMainOrderId = tbs.tradeMainOrderId 
JOIN SalesOrderLine AS sol ON sol.tbTradeSubOrderId = tbso.tradeSubOrderId AND sol.isEnable = 1
JOIN Product AS p ON p.productCode = sol.productCode AND p.type <> 6 -- 1、剔除电子券 
JOIN SalesOrder AS so FORCE INDEX(platformIdPaymentTimeIndex) ON so.id = sol.salesOrderId AND so.`status` = 4 -- 已发货
JOIN Platform AS pf ON pf.pKey = so.platformId
WHERE so.paymentTime BETWEEN DATE_SUB('{}',INTERVAL 2 MONTH) AND '{}'
AND tbs.orderConsignTime BETWEEN '{}' AND '{}' -- 1、发货时间
AND so.platformId IN('%s')'''+date_limit

sql_02 = '''
AND so.warehouse NOT IN('990','1290') -- 2、剔除虚拟仓
AND tbs.orderStatus = 'TRADE_FINISHED' -- 3、交易成功
AND NOT (tbso.refundStatus = 'SUCCESS' AND IFNULL(tbso.refundApplyTime,tbs.endTime) < tbs.endTime) -- 4、剔除发货前退款成功
AND (so.internalRemark NOT LIKE '%试拍%' AND so.omsRemark NOT LIKE '%试拍%') -- 5、剔除试拍订单
GROUP BY 1,2,3;
'''

if __name__ == '__main__':
    platforms = ('100087',)
    print(sql_01.format('2020-01-01','2020-12-31 23:59:59', '2020-01-01', '2020-12-31 23:59:59')%("','".join(platforms))+sql_02)
