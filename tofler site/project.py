#always check for the input and output files

from bs4 import BeautifulSoup
import requests
import json

# fn = open('C:\Work\pythonScript\LLP1_new_company.json')

fn = open('C:/Work/pythonScript/Tofler/financials extract/zaubadatabase_ref/C2_company_extract - Formatted.json')

company_database = json.load(fn)

def getCompaniesDetails(company_list): 


  proxies = {
    "http": "http://yyyyyyyyyyyyyy.com:vedsph@gate2.proxyfuel.com:2000",  # add your proxy here
    "https": "http://yyyyyyyyyyyy.com:vedsph@gate2.proxyfuel.com:2000",
  }

# Pretend to be Firefox
  headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
  }

  CIN_num = company_list['CIN']
  company_name = company_list['basic_details']['company_name']
  company_name_dash = company_name.replace('. ', '-').replace('.', '-').replace(' (', '-').replace(') ', '-').replace(' ', '-').replace('&', 'and').replace('(', '-').replace(')', '-').lower()
  url = f'https://www.tofler.in/{company_name_dash}/company/{CIN_num}/financials'
  print(url)
  res = requests.get(url, proxies=proxies, headers=headers, timeout=20)
  soup = BeautifulSoup(res.content, 'lxml')
  company_details = soup.find_all('table', class_='table striped highlight responsive')  
  print(res)
  # company_charges = soup.find('table', {"id": "chargeassetdatatable"})
  




  # print(res)
  # print(url_gen)
  company_financials = company_details[0]
  # company_charges_data = soup.find('table', id = 'chargeassetdatatable').find('tbody') 
  # print(company_charges_data)

  with open('C:/Work/pythonScript/Tofler/financials extract/Financials_tofler_extract/C2_3_company_extract.json', 'a') as file:
      with open('C:/Work/pythonScript/Tofler/financials extract/Financials_tofler_extract/C2_3_company_extract.json', 'a') as file_exeption:
      # CIN
      # cin_details = {}
      # for company_new in cin_details_main[0].find_all('thead'):
      #     col = 0  
      #     for basic_details in company_new.find_all('p'):
      #         if col == 1:
      #             company_cin = basic_details.get_text()
      #             cin_details.update({
      #                 'company_CIN' : company_cin
      #             })
              
      #         col = col + 1  
      #         continue
      
      #working module for company details
        company_data_financials = {}
        col = 1
        for basic_details in company_financials.find_all('span'):
            if col == 1:
                operating_revenue = basic_details
            if col == 2:
                EBITDA = basic_details
            if col == 3:
                networth = basic_details
            if col == 4:
                debt_to_equity_ratio = basic_details
            if col == 5:
                return_on_equity = basic_details
            if col == 6:
                total_assets = basic_details    
            if col == 7:
                fixed_assets = basic_details
            if col == 8:
                current_assets = basic_details    
            if col == 9:
                current_liability = basic_details    
            if col == 10:
                trade_receivables = basic_details    
            if col == 11:
                trade_payables = basic_details 
                
            if col == 12:
                current_ratio = basic_details    

                company_data_financials.update({
                    'operating_revenue' : operating_revenue.get_text(),
                    'EBITDA_y_o_y' : EBITDA.get_text(), 
                    'networth_y_o_y' : networth.get_text(),
                    'debt_to_equity_ratio' : debt_to_equity_ratio.get_text(),
                    'return_on_equity' : return_on_equity.get_text(), 
                    'total_assets_y_o_y' : total_assets.get_text(),
                    'fixed_assets_y_o_y' : fixed_assets.get_text(),
                    'current_assets_y_o_y' : current_assets.get_text(), 
                    'current_liability_y_o_y' : current_liability.get_text(),
                    'trade_receivables_y_o_y' : trade_receivables.get_text(),
                    'trade_payables_y_o_y' : trade_payables.get_text(), 
                    'current_ratio' : current_ratio.get_text()
                })

            col = col + 1
            continue

        # print(company_data_financials)

    #details for company charges
        # charge_details_tler = []
        # for company_charge_total in company_charges_data.find_all('tr'):
        #     col = 0

        #     for basic_details in company_charge_total.find_all('td'):
        #         if col == 0:
        #             company_chargeid = basic_details
        #         if col == 1:
        #             charge_creation_or_modification_date = basic_details
        #         if col == 2:
        #             charge_modified = basic_details
        #         if col == 3:
        #             charge_amount = basic_details
        #             charge_val = charge_amount.replace(' ','')
        #             if charge_val[-2:] == 'cr':
        #               charge_val = (float(charge_val[:-2]) * 10000000)  
        #             else :
        #               charge_val = (float(charge_val[:-3]) * 100000)
        #         if col == 4:
        #             company_chargeholder = basic_details

        #             charge_details_tler.append({
        #                 'company_chargeid' : company_chargeid.get_text(),
        #                 'charge_creation_or_modification_date' : charge_creation_or_modification_date.get_text(), 
        #                 'charge_modified' : charge_modified.get_text(),
        #                 'charge_amount' : charge_amount.get_text(),
        #                 'company_chargeholder' : company_chargeholder.get_text()
        #             })
              
        #         col = col + 1  
        #         continue

        # print(charge_details_tler)

        # charge_total_rs = 0
        # for charges_am in charge_details_tler:  
        #   charge_val = charges_am['charge_amount']

        #   charge_total_rs += charge_val
        # print(charge_total_rs)

        company_full_data = {
                            'CIN' : CIN_num,                
                            'company_main_financials' : company_data_financials, 
                            # 'charge_details_tler' : charge_details_tler,
                            # 'charge_total_rs' : charge_total_rs
                            }

        print(company_full_data)

        json.dump(company_full_data, file)
      json.dump(company_full_data, file_exeption)


      # print(data_main_details)

# for company_list in company_database:
#   # print(company_list)
#   try:
#     getCompaniesDetails(company_list)
#   except:
#     continue

  # TRY AND Except block
i = 0
total_hits = 0
exception_list = []
for company_list in company_database:
    try:
      if company_list.get('basic_details', {}).get('company_status') != "Strike Off":
        new_update = company_list
        getCompaniesDetails(new_update)
      total_hits += 1
      print(f'total scraped {total_hits}')
    except: 
      i += 1
      print(f'number of exception {i}' )
      exception_list.append(str(company_list))      
      continue



fn.close()


