Title: The a second article
Date: 2013-12-01 10:02

See below intra-site link examples in Markdown format.


```python
class InvestCollect(xydata.DailyCollect):
    """
    投资数据处理
    """

    def __init__(self):
        xydata.DailyCollect.__init__(self)
        self.column_list = ["FuiInvestId", "FuiUid", "FuiLoanId", "FuiCreateTime", "FuiInvestMoney", "FuiLoanAmount",
                            "FuiActiveTime", "FstrInvestSource", "FstrInvestPlatform", "FuiPeriodsDays"]
```

```sql
select FstAccountId from account.t_system_account 
```

#### 2、多期理财回款查询接口

请求：

| 名称 | 字段名 | 类型 | 是否必须 | 示例 | 说明 |
| --- | --- | --- | --- | --- | --- |
| 理财计划id| financial_id | int | 是 | 89405898986651650||

返回：

| 名称 | 字段名 | 类型 | 是否必须 | 示例 | 说明 |
| --- | --- | --- | --- | --- | --- |
| 回款日期时间戳 | date_ts | int | 是 | 1495096688 |回款日期时间戳|
| 下次回款金额 | next_repay_total | int | 是 | 200000 |回款金额，单位：分|
