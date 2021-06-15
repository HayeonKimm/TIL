```python
!pip install pymysql
```

    Collecting pymysql
      Downloading PyMySQL-1.0.2-py3-none-any.whl (43 kB)
    Installing collected packages: pymysql
    Successfully installed pymysql-1.0.2
    


```python
import pymysql
```


```python
conn = pymysql.connect(host='localhost', port=3306,user='root',password='a1234',db='classicmodels')
cur=conn.cursor()
cur

sql='SELECT * FROM customers'#모든 데이터를 가져옴
cur.execute(sql)

# result = cur.fetchone()        #하나만 가져와서 출력
# print(result)

result = cur.fetchall()
# print(result)

for row in result:
#     print(row)
    cur=conn.cursor()
    print(row[0],row[1])

# conn.commit() #insert,update,delete 등 변경사항 적용 시켜주는 코드 
conn.close() #db접속 종료시켜주는 코드
```

    103 Atelier graphique
    112 Signal Gift Stores
    114 Australian Collectors, Co.
    119 La Rochelle Gifts
    121 Baane Mini Imports
    124 Mini Gifts Distributors Ltd.
    125 Havel & Zbyszek Co
    128 Blauer See Auto, Co.
    129 Mini Wheels Co.
    131 Land of Toys Inc.
    141 Euro+ Shopping Channel
    144 Volvo Model Replicas, Co
    145 Danish Wholesale Imports
    146 Saveley & Henriot, Co.
    148 Dragon Souveniers, Ltd.
    151 Muscle Machine Inc
    157 Diecast Classics Inc.
    161 Technics Stores Inc.
    166 Handji Gifts& Co
    167 Herkku Gifts
    168 American Souvenirs Inc
    169 Porto Imports Co.
    171 Daedalus Designs Imports
    172 La Corne D'abondance, Co.
    173 Cambridge Collectables Co.
    175 Gift Depot Inc.
    177 Osaka Souveniers Co.
    181 Vitachrome Inc.
    186 Toys of Finland, Co.
    187 AV Stores, Co.
    189 Clover Collections, Co.
    198 Auto-Moto Classics Inc.
    201 UK Collectables, Ltd.
    202 Canadian Gift Exchange Network
    204 Online Mini Collectables
    205 Toys4GrownUps.com
    206 Asian Shopping Network, Co
    209 Mini Caravy
    211 King Kong Collectables, Co.
    216 Enaco Distributors
    219 Boards & Toys Co.
    223 Natürlich Autos
    227 Heintze Collectables
    233 Québec Home Shopping Network
    237 ANG Resellers
    239 Collectable Mini Designs Co.
    240 giftsbymail.co.uk
    242 Alpha Cognac
    247 Messner Shopping Network
    249 Amica Models & Co.
    250 Lyon Souveniers
    256 Auto Associés & Cie.
    259 Toms Spezialitäten, Ltd
    260 Royal Canadian Collectables, Ltd.
    273 Franken Gifts, Co
    276 Anna's Decorations, Ltd
    278 Rovelli Gifts
    282 Souveniers And Things Co.
    286 Marta's Replicas Co.
    293 BG&E Collectables
    298 Vida Sport, Ltd
    299 Norway Gifts By Mail, Co.
    303 Schuyler Imports
    307 Der Hund Imports
    311 Oulu Toy Supplies, Inc.
    314 Petit Auto
    319 Mini Classics
    320 Mini Creations Ltd.
    321 Corporate Gift Ideas Co.
    323 Down Under Souveniers, Inc
    324 Stylish Desk Decors, Co.
    328 Tekni Collectables Inc.
    333 Australian Gift Network, Co
    334 Suominen Souveniers
    335 Cramer Spezialitäten, Ltd
    339 Classic Gift Ideas, Inc
    344 CAF Imports
    347 Men 'R' US Retailers, Ltd.
    348 Asian Treasures, Inc.
    350 Marseille Mini Autos
    353 Reims Collectables
    356 SAR Distributors, Co
    357 GiftsForHim.com
    361 Kommission Auto
    362 Gifts4AllAges.com
    363 Online Diecast Creations Co.
    369 Lisboa Souveniers, Inc
    376 Precious Collectables
    379 Collectables For Less Inc.
    381 Royale Belge
    382 Salzburg Collectables
    385 Cruz & Sons Co.
    386 L'ordine Souveniers
    398 Tokyo Collectables, Ltd
    406 Auto Canal+ Petit
    409 Stuttgart Collectable Exchange
    412 Extreme Desk Decorations, Ltd
    415 Bavarian Collectables Imports, Co.
    424 Classic Legends Inc.
    443 Feuer Online Stores, Inc
    447 Gift Ideas Corp.
    448 Scandinavian Gift Ideas
    450 The Sharp Gifts Warehouse
    452 Mini Auto Werke
    455 Super Scale Inc.
    456 Microscale Inc.
    458 Corrida Auto Replicas, Ltd
    459 Warburg Exchange
    462 FunGiftIdeas.com
    465 Anton Designs, Ltd.
    471 Australian Collectables, Ltd
    473 Frau da Collezione
    475 West Coast Collectables Co.
    477 Mit Vergnügen & Co.
    480 Kremlin Collectables, Co.
    481 Raanan Stores, Inc
    484 Iberia Gift Imports, Corp.
    486 Motor Mint Distributors Inc.
    487 Signal Collectibles Ltd.
    489 Double Decker Gift Stores, Ltd
    495 Diecast Collectables
    496 Kelly's Gift Shop
    


