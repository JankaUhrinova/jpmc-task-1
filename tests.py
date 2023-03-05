#testable with pytest
from client import getRatio, getDataPoint

quote = {'stock':'ABC',
             'top_bid':{'price':118.24},
             'top_ask':{'price':120.24},
             }

def test_price_is_average():
    assert getDataPoint(quote)[3] == (getDataPoint(quote)[1]+getDataPoint(quote)[2])/2 

def test_getRatio_returns_ratio():
    assert getRatio(10.4,4.5) == 10.4/4.5

def test_stock_price_is_0():
    assert getRatio(10,0) == None

