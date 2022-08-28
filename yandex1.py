# Дан файл со сделками с недвижимостью за год, выделить в файл ту недвижимость, которая продавалась больше 1 раза.
import pandas

records = pandas.read_csv('pp-complete.csv', delimiter=',', names=['transaction-id', 'price', 'date', 'postcode',
                                                                   'property-type', 'old-new', 'duration', 'paon',
                                                                   'saon', 'street', 'locality', 'city', 'district',
                                                                   'county', 'ppd-category', 'record-status'])

all_addr = records.drop(['transaction-id', 'price', 'date', 'property-type', 'old-new', 'duration',
                         'ppd-category', 'record-status'], axis=1)

duple_addr = all_addr[all_addr.groupby(['postcode', 'paon', 'saon', 'street', 'locality', 'city',
                                        'district', 'county'])['postcode'].transform('size') > 1]

addr_list = duple_addr.drop_duplicates(subset=['postcode', 'paon', 'saon', 'street', 'locality', 'city',
                                               'district', 'county'], keep='first').reset_index(drop=True)

print(addr_list.to_csv('address_list.csv'))
