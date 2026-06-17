def execute_query(sql_query, df):

    if "SUM(revenue)" in sql_query:
        return df["revenue"].sum()

    if "SUM(units_sold)" in sql_query:
        return df["units_sold"].sum()

    if "promotion_flag" in sql_query:
        return df[df["promotion_flag"] == True]

    return df.head()