```python
conn = pymysql.connect(host='localhost', port=3306,user='root',password='a1234',db='classicmodels')
cur=conn.cursor()

num = 119

# list or tuple :%s

sql='SELECT * FROM customers WHERE customerNumber=%s'
cur.execute(sql,(num))
print(sql)

result = cur.fetchone();
# print(result)
print(result[0],result[1],result[2])

conn.close()
```

    SELECT * FROM customers WHERE customerNumber=%s
    119 La Rochelle Gifts Labrune
    


```python
conn = pymysql.connect(host='localhost', port=3306,user='root',password='a1234',db='classicmodels')
cur=conn.cursor()

sql = 'SELECT*FROM customers WHERE customerName=%s' # 이건 컬럼 특성상 fetchall로 설정해야함, 
cur.execute(sql,('La Rochelle Gifts'))

print(sql) #이건 그냥 확인용
      
result = cur.fetchall()

for row in result:
    print(row)
    
conn.close()

```

    SELECT*FROM customers WHERE customerName=%s
    (119, 'La Rochelle Gifts', 'Labrune', 'Janine ', '40.67.8555', '67, rue des Cinquante Otages', None, 'Nantes', None, '44000', 'France', 1370, Decimal('118200.00'))
    


```python
conn = pymysql.connect(host='localhost', port=3306,user='root',password='a1234',db='classicmodels')
cur=conn.cursor()

search = 'A'
sql = 'SELECT*FROM customers WHERE customerName LIKE binary"%%%s%%"' %(search)
cur.execute(sql)

print(sql) #이건 그냥 확인용
      
result = cur.fetchall()

for row in result:
    print(row)
    
conn.close()
```

    SELECT*FROM customers WHERE customerName LIKE binary"%A%"
    (103, 'Atelier graphique', 'Schmitt', 'Carine ', '40.32.2555', '54, rue Royale', None, 'Nantes', None, '44000', 'France', 1370, Decimal('21000.00'))
    (114, 'Australian Collectors, Co.', 'Ferguson', 'Peter', '03 9520 4555', '636 St Kilda Road', 'Level 3', 'Melbourne', 'Victoria', '3004', 'Australia', 1611, Decimal('117300.00'))
    (128, 'Blauer See Auto, Co.', 'Keitel', 'Roland', '+49 69 66 90 2555', 'Lyonerstr. 34', None, 'Frankfurt', None, '60528', 'Germany', 1504, Decimal('59700.00'))
    (168, 'American Souvenirs Inc', 'Franco', 'Keith', '2035557845', '149 Spinnaker Dr.', 'Suite 101', 'New Haven', 'CT', '97823', 'USA', 1286, Decimal('0.00'))
    (187, 'AV Stores, Co.', 'Ashworth', 'Rachel', '(171) 555-1555', 'Fauntleroy Circus', None, 'Manchester', None, 'EC2 5NT', 'UK', 1501, Decimal('136800.00'))
    (198, 'Auto-Moto Classics Inc.', 'Taylor', 'Leslie', '6175558428', '16780 Pompton St.', None, 'Brickhaven', 'MA', '58339', 'USA', 1216, Decimal('23000.00'))
    (206, 'Asian Shopping Network, Co', 'Walker', 'Brydey', '+612 9411 1555', 'Suntec Tower Three', '8 Temasek', 'Singapore', None, '038988', 'Singapore', None, Decimal('0.00'))
    (223, 'Natürlich Autos', 'Kloss', 'Horst ', '0372-555188', 'Taucherstraße 10', None, 'Cunewalde', None, '01307', 'Germany', None, Decimal('0.00'))
    (237, 'ANG Resellers', 'Camino', 'Alejandra ', '(91) 745 6555', 'Gran Vía, 1', None, 'Madrid', None, '28001', 'Spain', None, Decimal('0.00'))
    (242, 'Alpha Cognac', 'Roulet', 'Annette ', '61.77.6555', '1 rue Alsace-Lorraine', None, 'Toulouse', None, '31000', 'France', 1370, Decimal('61100.00'))
    (249, 'Amica Models & Co.', 'Accorti', 'Paolo ', '011-4988555', 'Via Monte Bianco 34', None, 'Torino', None, '10100', 'Italy', 1401, Decimal('113000.00'))
    (256, 'Auto Associés & Cie.', 'Tonini', 'Daniel ', '30.59.8555', "67, avenue de l'Europe", None, 'Versailles', None, '78000', 'France', 1370, Decimal('77900.00'))
    (276, "Anna's Decorations, Ltd", "O'Hara", 'Anna', '02 9936 8555', '201 Miller Street', 'Level 15', 'North Sydney', 'NSW', '2060', 'Australia', 1611, Decimal('107800.00'))
    (282, 'Souveniers And Things Co.', 'Huxley', 'Adrian', '+61 2 9495 8555', 'Monitor Money Building', '815 Pacific Hwy', 'Chatswood', 'NSW', '2067', 'Australia', 1611, Decimal('93300.00'))
    (314, 'Petit Auto', 'Dewey', 'Catherine ', '(02) 5554 67', 'Rue Joseph-Bens 532', None, 'Bruxelles', None, 'B-1180', 'Belgium', 1401, Decimal('79900.00'))
    (333, 'Australian Gift Network, Co', 'Calaghan', 'Ben', '61-7-3844-6555', '31 Duncan St. West End', None, 'South Brisbane', 'Queensland', '4101', 'Australia', 1611, Decimal('51600.00'))
    (344, 'CAF Imports', 'Fernandez', 'Jesus', '+34 913 728 555', 'Merchants House', "27-30 Merchant's Quay", 'Madrid', None, '28023', 'Spain', 1702, Decimal('59600.00'))
    (348, 'Asian Treasures, Inc.', 'McKenna', 'Patricia ', '2967 555', '8 Johnstown Road', None, 'Cork', 'Co. Cork', None, 'Ireland', None, Decimal('0.00'))
    (350, 'Marseille Mini Autos', 'Lebihan', 'Laurence ', '91.24.4555', '12, rue des Bouchers', None, 'Marseille', None, '13008', 'France', 1337, Decimal('65000.00'))
    (356, 'SAR Distributors, Co', 'Kuger', 'Armand', '+27 21 550 3555', '1250 Pretorius Street', None, 'Hatfield', 'Pretoria', '0028', 'South Africa', None, Decimal('0.00'))
    (361, 'Kommission Auto', 'Josephs', 'Karin', '0251-555259', 'Luisenstr. 48', None, 'Münster', None, '44087', 'Germany', None, Decimal('0.00'))
    (362, 'Gifts4AllAges.com', 'Yoshido', 'Juri', '6175559555', '8616 Spinnaker Dr.', None, 'Boston', 'MA', '51003', 'USA', 1216, Decimal('41900.00'))
    (406, 'Auto Canal+ Petit', 'Perrier', 'Dominique', '(1) 47.55.6555', '25, rue Lauriston', None, 'Paris', None, '75016', 'France', 1337, Decimal('95000.00'))
    (452, 'Mini Auto Werke', 'Mendel', 'Roland ', '7675-3555', 'Kirchgasse 6', None, 'Graz', None, '8010', 'Austria', 1401, Decimal('45300.00'))
    (458, 'Corrida Auto Replicas, Ltd', 'Sommer', 'Martín ', '(91) 555 22 82', 'C/ Araquil, 67', None, 'Madrid', None, '28023', 'Spain', 1702, Decimal('104600.00'))
    (465, 'Anton Designs, Ltd.', 'Anton', 'Carmen', '+34 913 728555', 'c/ Gobelas, 19-1 Urb. La Florida', None, 'Madrid', None, '28023', 'Spain', None, Decimal('0.00'))
    (471, 'Australian Collectables, Ltd', 'Clenahan', 'Sean', '61-9-3844-6555', '7 Allen Street', None, 'Glen Waverly', 'Victoria', '3150', 'Australia', 1611, Decimal('60300.00'))
    


