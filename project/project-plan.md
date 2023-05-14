# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyzes bicycle traffic under different weather conditions. For several selected cities in Germany, the number of bicycles at counting stations is examined and connected to the precipitation in these areas.  

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis helps to understand and make predictions on the interplay between weather and bicycle traffic. The insights may help city planers to optimize traffic routes and public transport. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Verkehrszählung Fahrradverkehr
* Metadata URL: https://mobilithek.info/offers/-6901989592576801458
* Data URL: https://github.com/od-ms/radverkehr-zaehlstellen
* Data Type: CSV

Daily, 15-min intervall countings of bicycles at a certain street in Münster.


### Datasource2: Niederschlagsdaten DWD
* Metadata URL: https://www.dwd.de/DE/leistungen/cdc/cdc_ueberblick-klimadaten.html
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/precipitation/recent/
* Data Type: ZIP

Daily, 10-min intervall of precipitation at weather stations throughout Germany.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
2. Inspect data structure of Datasource1 [#2][i2]
3. Inspect data structure of Datasource2 [#3][i3]
4. Download all relevant files for Datasource1 [#4][i4]
5. Download all relevant files for Datasource2 [#5][i5]
6. Set up data import for Datasource1 [#6][i6]
7. Set up data import for Datasource2 [#7][i7]
8. Clean data of Datasource1 [#8][i8]
9. Clean data of Datasource2 [#9][i9]
10. Aggregate data of Datasource1 [#10][i10]
11. Aggregate data of Datasource2 [#11][i11]
12. Plot data of Datasource1 [#12][i12]
13. Plot data of Datasource2 [#13][i13]
14. Analyze interplay of Datasource1 and Datasource2 [#14][i14]
15. Visualize relationship of Datasource1 and Datasource2 [#15][i15]
16. Comment and clean up code [#16][i16]
17. Formulate conclusion [#17][i17]

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
[i2]: https://github.com/fabalex7/2023-amse/issues/2
[i3]: https://github.com/fabalex7/2023-amse/issues/3
[i4]: https://github.com/fabalex7/2023-amse/issues/4
[i5]: https://github.com/fabalex7/2023-amse/issues/5
[i6]: https://github.com/fabalex7/2023-amse/issues/6
[i7]: https://github.com/fabalex7/2023-amse/issues/7
[i8]: https://github.com/fabalex7/2023-amse/issues/8
[i9]: https://github.com/fabalex7/2023-amse/issues/9
[i10]: https://github.com/fabalex7/2023-amse/issues/10
[i11]: https://github.com/fabalex7/2023-amse/issues/11
[i12]: https://github.com/fabalex7/2023-amse/issues/12
[i13]: https://github.com/fabalex7/2023-amse/issues/13
[i14]: https://github.com/fabalex7/2023-amse/issues/14
[i15]: https://github.com/fabalex7/2023-amse/issues/15
[i16]: https://github.com/fabalex7/2023-amse/issues/16
[i17]: https://github.com/fabalex7/2023-amse/issues/17
