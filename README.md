# Hypothesis Testing using 3 inter-related sets of data.

## Definitions:

- A **quarter** is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
- A **recession** is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
- A **recession bottom** is the quarter within a recession which had the lowest GDP.
- A **university town** is a city which has a high percentage of university students compared to the total population of the city.

## Hypothesis
University towns have their mean housing prices less effected by recessions. 
Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

## T-test

A t-test is a statistical test that compares the means of two samples. 

It is used in hypothesis testing, with a null hypothesis that the difference in group means is zero and an alternate hypothesis that the difference in group means is different from zero.
T-test result will either accepts the hypothesis or rejects the same.

### The following data files are available for this assignment:

- From the [Zillow research data](https://www.zillow.com/research/data/) site there is housing data for the United States. In particular the datafile for all homes at a city level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
- From the Wikipedia page on college towns is a [list of university towns](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) in the United States which has been copy and pasted into the file university_towns.txt.
- From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](https://www.bea.gov/data/gdp/gross-domestic-product#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. For this assignment, only look at GDP data from the first quarter of 2000 onward.