```python
conn = pymysql.connect(host='localhost', port=3306,user='root',password='a1234',db='classicmodels')
cur=conn.cursor()

search = 'A'
sql = 'SELECT*FROM customers WHERE customerName LIKE binary %s'
cur.execute(sql,"%%%s%%"%(search))


print(sql) #이건 그냥 확인용
      
result = cur.fetchall()

for row in result:
    print(row)
    
conn.close()
```

    SELECT*FROM customers WHERE customerName LIKE binary %s
    (103, 'Atelier graphique', 'Schmitt', 'Carine ', '40.32.2555', '54, rue Royale', None, 'Nantes', None, '44000', 'France', 1370, Decimal('21000.00'))
    (114, 'Australian Collectors, Co.', 'Ferguson', 'Peter', '03 9520 4555', '636 St Kilda Road', 'Level 3', 'Melbourne', 'Victoria', '3004', 'Australia', 1611, Decimal('117300.00'))
    (128, 'Blauer See Auto, Co.', 'Keitel', 'Roland', '+49 69 66 90 2555', 'Lyonerstr. 34', None, 'Frankfurt', None, '60528', 'Germany', 1504, Decimal('59700.00'))
    (168, 'American Souvenirs Inc', 'Franco', 'Keith', '2035557845', '149 Spinnaker Dr.', 'Suite 101', 'New Haven', 'CT', '97823', 'USA', 1286, Decimal('0.00'))
    (187, 'AV Stores, Co.', 'Ashworth', 'Rachel', '(171) 555-1555', 'Fauntleroy Circus', None, 'Manchester', None, 'EC2 5NT', 'UK', 1501, Decimal('136800.00'))
    (198, 'Auto-Moto Classics Inc.', 'Taylor', 'Leslie', '6175558428', '16780 Pompton St.', None, 'Brickhaven', 'MA', '58339', 'USA', 1216, Decimal('23000.00'))
    (206, 'Asian Shopping Network, Co', 'Walker', 'Brydey', '+612 9411 1555', 'Suntec Tower Three', '8 Temasek', 'Singapore', None, '038988', 'Singapore', None, Decimal('0.00'))
    (223, 'Natürlich Autos', 'Kloss', 'Horst ', '0372-555188', 'Taucherstraße 10', None, 'Cunewalde', None, '01307', 'Germany', None, Decimal('0.00'))
    (237, 'ANG Resellers', 'Camino', 'Alejandra ', '(91) 745 6555', 'Gran Vía, 1', None, 'Madrid', None, '28001', 'Spain', None, Decimal('0.00'))
    (242, 'Alpha Cognac', 'Roulet', 'Annette ', '61.77.6555', '1 rue Alsace-Lorraine', None, 'Toulouse', None, '31000', 'France', 1370, Decimal('61100.00'))
    (249, 'Amica Models & Co.', 'Accorti', 'Paolo ', '011-4988555', 'Via Monte Bianco 34', None, 'Torino', None, '10100', 'Italy', 1401, Decimal('113000.00'))
    (256, 'Auto Associés & Cie.', 'Tonini', 'Daniel ', '30.59.8555', "67, avenue de l'Europe", None, 'Versailles', None, '78000', 'France', 1370, Decimal('77900.00'))
    (276, "Anna's Decorations, Ltd", "O'Hara", 'Anna', '02 9936 8555', '201 Miller Street', 'Level 15', 'North Sydney', 'NSW', '2060', 'Australia', 1611, Decimal('107800.00'))
    (282, 'Souveniers And Things Co.', 'Huxley', 'Adrian', '+61 2 9495 8555', 'Monitor Money Building', '815 Pacific Hwy', 'Chatswood', 'NSW', '2067', 'Australia', 1611, Decimal('93300.00'))
    (314, 'Petit Auto', 'Dewey', 'Catherine ', '(02) 5554 67', 'Rue Joseph-Bens 532', None, 'Bruxelles', None, 'B-1180', 'Belgium', 1401, Decimal('79900.00'))
    (333, 'Australian Gift Network, Co', 'Calaghan', 'Ben', '61-7-3844-6555', '31 Duncan St. West End', None, 'South Brisbane', 'Queensland', '4101', 'Australia', 1611, Decimal('51600.00'))
    (344, 'CAF Imports', 'Fernandez', 'Jesus', '+34 913 728 555', 'Merchants House', "27-30 Merchant's Quay", 'Madrid', None, '28023', 'Spain', 1702, Decimal('59600.00'))
    (348, 'Asian Treasures, Inc.', 'McKenna', 'Patricia ', '2967 555', '8 Johnstown Road', None, 'Cork', 'Co. Cork', None, 'Ireland', None, Decimal('0.00'))
    (350, 'Marseille Mini Autos', 'Lebihan', 'Laurence ', '91.24.4555', '12, rue des Bouchers', None, 'Marseille', None, '13008', 'France', 1337, Decimal('65000.00'))
    (356, 'SAR Distributors, Co', 'Kuger', 'Armand', '+27 21 550 3555', '1250 Pretorius Street', None, 'Hatfield', 'Pretoria', '0028', 'South Africa', None, Decimal('0.00'))
    (361, 'Kommission Auto', 'Josephs', 'Karin', '0251-555259', 'Luisenstr. 48', None, 'Münster', None, '44087', 'Germany', None, Decimal('0.00'))
    (362, 'Gifts4AllAges.com', 'Yoshido', 'Juri', '6175559555', '8616 Spinnaker Dr.', None, 'Boston', 'MA', '51003', 'USA', 1216, Decimal('41900.00'))
    (406, 'Auto Canal+ Petit', 'Perrier', 'Dominique', '(1) 47.55.6555', '25, rue Lauriston', None, 'Paris', None, '75016', 'France', 1337, Decimal('95000.00'))
    (452, 'Mini Auto Werke', 'Mendel', 'Roland ', '7675-3555', 'Kirchgasse 6', None, 'Graz', None, '8010', 'Austria', 1401, Decimal('45300.00'))
    (458, 'Corrida Auto Replicas, Ltd', 'Sommer', 'Martín ', '(91) 555 22 82', 'C/ Araquil, 67', None, 'Madrid', None, '28023', 'Spain', 1702, Decimal('104600.00'))
    (465, 'Anton Designs, Ltd.', 'Anton', 'Carmen', '+34 913 728555', 'c/ Gobelas, 19-1 Urb. La Florida', None, 'Madrid', None, '28023', 'Spain', None, Decimal('0.00'))
    (471, 'Australian Collectables, Ltd', 'Clenahan', 'Sean', '61-9-3844-6555', '7 Allen Street', None, 'Glen Waverly', 'Victoria', '3150', 'Australia', 1611, Decimal('60300.00'))
    


```python

```
