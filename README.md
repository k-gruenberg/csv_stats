# csv_stats
A Python script printing various statistics about a given CSV file. Useful as a starting point for data analysis tasks.

## Example

```
$ python3.12 csv_stats.py input.csv --header --class-label is_claim 

No. of rows: 5001
No. of columns: 44
Header?: True
Class label column: 44 (is_claim)

Duplicate rows:
        (1) 2x ('ID42123', '2023-04-06', '0.07', '0.490384615384615', 'C8', '8794', '1', 'B2', 'M6', 'Petrol', '113Nm@4400rpm', '88.50bhp@6000rpm', 'K Series Dual jet', '2', 'No', 'Yes', 'No', 'Yes', 'No', 'Drum', '1197', '4', 'Manual', '5', 'Electric', '4.8', '3845', '1735', '1530', '1335', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', '2', '0')

Rows with missing values:
        (1) 2 missing: ('ID24484', '2023-02-06', '0.16', '0.471153846153846', 'C5', 'NA', '4', 'B2', 'M5', 'Diesel', '200Nm@3000rpm', '88.77bhp@4000rpm', '1.5 Turbocharged Revotorq', 'NA', 'No', 'Yes', 'No', 'Yes', 'No', 'Drum', '1497', '4', 'Manual', '5', 'Electric', '5', '3990', '1755', '1523', '1490', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', '5', '0')
        (2) 2 missing: ('ID43797', '2022-12-24', '0.02', '0.634615384615385', 'C8', 'NA', '1', 'B1', 'M8', 'CNG', '82.1Nm@3400rpm', '55.92bhp@5300rpm', 'K10C', '2', 'NA', 'No', 'No', 'Yes', 'No', 'Drum', '998', '3', 'Manual', '5', 'Power', '4.7', '3655', '1620', '1675', '1340', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', '2', '0')
        (3) 2 missing: ('ID19529', '2023-03-30', '0.15', '0.403846153846154', 'C5', 'NA', '3', 'C2', 'M4', 'Diesel', '250Nm@2750rpm', '113.45bhp@4000rpm', '1.5 L U2 CRDi', 'NA', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Disc', '1493', '4', 'Automatic', '6', 'Power', '5.2', '4300', '1790', '1635', '1720', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', '3', '0')
        (4) 1 missing: ('ID40058', '2022-06-06', '0.02', '0.634615384615385', 'C5', 'NA', '1', 'A', 'M1', 'CNG', '60Nm@3500rpm', '40.36bhp@6000rpm', 'F8D Petrol Engine', '2', 'No', 'No', 'No', 'Yes', 'No', 'Drum', '796', '3', 'Manual', '5', 'Power', '4.6', '3445', '1515', '1475', '1185', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'Yes', '0', '0')
        (5) 1 missing: ('ID02616', '2023-06-19', '0.03', '0.644230769230769', 'C5', 'NA', '5', 'C1', 'M9', 'Diesel', '200Nm@1750rpm', '97.89bhp@3600rpm', 'i-DTEC', '2', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Drum', '1498', '4', 'Manual', '5', 'Electric', '4.9', '3995', '1695', '1501', '1051', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', '4', '0')
        (6) 1 missing: ('ID21492', '2023-02-06', '0.39', '0.548076923076923', 'C8', 'NA', '1', 'C1', 'M2', 'Petrol', '113Nm@4400rpm', '88.50bhp@6000rpm', '1.2 L K12N Dualjet', '2', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Drum', '1197', '4', 'Automatic', '5', 'Electric', '4.8', '3995', '1735', '1515', '1335', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', '2', '0')
        (7) 1 missing: ('ID05492', '2022-04-21', '0.05', '0.394230769230769', 'C8', 'NA', '3', 'C2', 'M4', 'Diesel', '250Nm@2750rpm', '113.45bhp@4000rpm', '1.5 L U2 CRDi', '6', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Disc', '1493', '4', 'Automatic', '6', 'Power', '5.2', '4300', '1790', '1635', '1720', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', '3', '0')
        (8) 1 missing: ('ID43552', '2023-03-03', '0.01', '0.288461538461538', 'C2', 'NA', '3', 'C2', 'M4', 'Diesel', '250Nm@2750rpm', '113.45bhp@4000rpm', '1.5 L U2 CRDi', '6', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Disc', '1493', '4', 'Automatic', '6', 'Power', '5.2', '4300', '1790', '1635', '1720', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', '3', '0')
        (9) 1 missing: ('ID51138', '2022-04-26', '0.02', '0.673076923076923', 'C8', 'NA', '3', 'C2', 'M4', 'Diesel', '250Nm@2750rpm', '113.45bhp@4000rpm', '1.5 L U2 CRDi', '6', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Disc', '1493', '4', 'Automatic', '6', 'Power', '5.2', '4300', '1790', '1635', '1720', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', '3', '0')
        (10) 1 missing: ('ID36128', '2022-03-07', '0.14', '0.432692307692308', 'C8', 'NA', '3', 'C2', 'M4', 'Diesel', '250Nm@2750rpm', '113.45bhp@4000rpm', '1.5 L U2 CRDi', '6', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Disc', '1493', '4', 'Automatic', '6', 'Power', '5.2', '4300', '1790', '1635', '1720', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', '3', '0')
        ...

Columns:
        (001) STR      policy_id                          5_000 distinct values,       0 missing
        (002) STR      policy_date                          727 distinct values,       0 missing
        (003) FLOAT    age_of_car                            35 distinct values,       0 missing: min. 0.00, max. 0.39, 0 neg. values, 462 zero values, 4_539 pos. values
        (004) FLOAT    age_of_policyholder                   66 distinct values,       0 missing: min. 0.29, max. 0.99, 0 neg. values, 0 zero values, 5_001 pos. values
        (005) STR      area_cluster                          40 distinct values,       0 missing
        (006) STR      population_density                    22 distinct values,     400 missing
        (007) INT      make                                   5 distinct values,       0 missing: 3231x '1', 208x '2', 1223x '3', 166x '4', 173x '5'
        (008) STR      segment                                6 distinct values,       0 missing
        (009) STR      model                                 11 distinct values,       0 missing
        (010) STR      fuel_type                              3 distinct values,       0 missing: 1632x 'CNG', 1531x 'Diesel', 1838x 'Petrol'
        (011) STR      max_torque                             9 distinct values,       0 missing
        (012) STR      max_power                              9 distinct values,       0 missing
        (013) STR      engine_type                           11 distinct values,       0 missing
        (014) STR      airbags                                4 distinct values,      17 missing: 109x '1', 3444x '2', 1431x '6', 17x 'NA'
        (015) STR      is_esc                                 3 distinct values,       5 missing: 5x 'NA', 3424x 'No', 1572x 'Yes'
        (016) STR      is_adjustable_steering                 2 distinct values,       0 missing: 1871x 'No', 3130x 'Yes'
        (017) STR      is_tpms                                2 distinct values,       0 missing: 3778x 'No', 1223x 'Yes'
        (018) STR      is_parking_sensors                     2 distinct values,       0 missing: 208x 'No', 4793x 'Yes'
        (019) STR      is_parking_camera                      4 distinct values,       0 missing: 1x '2', 1x '3', 3043x 'No', 1956x 'Yes'
        (020) STR      rear_brakes_type                       2 distinct values,       0 missing: 1223x 'Disc', 3778x 'Drum'
        (021) INT      displacement                           9 distinct values,       0 missing: min. 796.00, max. 1_498.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (022) INT      cylinder                               3 distinct values,       0 missing: 1x '-4', 1762x '3', 3238x '4'
        (023) STR      transmission_type                      2 distinct values,       0 missing: 1752x 'Automatic', 3249x 'Manual'
        (024) INT      gear_box                               2 distinct values,       0 missing: 3747x '5', 1254x '6'
        (025) STR      steering_type                          3 distinct values,       0 missing: 2115x 'Electric', 109x 'Manual', 2777x 'Power'
        (026) FLOAT    turning_radius                         9 distinct values,       0 missing: min. 4.50, max. 5.20, 0 neg. values, 0 zero values, 5_001 pos. values
        (027) INT      length                                 9 distinct values,       0 missing: min. 3_445.00, max. 4_300.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (028) INT      width                                 11 distinct values,       0 missing: min. 1_475.00, max. 20_137.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (029) INT      height                                11 distinct values,       0 missing: min. 1_475.00, max. 1_825.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (030) INT      gross_weight                          10 distinct values,       0 missing: min. 1_051.00, max. 1_720.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (031) STR      is_front_fog_lights                    2 distinct values,       0 missing: 2006x 'No', 2995x 'Yes'
        (032) STR      is_rear_window_wiper                   2 distinct values,       0 missing: 3566x 'No', 1435x 'Yes'
        (033) STR      is_rear_window_washer                  2 distinct values,       0 missing: 3566x 'No', 1435x 'Yes'
        (034) STR      is_rear_window_defogger                2 distinct values,       0 missing: 3253x 'No', 1748x 'Yes'
        (035) STR      is_brake_assist                        2 distinct values,       0 missing: 2148x 'No', 2853x 'Yes'
        (036) STR      is_power_door_locks                    2 distinct values,       0 missing: 1276x 'No', 3725x 'Yes'
        (037) STR      is_central_locking                     2 distinct values,       0 missing: 1276x 'No', 3725x 'Yes'
        (038) STR      is_power_steering                      2 distinct values,       0 missing: 109x 'No', 4892x 'Yes'
        (039) STR      is_driver_seat_height_adjustable       2 distinct values,       0 missing: 1975x 'No', 3026x 'Yes'
        (040) STR      is_day_night_rear_view_mirror          2 distinct values,       0 missing: 3021x 'No', 1980x 'Yes'
        (041) STR      is_ecw                                 2 distinct values,       0 missing: 1276x 'No', 3725x 'Yes'
        (042) STR      is_speed_alert                         2 distinct values,       0 missing: 31x 'No', 4970x 'Yes'
        (043) INT      ncap_rating                            5 distinct values,       0 missing: 1488x '0', 1951x '2', 1223x '3', 173x '4', 166x '5'
        (044) INT    * is_claim                               2 distinct values,       0 missing: 4675x '0', 326x '1'

ZeroR:
        Prediction: 0
        Accuracy: 4_675 / 5_001 = 93.48%
        Precision: 93.48% or N/A
        Recall: 100% or 0%

Attribute distributions by class:
        Column 1 (policy_id):
                Class 0: mode 'ID42123' (0.04%)
                Class 1: mode 'ID28628' (0.31%)
        Column 2 (policy_date):
                Class 0: mode '2023-05-17' (0.32%)
                Class 1: mode '2022-07-01' (1.23%)
        Column 3 (age_of_car):
                Class 0: mode '0.01' (10.57%), median 0.060, avg. 0.070, min. 0.000, max. 0.390
                Class 1: mode '0' (16.87%), median 0.050, avg. 0.064, min. 0.000, max. 0.250
        Column 4 (age_of_policyholder):
                Class 0: mode '0.394230769230769' (3.21%), median 0.452, avg. 0.470, min. 0.288, max. 0.990
                Class 1: mode '0.451923076923077' (5.21%), median 0.471, avg. 0.486, min. 0.288, max. 0.856
        Column 5 (area_cluster):
                Class 0: mode 'C8' (37.80%)
                Class 1: mode 'C8' (37.12%)
        Column 6 (population_density):
                Class 0: mode '8794' (34.72%)
                Class 1: mode '8794' (34.97%)
        Column 7 (make):
                Class 0: mode '1' (64.56%), median 1.000, avg. 1.768, min. 1.000, max. 5.000
                Class 1: mode '1' (65.34%), median 1.000, avg. 1.782, min. 1.000, max. 5.000
        Column 8 (segment):
                Class 0: mode 'B2' (32.26%)
                Class 1: mode 'B2' (35.89%)
        Column 9 (model):
                Class 0: mode 'M6' (25.52%)
                Class 1: mode 'M6' (26.07%)
        Column 10 (fuel_type):
                Class 0: mode 'Petrol' (36.71%)
                Class 1: mode 'Petrol' (37.42%)
        Column 11 (max_torque):
                Class 0: mode '113Nm@4400rpm' (31.87%)
                Class 1: mode '113Nm@4400rpm' (33.44%)
        Column 12 (max_power):
                Class 0: mode '88.50bhp@6000rpm' (31.87%)
                Class 1: mode '88.50bhp@6000rpm' (33.44%)
        Column 13 (engine_type):
                Class 0: mode 'K Series Dual jet' (25.52%)
                Class 1: mode 'K Series Dual jet' (26.07%)
        Column 14 (airbags):
                Class 0: mode '2' (68.73%)
                Class 1: mode '2' (70.86%)
        Column 15 (is_esc):
                Class 0: mode 'No' (68.32%)
                Class 1: mode 'No' (70.55%)
        Column 16 (is_adjustable_steering):
                Class 0: mode 'Yes' (62.48%)
                Class 1: mode 'Yes' (64.11%)
        Column 17 (is_tpms):
                Class 0: mode 'No' (75.36%)
                Class 1: mode 'No' (78.22%)
        Column 18 (is_parking_sensors):
                Class 0: mode 'Yes' (95.81%)
                Class 1: mode 'Yes' (96.32%)
        Column 19 (is_parking_camera):
                Class 0: mode 'No' (60.66%)
                Class 1: mode 'No' (63.50%)
        Column 20 (rear_brakes_type):
                Class 0: mode 'Drum' (75.36%)
                Class 1: mode 'Drum' (78.22%)
        Column 21 (displacement):
                Class 0: mode '1197' (31.87%), median 1_197.000, avg. 1_171.684, min. 796.000, max. 1_498.000
                Class 1: mode '1197' (33.44%), median 1_197.000, avg. 1_175.187, min. 796.000, max. 1_498.000
        Column 22 (cylinder):
                Class 0: mode '4' (64.62%), median 4.000, avg. 3.645, min. -4.000, max. 4.000
                Class 1: mode '4' (66.56%), median 4.000, avg. 3.666, min. 3.000, max. 4.000
        Column 23 (transmission_type):
                Class 0: mode 'Manual' (64.81%)
                Class 1: mode 'Manual' (67.18%)
        Column 24 (gear_box):
                Class 0: mode '5' (74.72%), median 5.000, avg. 5.253, min. 5.000, max. 6.000
                Class 1: mode '5' (77.91%), median 5.000, avg. 5.221, min. 5.000, max. 6.000
        Column 25 (steering_type):
                Class 0: mode 'Power' (55.81%)
                Class 1: mode 'Power' (51.53%)
        Column 26 (turning_radius):
                Class 0: mode '4.8' (27.64%), median 4.800, avg. 4.859, min. 4.500, max. 5.200
                Class 1: mode '4.8' (29.14%), median 4.800, avg. 4.852, min. 4.500, max. 5.200
        Column 27 (length):
                Class 0: mode '3845' (25.52%), median 3_845.000, avg. 3_860.759, min. 3_445.000, max. 4_300.000
                Class 1: mode '3845' (26.07%), median 3_845.000, avg. 3_855.169, min. 3_445.000, max. 4_300.000
        Column 28 (width):
                Class 0: mode '1735' (27.64%), median 1_735.000, avg. 1_680.798, min. 1_475.000, max. 20_137.000
                Class 1: mode '1735' (29.14%), median 1_735.000, avg. 1_676.929, min. 1_475.000, max. 1_811.000
        Column 29 (height):
                Class 0: mode '1530' (25.52%), median 1_530.000, avg. 1_555.876, min. 1_475.000, max. 1_825.000
                Class 1: mode '1530' (26.07%), median 1_530.000, avg. 1_551.828, min. 1_475.000, max. 1_825.000
        Column 30 (gross_weight):
                Class 0: mode '1335' (27.64%), median 1_335.000, avg. 1_390.759, min. 1_051.000, max. 1_720.000
                Class 1: mode '1335' (29.14%), median 1_335.000, avg. 1_385.049, min. 1_051.000, max. 1_720.000
        Column 31 (is_front_fog_lights):
                Class 0: mode 'Yes' (59.98%)
                Class 1: mode 'Yes' (58.59%)
        Column 32 (is_rear_window_wiper):
                Class 0: mode 'No' (71.12%)
                Class 1: mode 'No' (73.93%)
        Column 33 (is_rear_window_washer):
                Class 0: mode 'No' (71.12%)
                Class 1: mode 'No' (73.93%)
        Column 34 (is_rear_window_defogger):
                Class 0: mode 'No' (64.90%)
                Class 1: mode 'No' (67.18%)
        Column 35 (is_brake_assist):
                Class 0: mode 'Yes' (57.16%)
                Class 1: mode 'Yes' (55.52%)
        Column 36 (is_power_door_locks):
                Class 0: mode 'Yes' (74.50%)
                Class 1: mode 'Yes' (74.23%)
        Column 37 (is_central_locking):
                Class 0: mode 'Yes' (74.50%)
                Class 1: mode 'Yes' (74.23%)
        Column 38 (is_power_steering):
                Class 0: mode 'Yes' (97.84%)
                Class 1: mode 'Yes' (97.55%)
        Column 39 (is_driver_seat_height_adjustable):
                Class 0: mode 'Yes' (60.62%)
                Class 1: mode 'Yes' (58.90%)
        Column 40 (is_day_night_rear_view_mirror):
                Class 0: mode 'No' (60.47%)
                Class 1: mode 'No' (59.51%)
        Column 41 (is_ecw):
                Class 0: mode 'Yes' (74.50%)
                Class 1: mode 'Yes' (74.23%)
        Column 42 (is_speed_alert):
                Class 0: mode 'Yes' (99.36%)
                Class 1: mode 'Yes' (99.69%)
        Column 43 (ncap_rating):
                Class 0: mode '2' (39.02%), median 2.000, avg. 1.815, min. 0.000, max. 5.000
                Class 1: mode '2' (38.96%), median 2.000, avg. 1.859, min. 0.000, max. 5.000

Identical/Equivalent/Redundant columns:
        Column 7 (make) is redundant as there's already column 9 (model):
                1 ('1', 'M1')
                2 ('1', 'M10')
                3 ('1', 'M2')
                4 ('1', 'M6')
                5 ('1', 'M7')
                6 ('1', 'M8')
                7 ('2', 'M3')
                8 ('3', 'M4')
                9 ('4', 'M11')
                10 ('4', 'M5')
                11 ('5', 'M9')
        Because there's already column 7 (make), column 17 (is_tpms) is redundant:
                1 ('1', 'No')
                2 ('2', 'No')
                3 ('3', 'Yes')
                4 ('4', 'No')
                5 ('5', 'No')
        Because there's already column 7 (make), column 18 (is_parking_sensors) is redundant:
                1 ('1', 'Yes')
                2 ('2', 'No')
                3 ('3', 'Yes')
                4 ('4', 'Yes')
                5 ('5', 'Yes')
        Because there's already column 7 (make), column 20 (rear_brakes_type) is redundant:
                1 ('1', 'Drum')
                2 ('2', 'Drum')
                3 ('3', 'Disc')
                4 ('4', 'Drum')
                5 ('5', 'Drum')
        Column 8 (segment) is redundant as there's already column 9 (model):
                1 ('A', 'M1')
                2 ('A', 'M3')
                3 ('B1', 'M8')
                4 ('B2', 'M5')
                5 ('B2', 'M6')
                6 ('B2', 'M7')
                7 ('C1', 'M11')
                8 ('C1', 'M2')
                9 ('C1', 'M9')
                10 ('C2', 'M4')
                11 ('Utility', 'M10')
        Because there's already column 8 (segment), column 38 (is_power_steering) is redundant:
                1 ('A', 'Yes')
                2 ('B1', 'Yes')
                3 ('B2', 'Yes')
                4 ('C1', 'Yes')
                5 ('C2', 'Yes')
                6 ('Utility', 'No')
        Because there's already column 9 (model), column 10 (fuel_type) is redundant:
                1 ('M1', 'CNG')
                2 ('M10', 'CNG')
                3 ('M11', 'Petrol')
                4 ('M2', 'Petrol')
                5 ('M3', 'Petrol')
                6 ('M4', 'Diesel')
                7 ('M5', 'Diesel')
                8 ('M6', 'Petrol')
                9 ('M7', 'Petrol')
                10 ('M8', 'CNG')
                11 ('M9', 'Diesel')
        Because there's already column 9 (model), column 11 (max_torque) is redundant:
                1 ('M1', '60Nm@3500rpm')
                2 ('M10', '85Nm@3000rpm')
                3 ('M11', '170Nm@4000rpm')
                4 ('M2', '113Nm@4400rpm')
                5 ('M3', '91Nm@4250rpm')
                6 ('M4', '250Nm@2750rpm')
                7 ('M5', '200Nm@3000rpm')
                8 ('M6', '113Nm@4400rpm')
                9 ('M7', '113Nm@4400rpm')
                10 ('M8', '82.1Nm@3400rpm')
                11 ('M9', '200Nm@1750rpm')
        Because there's already column 9 (model), column 12 (max_power) is redundant:
                1 ('M1', '40.36bhp@6000rpm')
                2 ('M10', '61.68bhp@6000rpm')
                3 ('M11', '118.36bhp@5500rpm')
                4 ('M2', '88.50bhp@6000rpm')
                5 ('M3', '67.06bhp@5500rpm')
                6 ('M4', '113.45bhp@4000rpm')
                7 ('M5', '88.77bhp@4000rpm')
                8 ('M6', '88.50bhp@6000rpm')
                9 ('M7', '88.50bhp@6000rpm')
                10 ('M8', '55.92bhp@5300rpm')
                11 ('M9', '97.89bhp@3600rpm')
        Columns 9 (model) and 13 (engine_type) are equivalent:
                1 ('M1', 'F8D Petrol Engine')
                2 ('M10', 'G12B')
                3 ('M11', '1.5 Turbocharged Revotron')
                4 ('M2', '1.2 L K12N Dualjet')
                5 ('M3', '1.0 SCe')
                6 ('M4', '1.5 L U2 CRDi')
                7 ('M5', '1.5 Turbocharged Revotorq')
                8 ('M6', 'K Series Dual jet')
                9 ('M7', '1.2 L K Series Engine')
                10 ('M8', 'K10C')
                11 ('M9', 'i-DTEC')
        Because there's already column 9 (model), column 16 (is_adjustable_steering) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'No')
                4 ('M2', 'Yes')
                5 ('M3', 'No')
                6 ('M4', 'Yes')
                7 ('M5', 'Yes')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 21 (displacement) is redundant:
                1 ('M1', '796')
                2 ('M10', '1196')
                3 ('M11', '1199')
                4 ('M2', '1197')
                5 ('M3', '999')
                6 ('M4', '1493')
                7 ('M5', '1497')
                8 ('M6', '1197')
                9 ('M7', '1197')
                10 ('M8', '998')
                11 ('M9', '1498')
        Because there's already column 9 (model), column 23 (transmission_type) is redundant:
                1 ('M1', 'Manual')
                2 ('M10', 'Manual')
                3 ('M11', 'Manual')
                4 ('M2', 'Automatic')
                5 ('M3', 'Automatic')
                6 ('M4', 'Automatic')
                7 ('M5', 'Manual')
                8 ('M6', 'Manual')
                9 ('M7', 'Automatic')
                10 ('M8', 'Manual')
                11 ('M9', 'Manual')
        Because there's already column 9 (model), column 24 (gear_box) is redundant:
                1 ('M1', '5')
                2 ('M10', '5')
                3 ('M11', '6')
                4 ('M2', '5')
                5 ('M3', '5')
                6 ('M4', '6')
                7 ('M5', '5')
                8 ('M6', '5')
                9 ('M7', '5')
                10 ('M8', '5')
                11 ('M9', '5')
        Because there's already column 9 (model), column 25 (steering_type) is redundant:
                1 ('M1', 'Power')
                2 ('M10', 'Manual')
                3 ('M11', 'Power')
                4 ('M2', 'Electric')
                5 ('M3', 'Electric')
                6 ('M4', 'Power')
                7 ('M5', 'Electric')
                8 ('M6', 'Electric')
                9 ('M7', 'Electric')
                10 ('M8', 'Power')
                11 ('M9', 'Electric')
        Because there's already column 9 (model), column 26 (turning_radius) is redundant:
                1 ('M1', '4.6')
                2 ('M10', '4.5')
                3 ('M11', '5.1')
                4 ('M2', '4.8')
                5 ('M3', '5')
                6 ('M4', '5.2')
                7 ('M5', '5')
                8 ('M6', '4.8')
                9 ('M7', '4.85')
                10 ('M8', '4.7')
                11 ('M9', '4.9')
        Because there's already column 9 (model), column 27 (length) is redundant:
                1 ('M1', '3445')
                2 ('M10', '3675')
                3 ('M11', '3993')
                4 ('M2', '3995')
                5 ('M3', '3731')
                6 ('M4', '4300')
                7 ('M5', '3990')
                8 ('M6', '3845')
                9 ('M7', '3990')
                10 ('M8', '3655')
                11 ('M9', '3995')
        Columns 9 (model) and 29 (height) are equivalent:
                1 ('M1', '1475')
                2 ('M10', '1825')
                3 ('M11', '1606')
                4 ('M2', '1515')
                5 ('M3', '1490')
                6 ('M4', '1635')
                7 ('M5', '1523')
                8 ('M6', '1530')
                9 ('M7', '1500')
                10 ('M8', '1675')
                11 ('M9', '1501')
        Because there's already column 9 (model), column 30 (gross_weight) is redundant:
                1 ('M1', '1185')
                2 ('M10', '1510')
                3 ('M11', '1660')
                4 ('M2', '1335')
                5 ('M3', '1155')
                6 ('M4', '1720')
                7 ('M5', '1490')
                8 ('M6', '1335')
                9 ('M7', '1410')
                10 ('M8', '1340')
                11 ('M9', '1051')
        Because there's already column 9 (model), column 31 (is_front_fog_lights) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'No')
                4 ('M2', 'Yes')
                5 ('M3', 'No')
                6 ('M4', 'Yes')
                7 ('M5', 'No')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 32 (is_rear_window_wiper) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'No')
                4 ('M2', 'No')
                5 ('M3', 'No')
                6 ('M4', 'Yes')
                7 ('M5', 'No')
                8 ('M6', 'No')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'No')
        Because there's already column 9 (model), column 33 (is_rear_window_washer) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'No')
                4 ('M2', 'No')
                5 ('M3', 'No')
                6 ('M4', 'Yes')
                7 ('M5', 'No')
                8 ('M6', 'No')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'No')
        Because there's already column 9 (model), column 34 (is_rear_window_defogger) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'Yes')
                4 ('M2', 'Yes')
                5 ('M3', 'No')
                6 ('M4', 'Yes')
                7 ('M5', 'No')
                8 ('M6', 'No')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 35 (is_brake_assist) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'Yes')
                4 ('M2', 'Yes')
                5 ('M3', 'No')
                6 ('M4', 'Yes')
                7 ('M5', 'No')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'No')
        Because there's already column 9 (model), column 36 (is_power_door_locks) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'Yes')
                4 ('M2', 'Yes')
                5 ('M3', 'Yes')
                6 ('M4', 'Yes')
                7 ('M5', 'Yes')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'Yes')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 37 (is_central_locking) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'Yes')
                4 ('M2', 'Yes')
                5 ('M3', 'Yes')
                6 ('M4', 'Yes')
                7 ('M5', 'Yes')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'Yes')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 39 (is_driver_seat_height_adjustable) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'Yes')
                4 ('M2', 'Yes')
                5 ('M3', 'No')
                6 ('M4', 'Yes')
                7 ('M5', 'No')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 40 (is_day_night_rear_view_mirror) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'No')
                4 ('M2', 'Yes')
                5 ('M3', 'Yes')
                6 ('M4', 'No')
                7 ('M5', 'No')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'No')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 41 (is_ecw) is redundant:
                1 ('M1', 'No')
                2 ('M10', 'No')
                3 ('M11', 'Yes')
                4 ('M2', 'Yes')
                5 ('M3', 'Yes')
                6 ('M4', 'Yes')
                7 ('M5', 'Yes')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'Yes')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 42 (is_speed_alert) is redundant:
                1 ('M1', 'Yes')
                2 ('M10', 'Yes')
                3 ('M11', 'No')
                4 ('M2', 'Yes')
                5 ('M3', 'Yes')
                6 ('M4', 'Yes')
                7 ('M5', 'Yes')
                8 ('M6', 'Yes')
                9 ('M7', 'Yes')
                10 ('M8', 'Yes')
                11 ('M9', 'Yes')
        Because there's already column 9 (model), column 43 (ncap_rating) is redundant:
                1 ('M1', '0')
                2 ('M10', '0')
                3 ('M11', '5')
                4 ('M2', '2')
                5 ('M3', '2')
                6 ('M4', '3')
                7 ('M5', '5')
                8 ('M6', '2')
                9 ('M7', '0')
                10 ('M8', '2')
                11 ('M9', '4')
        Columns 11 (max_torque) and 12 (max_power) are equivalent:
                1 ('113Nm@4400rpm', '88.50bhp@6000rpm')
                2 ('170Nm@4000rpm', '118.36bhp@5500rpm')
                3 ('200Nm@1750rpm', '97.89bhp@3600rpm')
                4 ('200Nm@3000rpm', '88.77bhp@4000rpm')
                5 ('250Nm@2750rpm', '113.45bhp@4000rpm')
                6 ('60Nm@3500rpm', '40.36bhp@6000rpm')
                7 ('82.1Nm@3400rpm', '55.92bhp@5300rpm')
                8 ('85Nm@3000rpm', '61.68bhp@6000rpm')
                9 ('91Nm@4250rpm', '67.06bhp@5500rpm')
        Columns 11 (max_torque) and 21 (displacement) are equivalent:
                1 ('113Nm@4400rpm', '1197')
                2 ('170Nm@4000rpm', '1199')
                3 ('200Nm@1750rpm', '1498')
                4 ('200Nm@3000rpm', '1497')
                5 ('250Nm@2750rpm', '1493')
                6 ('60Nm@3500rpm', '796')
                7 ('82.1Nm@3400rpm', '998')
                8 ('85Nm@3000rpm', '1196')
                9 ('91Nm@4250rpm', '999')
        Columns 12 (max_power) and 21 (displacement) are equivalent:
                1 ('113.45bhp@4000rpm', '1493')
                2 ('118.36bhp@5500rpm', '1199')
                3 ('40.36bhp@6000rpm', '796')
                4 ('55.92bhp@5300rpm', '998')
                5 ('61.68bhp@6000rpm', '1196')
                6 ('67.06bhp@5500rpm', '999')
                7 ('88.50bhp@6000rpm', '1197')
                8 ('88.77bhp@4000rpm', '1497')
                9 ('97.89bhp@3600rpm', '1498')
        Columns 13 (engine_type) and 29 (height) are equivalent:
                1 ('1.0 SCe', '1490')
                2 ('1.2 L K Series Engine', '1500')
                3 ('1.2 L K12N Dualjet', '1515')
                4 ('1.5 L U2 CRDi', '1635')
                5 ('1.5 Turbocharged Revotorq', '1523')
                6 ('1.5 Turbocharged Revotron', '1606')
                7 ('F8D Petrol Engine', '1475')
                8 ('G12B', '1825')
                9 ('K Series Dual jet', '1530')
                10 ('K10C', '1675')
                11 ('i-DTEC', '1501')
        Columns 17 (is_tpms) and 20 (rear_brakes_type) are equivalent:
                1 ('No', 'Drum')
                2 ('Yes', 'Disc')
        Columns 32 (is_rear_window_wiper) and 33 (is_rear_window_washer) are always *exactly* identical:
                1 ('No', 'No')
                2 ('Yes', 'Yes')
        Columns 36 (is_power_door_locks) and 37 (is_central_locking) are always *exactly* identical:
                1 ('No', 'No')
                2 ('Yes', 'Yes')
        Columns 36 (is_power_door_locks) and 41 (is_ecw) are always *exactly* identical:
                1 ('No', 'No')
                2 ('Yes', 'Yes')
        Columns 37 (is_central_locking) and 41 (is_ecw) are always *exactly* identical:
                1 ('No', 'No')
                2 ('Yes', 'Yes')

```
