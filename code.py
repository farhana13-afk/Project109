import statistics
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
rs = df["reading score"].to_list()

rs_mean = statistics.mean(rs)
rs_median = statistics.median(rs)
rs_mode = statistics.mode(rs)
rs_stddev = statistics.stdev(rs)

first_rs_std_dev_start, first_rs_std_dev_end = rs_mean - rs_stddev, rs_mean + rs_stddev
second_rs_std_dev_start, second_rs_std_dev_end = rs_mean - (2*rs_stddev), rs_mean + (2*rs_stddev)
third_rs_std_dev_start, third_rs_std_dev_end = rs_mean - (3*rs_stddev), rs_mean + (3*rs_stddev)


list_of_data_within_1_std_deviation = [result for result in rs if result > first_rs_std_dev_start and result < first_rs_std_dev_end]
list_of_data_within_2_std_deviation = [result for result in rs if result > second_rs_std_dev_start and result < second_rs_std_dev_end]
list_of_data_within_3_std_deviation = [result for result in rs if result > third_rs_std_dev_start and result < third_rs_std_dev_end]

print("Mean of this data is {}".format(rs_mean))
print("Median of this data is {}".format(rs_median))
print("Mode of this data is {}".format(rs_mode))
print("Standard deviation of this data is {}".format(rs_stddev))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(rs)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(rs)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(rs)))
