# csv_stats
A Python script printing various statistics about a given CSV file. Useful as a starting point for data analysis tasks.

## Example

```
$ python3.12 csv_stats.py input.csv --header

No. of rows: 5001
No. of columns: 44
Header?: True

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
        (001) STR   policy_id                          5_000 distinct values,       0 missing
        (002) STR   policy_date                          727 distinct values,       0 missing
        (003) FLOAT age_of_car                            35 distinct values,       0 missing: min. 0.00, max. 0.39, 0 neg. values, 462 zero values, 4_539 pos. values
        (004) FLOAT age_of_policyholder                   66 distinct values,       0 missing: min. 0.29, max. 0.99, 0 neg. values, 0 zero values, 5_001 pos. values
        (005) STR   area_cluster                          40 distinct values,       0 missing
        (006) STR   population_density                    22 distinct values,     400 missing
        (007) INT   make                                   5 distinct values,       0 missing: 3231x '1', 208x '2', 1223x '3', 166x '4', 173x '5'
        (008) STR   segment                                6 distinct values,       0 missing
        (009) STR   model                                 11 distinct values,       0 missing
        (010) STR   fuel_type                              3 distinct values,       0 missing: 1632x 'CNG', 1531x 'Diesel', 1838x 'Petrol'
        (011) STR   max_torque                             9 distinct values,       0 missing
        (012) STR   max_power                              9 distinct values,       0 missing
        (013) STR   engine_type                           11 distinct values,       0 missing
        (014) STR   airbags                                4 distinct values,      17 missing: 109x '1', 3444x '2', 1431x '6', 17x 'NA'
        (015) STR   is_esc                                 3 distinct values,       5 missing: 5x 'NA', 3424x 'No', 1572x 'Yes'
        (016) STR   is_adjustable_steering                 2 distinct values,       0 missing: 1871x 'No', 3130x 'Yes'
        (017) STR   is_tpms                                2 distinct values,       0 missing: 3778x 'No', 1223x 'Yes'
        (018) STR   is_parking_sensors                     2 distinct values,       0 missing: 208x 'No', 4793x 'Yes'
        (019) STR   is_parking_camera                      4 distinct values,       0 missing: 1x '2', 1x '3', 3043x 'No', 1956x 'Yes'
        (020) STR   rear_brakes_type                       2 distinct values,       0 missing: 1223x 'Disc', 3778x 'Drum'
        (021) INT   displacement                           9 distinct values,       0 missing: min. 796.00, max. 1_498.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (022) INT   cylinder                               3 distinct values,       0 missing: 1x '-4', 1762x '3', 3238x '4'
        (023) STR   transmission_type                      2 distinct values,       0 missing: 1752x 'Automatic', 3249x 'Manual'
        (024) INT   gear_box                               2 distinct values,       0 missing: 3747x '5', 1254x '6'
        (025) STR   steering_type                          3 distinct values,       0 missing: 2115x 'Electric', 109x 'Manual', 2777x 'Power'
        (026) FLOAT turning_radius                         9 distinct values,       0 missing: min. 4.50, max. 5.20, 0 neg. values, 0 zero values, 5_001 pos. values
        (027) INT   length                                 9 distinct values,       0 missing: min. 3_445.00, max. 4_300.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (028) INT   width                                 11 distinct values,       0 missing: min. 1_475.00, max. 20_137.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (029) INT   height                                11 distinct values,       0 missing: min. 1_475.00, max. 1_825.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (030) INT   gross_weight                          10 distinct values,       0 missing: min. 1_051.00, max. 1_720.00, 0 neg. values, 0 zero values, 5_001 pos. values
        (031) STR   is_front_fog_lights                    2 distinct values,       0 missing: 2006x 'No', 2995x 'Yes'
        (032) STR   is_rear_window_wiper                   2 distinct values,       0 missing: 3566x 'No', 1435x 'Yes'
        (033) STR   is_rear_window_washer                  2 distinct values,       0 missing: 3566x 'No', 1435x 'Yes'
        (034) STR   is_rear_window_defogger                2 distinct values,       0 missing: 3253x 'No', 1748x 'Yes'
        (035) STR   is_brake_assist                        2 distinct values,       0 missing: 2148x 'No', 2853x 'Yes'
        (036) STR   is_power_door_locks                    2 distinct values,       0 missing: 1276x 'No', 3725x 'Yes'
        (037) STR   is_central_locking                     2 distinct values,       0 missing: 1276x 'No', 3725x 'Yes'
        (038) STR   is_power_steering                      2 distinct values,       0 missing: 109x 'No', 4892x 'Yes'
        (039) STR   is_driver_seat_height_adjustable       2 distinct values,       0 missing: 1975x 'No', 3026x 'Yes'
        (040) STR   is_day_night_rear_view_mirror          2 distinct values,       0 missing: 3021x 'No', 1980x 'Yes'
        (041) STR   is_ecw                                 2 distinct values,       0 missing: 1276x 'No', 3725x 'Yes'
        (042) STR   is_speed_alert                         2 distinct values,       0 missing: 31x 'No', 4970x 'Yes'
        (043) INT   ncap_rating                            5 distinct values,       0 missing: 1488x '0', 1951x '2', 1223x '3', 173x '4', 166x '5'
        (044) INT   is_claim                               2 distinct values,       0 missing: 4675x '0', 326x '1'

Identical/Equivalent columns:
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
