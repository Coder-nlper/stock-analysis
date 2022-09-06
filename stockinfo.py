import akshare as ak

def all_stock_real_time_info():
	# 沪深京三市股票实时信息
	stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
	print(stock_zh_a_spot_em_df)
	# 沪A实时信息
	stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
	print(stock_sh_a_spot_em_df)
	# 深A实时信息
	stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
	print(stock_sz_a_spot_em_df)
	# 京A实时信息
	stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
	print(stock_bj_a_spot_em_df)
	# 新股
	stock_new_a_spot_em_df = ak.stock_new_a_spot_em()
	print(stock_new_a_spot_em_df)
	# 科创板
	stock_kc_a_spot_em_em_df = ak.stock_kc_a_spot_em()
	print(stock_kc_a_spot_em_em_df)
	#股票指数
	stock_zh_index_spot_df = ak.stock_zh_index_spot()
	print(stock_zh_index_spot_df)

def money_flow():
	# 板块资金流排名 {"今日", "5日", "10日"},  {"行业资金流": "2", "概念资金流": "3", "地域资金流": "1"}
	stock_sector_fund_flow_rank_df = ak.stock_sector_fund_flow_rank(indicator="今日",
		                                                            sector_type="行业资金流")
	print(stock_sector_fund_flow_rank_df)
	# 个股资金流排名  {"今日", "3日", "5日", "10日"}
	stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank(indicator="今日")
	print(stock_individual_fund_flow_rank_df)

def singel_stock_info(stock_code, start_date, end_date, adjust=""):
	stock_type="sh"
	if stock_code.startswith("00"):
		stock_type="sz"
	# 股票基本信息
	#stock_individual_info_em_df = ak.stock_individual_info_em(symbol=stock_code)
	#print(stock_individual_info_em_df)
	# 股票历史交易信息，period有'daily', 'weekly', 'monthly'，
	# 复权信息：adjust有qfq: 前复权; hfq: 后复权，默认不复权
	stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_code,
		                                   period="daily",
		                                   start_date=start_date,
		                                   end_date=end_date,
		                                   adjust=adjust)
	print(stock_zh_a_hist_df)
	# 分时数据 1, 5, 15, 30, 60 单位：分钟
	stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol=stock_code,
		                                                 start_date=start_date,
		                                                 end_date=end_date,
		                                                 period='1',
		                                                 adjust=adjust)
	print(stock_zh_a_hist_min_em_df)
	#盘前数据
	stock_zh_a_hist_pre_min_em_df = ak.stock_zh_a_hist_pre_min_em(symbol=stock_code,
		                                                          start_time="09:00:00",
		                                                          end_time="09:31:00")
	print(stock_zh_a_hist_pre_min_em_df)
	# 历史分笔数据，当日数据在晚上10点后更新
	stock_zh_a_tick_163_df = ak.stock_zh_a_tick_163(symbol=stock_type + stock_code,
		                                            trade_date=end_date)
	print(stock_zh_a_tick_163_df)
	# 股资金流
	stock_individual_fund_flow_df = ak.stock_individual_fund_flow(stock=stock_code, market=stock_type)
	print(stock_individual_fund_flow_df)



if __name__ == '__main__':
	#singel_stock_info(stock_code="600033", start_date="20200505", end_date="20220905",adjust="qfq")
	#all_stock_real_time_info()
	money_flow()