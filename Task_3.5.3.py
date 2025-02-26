models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}


# odpowiedź 1
for i in zip(models,sales2018,sales2017,sales2016):
  brand,model = i[0].split(" - ")
  brand_models = cars.setdefault(brand,{})
  brand_model_sales = brand_models.setdefault(model,{})
  brand_model_sales["sales"] = {"2016": 0 if i[3] == "NA" else int(i[3].replace(',',"")),
                                "2017": 0 if i[2] == "NA" else int(i[2].replace(',',"")),
                                "2018": 0 if i[1] == "NA" else int(i[1].replace(',',""))}


# odpowiedź 2
top_brand_2018 = ("",0)
for brand in cars.keys():
  brand_sales = 0
  for model in cars[brand].keys():
    model_sales = cars[brand][model]['sales']['2018']
    brand_sales += model_sales
  if brand_sales > top_brand_2018[1]:
    top_brand_2018 = (brand,brand_sales)
answer2 = top_brand_2018[0]


# odpowiedź 3
for brand in cars.keys():
  for model in cars[brand].keys():
    sales = cars[brand][model]['sales']
    if sales['2016'] == 0 and sales['2017'] > 0:
      answer3.append(model)


# odpowiedź 4
min_model_sales = ("",100000000000000)
for brand in cars.keys():
  for model in cars[brand].keys():
    model_sales = sum(cars[brand][model]['sales'].values())
    if model_sales < min_model_sales[1]:
      min_model_sales = (model,model_sales)
answer4 = min_model_sales[0]


# odpowiedź 5
sales17 = 0
sales18 = 0
for sales in cars['Ford'].values():
  sales17 += sales['sales']['2017']
  sales18 += sales['sales']['2018']
answer5 = "{0:.0%}".format(sales18 / sales17 - 1)