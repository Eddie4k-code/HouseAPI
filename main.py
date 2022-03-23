import requests
import pandas as pd

df = pd.DataFrame





def sold_houses():
    import requests

    url = "https://realty-in-us.p.rapidapi.com/properties/list-sold"

    querystring = {"city": "", "state_code": "", "offset": "0", "limit": "200", "sort": "newest"}

    headers = {
        'x-rapidapi-host': "realty-in-us.p.rapidapi.com",
        'x-rapidapi-key': "API KEY GOES HERE"
    }

    sold = requests.request("GET", url, headers=headers, params=querystring)
    sold_data = sold.json()

    main_dict = sold_data['listings']

    property_id_list = []
    property_type_list = []
    property_address_list = []
    property_price_list = []
    property_sell_date = []
   

    for dict in main_dict:
        

        df = pd.DataFrame()


        property_id_list.append(dict["property_id"])
        property_type_list.append(dict['prop_type'])
        property_address_list.append(dict['address'])
        property_price_list.append(dict['price_raw'])
        property_sell_date.append(dict['sold_date'][0:3])



    
    df.insert(loc=0, column='Property_ID', value=property_id_list)
    df.insert(loc=1, column='Property_Type', value=property_type_list)
    df.insert(loc=2, column='Address', value=property_address_list)
    df.insert(loc=3, column='Price', value=property_price_list)
    df.insert(loc=4, column='Sold Date', value=property_sell_date)
    
    













    #Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('test.xlsx')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

    # Close the Pandas Excel writer and output the Excel file.
    writer.close()
