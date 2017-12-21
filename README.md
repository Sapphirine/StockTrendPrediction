# StockTrendPrediction
Columbia University EECS6893 Big Data Final Project -- Yucan Liu (yl3791), Yuxin Ding (yd2405)

## Directory
```
StockTrendPrediction
|
+--python
|   +--kmeans_reg.py
|   +--coint_reg.py
+--data
    +--output
          +--...some sample data...
    +--single
          +--...some sample data...
    +--nasdaqlisted.txt
    +--otherlisted.txt
    +--sp500.txt
    +--generate_all_data.py
    +--generate_single_data.py
    +--getDiff.py
```

## Usage
1. `generate_all_data.py` is a python script, which will automatically download a group of stock data. This Python file will read from an external file first and load all the target stocks’ names. Then, it will download the data that fulfill the requirement (has valid data in the design time frame) and write into a CSV file in the given directory.

2. `generate_single_data.py` is another python script, which works similar to generate_all_data.py file. It will simply download a given stock’s data within a provided date frame. The result will be written into a CSV file, which can be read as a dataframe for our further experiments.

3. `kmeans_reg.py` is the python file that runs stock prediction algorithm with finding correlating stock data by k-means. The input is the target data, the data pool of other data and the delay days. Two input datasets are in two individual csv files. Date is the row and companies are the columns. The delay date is a list of days, defaulted as [5, 20, 40, 60, 100, 120]. The output is the prediction accuracy of regression with k-means compared regression without k-means.

4. `coint_reg.py` is the python file that runs stock prediction algorithm with finding correlating stock data by cointegration. The input is the target data, the data pool of other data and the delay days. Two input format is the same as previously stated. The output is the prediction accuracy of regression with cointegration compared regression without cointegration.
