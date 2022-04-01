from pandasql import load_births, load_meat, sqldf


def pysqldf(q): return sqldf(q, globals())


meat = load_meat()
births = load_births()

print(pysqldf("SELECT * FROM meat LIMIT 10;").head())
