#https://www.akshare.xyz/data/macro/macro.html
import akshare as ak
#宏观数据

def get_china_macro_data(start_date, end_date):
    ## 居民消费价格指数CPI, 工业生产者出厂价格指数PPI
    cpiy_df = ak.macro_china_cpi_yearly()[start_date:end_date]
    cpim_df = ak.macro_china_cpi_monthly()[start_date:end_date]
    ppi_df = ak.macro_china_ppi_yearly()[start_date:end_date]
    print(cpi_df)
    print(ppi_df)
    # 获取GDP数据
    gdp_df = ak.macro_china_gdp_yearly()[start_date:end_date]
    print(gdp_df)
    # LPR
    lpr_df = ak.macro_china_lpr()
    # 社会融资规模
    shrzgm_df = ak.macro_china_shrzgm()
    # 工业增加值增长
    gyzjz_df = ak.macro_china_gyzjz()