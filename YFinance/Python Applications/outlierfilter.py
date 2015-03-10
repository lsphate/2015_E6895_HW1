import math

def stof(x):
    try:
        return float(x[0])
    except (ValueError, TypeError):
        return 0.0

price = sc.textFile("PRICE_DATA_NAME").map(lambda line: line.split(' '))
pricen = price.map(stof)
stats = pricen.stats()
stddev = stats.stdev()
mean = stats.mean()
outliers = pricen.filter(lambda x: math.fabs(x - mean) > 2 * stddev)
print outliers.collect()
