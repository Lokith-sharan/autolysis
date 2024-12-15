# Analysis of happiness.csv

## Dataset Overview
This dataset has the following key characteristics:

### Summary Statistics
```plaintext
                                   count unique        top freq        mean       std     min     25%     50%      75%     max
Country name                        2363    165  Argentina   18         NaN       NaN     NaN     NaN     NaN      NaN     NaN
year                              2363.0    NaN        NaN  NaN  2014.76386  5.059436  2005.0  2011.0  2015.0   2019.0  2023.0
Life Ladder                       2363.0    NaN        NaN  NaN    5.483566  1.125522   1.281   4.647   5.449   6.3235   8.019
Log GDP per capita                2335.0    NaN        NaN  NaN    9.399671  1.152069   5.527  8.5065   9.503  10.3925  11.676
Social support                    2350.0    NaN        NaN  NaN    0.809369  0.121212   0.228   0.744  0.8345    0.904   0.987
Healthy life expectancy at birth  2300.0    NaN        NaN  NaN   63.401828  6.842644    6.72  59.195    65.1  68.5525    74.6
Freedom to make life choices      2327.0    NaN        NaN  NaN    0.750282  0.139357   0.228   0.661   0.771    0.862   0.985
Generosity                        2282.0    NaN        NaN  NaN    0.000098  0.161388   -0.34  -0.112  -0.022  0.09375     0.7
Perceptions of corruption         2238.0    NaN        NaN  NaN    0.743971  0.184865   0.035   0.687  0.7985  0.86775   0.983
Positive affect                   2339.0    NaN        NaN  NaN    0.651882   0.10624   0.179   0.572   0.663    0.737   0.884
Negative affect                   2347.0    NaN        NaN  NaN    0.273151  0.087131   0.083   0.209   0.262    0.326   0.705

### Missing Values
```plaintext
Country name                          0
year                                  0
Life Ladder                           0
Log GDP per capita                   28
Social support                       13
Healthy life expectancy at birth     63
Freedom to make life choices         36
Generosity                           81
Perceptions of corruption           125
Positive affect                      24
Negative affect                      16

## Visualizations

### Correlation Matrix
![Correlation Matrix](correlation_matrix.png)
### Pairplot
![Pairplot](pairplot.png)

## Narrative Insights
The analysis reveals significant trends and patterns in the dataset. Correlation matrix and pairplot provide insights into relationships among variables.

More detailed findings are generated below.


Based on the provided dataset summary and the statistics for each variable, here’s a detailed analysis of the data:

### Overview of the Dataset

1. **Number of Entries**: The dataset comprises 2,363 entries with various attributes related to the quality of life indicators across different countries and years.

2. **Country Information**: There are 165 unique countries represented, with Argentina appearing the most frequently (18 times).

3. **Year Information**: The data spans multiple years, with a mean year of approximately 2014.76 and a range from 2005 to 2023. This suggests that data might be variously collected over this period, indicating how well-being measures have changed.

### Key Variables Analysis

- **Life Ladder**:
  - **Mean (5.48)**: Overall, individuals report a moderate level of life satisfaction on a scale ranging generally between 0 and 10.
  - **Standard Deviation (1.13)**: There is some variability in life satisfaction across different observations.
  - **Range (1.28 to 8.02)**: Indicates that some countries score significantly higher, reflecting potential disparities in life satisfaction.

- **Log GDP per Capita**:
  - **Mean (9.4)**: Indicates good economic performance on average, with values typically reflecting a higher standard of living.
  - **Standard Deviation (1.15)**: Suggests varied economic performance among countries.
  - **Range (5.53 to 11.68)**: Ashows significant economic diversity, likely between developed and developing nations.

- **Social Support**:
  - **Mean (0.81)**: Suggests that people generally perceive a moderate to high level of social support available to them.
  - **Standard Deviation (0.12)**: Some differences in perceptions of social support are observed.
  - **Range (0.23 to 0.99)**: Indicates that some individuals may feel less supported, which could reflect societal issues in certain regions.

- **Healthy Life Expectancy**:
  - **Mean (63.4 years)**: Reflects reasonable health outcomes but may overshadow significant differences in health systems across countries.
  - **Standard Deviation (6.84)**: There is variability in health outcomes.
  - **Range (6.72 to 74.6)**: Suggests discrepancies in health care access and quality.

- **Freedom to Make Life Choices**:
  - **Mean (0.75)**: Indicates a generally high perception of freedom among individuals.
  - **Standard Deviation (0.14)** and **range (0.23 to 0.99)**: Reflect variance in how freedoms are perceived.

- **Generosity**:
  - **Mean (0.0001)**: This value indicates that average generosity levels are very low or nearly neutral.
  - **Standard Deviation (0.16)**: Shows noticeable variation in generosity, which could be tied to cultural factors.
  - **Range (-0.34 to 0.7)**: Suggests overall scarcity in perceived generosity, which could reflect economic conditions or cultural aspects.

- **Perceptions of Corruption**:
  - **Mean (0.74)**: Indicates a moderate perception of corruption.
  - **Standard Deviation (0.18)**: Different perceptions are evident among countries.
  - **Range (0.035 to 0.983)**: Highlights significant variance in views on corruption.

- **Positive and Negative Affect**:
  - **Mean Positive Affect (0.65)** and **Mean Negative Affect (0.27)**: The positive affect is higher than negative affect on average, suggesting generally positive emotional experiences in the population.
  - **Ranges (**Positive Affect: 0.18 to 0.88**, **Negative Affect: 0.08 to 0.71**): This suggests there are populations experiencing more negativity, likely reflecting social, economic, or health concerns.

### Missing Values

- **Missing Data**: Some fields contain missing values, particularly in the metrics of **Log GDP per Capita (28)**, **Generosity (81)**, and **Perceptions of Corruption (125)**. It may be important to consider methods such as imputation or exclusion of these rows/columns in analyses depending on the analysis aims.
  
To summarize, the dataset presents a rich landscape of well-being measures correlated with economic and social indicators across various countries. The presence of significant variability within many variables suggests potential areas for further investigation into socio-economic or cultural factors. The missing values in certain fields should be addressed to maintain the integrity of analyses.