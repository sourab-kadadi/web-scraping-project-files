# final version
#check the file locations before execution
#the input file should be a json containing list. so for the exising data add [] at beginning and end and replace ' by "
# , delimiter error check in input file referring to " in string
#in the output file format the json by adding [] in start and end and by replacing "}{" by "},{" so as to indicate end of file

from bs4 import BeautifulSoup
import requests
import json

#convert it to list and remove comma at the end

 
# reading the data from the file
# file = open(r"N:/Python projects saved/List_companies/A_company.json", 'r')
# company_database = json.load(file)



#company database input
#A_company 1 to 2100
company_database = [
{'CIN': 'U51909WB2004PTC100637', 'Company_name': 'AAKASH SUPPLIERS PRIVATE LIMITED', 'URL data': 'https://www.zaubacorp.com/company/AAKASH-SUPPLIERS-PRIVATE-LIMITED/U51909WB2004PTC100637', 'company_country': 'India', 'company_address': '29A, NANDAN ROAD , 1ST FLOR KOLKATA WB 700025 IN, ,  - , , '},
{'CIN': 'U72100DL1999PTC101591', 'Company_name': 'AAKASH SYSTEMS PRIVATE LIMITED.', 'URL data': 'https://www.zaubacorp.com/company/AAKASH-SYSTEMS-PRIVATE-LIMITED-/U72100DL1999PTC101591', 'company_country': 'India', 'company_address': 'A 501, ANSAL CHAMBER 1, 3 BHIKAJI CAMA PLACE NEW DELHI DL 110066 IN, ,  - , , '},
]









#convert it to list and remove comma at the end
# company_database = [
# {'CIN': 'U74140DL2009PTC191938', 'Company_name': 'A  A TRAINING PRIVATE LIMITED', 'URL data': 'https://www.zaubacorp.com/company/LIFEPURE-LABS-PRIVATE-LIMITED/U24232CH2015PTC035518', 'company_country': 'India', 'company_address': 'D 810, FIRST FLOOR, NEW FRIENDS COLONY, NEW DELHI - 110065, Delhi, INDIA'},
# {'CIN': 'U74140DL2009PTC191938', 'Company_name': 'A  A TRAINING PRIVATE LIMITED', 'URL data': 'https://www.zaubacorp.com/company/A-B-A-HOTELS-RESORTS-PRIVATE-LIMITED/U55101CH2011PTC033153', 'company_country': 'India', 'company_address': 'D 810, FIRST FLOOR, NEW FRIENDS COLONY, NEW DELHI - 110065, Delhi, INDIA'},
# {'CIN': 'U74899DL1976PTC008196', 'Company_name': 'A & A INFRASTRUCTURE PRIVATE LIMITED', 'URL data': 'https://www.zaubacorp.com/company/VELOX-BIOLOGICS-PRIVATE-LIMITED/U24232CH2011PTC032721', 'company_country': 'India', 'company_address': '275, 2nd Floor, Vardhman Fortune Mall Community Centre GT Karnal Road Delhi North West DL 110033 IN, ,  - , , '}
# ]




def getCompaniesDetails(url_list): 
    url_parse = f'{url}'

    res = requests.get(url_parse)
    soup = BeautifulSoup(res.content, 'lxml')
    company_details = soup.find_all('table', class_='table table-striped')  #here in the site all are in the form of table class, so there are around 6 tabls which are extracted as list so that indexing can be achieved
    updated_on = soup.find('div', style='vertical-align: bottom; float:left; width:45%;') # for the date of updation
    company_database = soup.find_all('div', class_='col-12')   #for parsing presecution, charges and establishment data
    

    # forcontact_parsed = soup.find_all('div', class_='col-lg-6 col-md-6 col-sm-12 col-xs-12')  #use this block only for contact details data
    # contact_info = forcontact_parsed[2] # block for contact data emailID 
    
    contact_info = soup.find('div', style='background: #fff; padding-bottom: 20px; margin-bottom: 20px')  #use this block only for contact details data
    # contact_info = forcontact_parsed[0] # block for contact data emailID 
    


    cin_details_main = soup.find_all('table', class_='table table-striped')  #for CIN
    basic_details_main = company_details[0] # company_details[0] gives list of first table containing company details 
    share_capial_details_main = company_details[3]  # company_details[3] gives share capital details
    listing_filing_main = company_details[4] # company_details[4] gives listing and filing status
    director_details_main = company_details[7] # company_details[7] gives  block of director details and their association with other companies iterate in that to extract further inclusing number of directors etc also also 7 9 gives single director info respectively
    prosecution_details_main = company_database[2] # company_database[2] gives prosecution block
    charges_data_main = company_database[3] # company_database[3] gives charges/borrowing details
    establishments_main = company_database[4] # company_database[4] gives establishements details


    # with open('result.json', 'a') as file:            
    with open('N:/Python projects saved/data scraping Zauba/data_companies_list/Full_details_companies_scraped/A_company_extract_from7942.json', 'a') as file:
      with open('exception.json', 'a') as file_exeption:
        # CIN
        cin_details = {}
        for company_new in cin_details_main[0].find_all('thead'):
            col = 0  
            for basic_details in company_new.find_all('p'):
                if col == 1:
                    company_cin = basic_details.get_text()
                    cin_details.update({
                        'company_CIN' : company_cin
                    })
                
                col = col + 1  
                continue
        
        #working module for company details
        data_main_details = {}
        for company_new in basic_details_main.find_all('tbody'):
            col = 0  
            for basic_details in company_new.find_all('p'):
                # if col == 0:
                #     company_CIN = basic_details
                if col == 1:
                    company_name = basic_details
                if col == 3:
                    company_status = basic_details
                if col == 5:
                    company_roc = basic_details
                if col == 7:
                    company_reg_no = basic_details
                if col == 9:
                    company_category = basic_details
                if col == 11:
                    company_sub_category = basic_details    
                if col == 13:
                    company_class = basic_details
                if col == 15:
                    company_dateof_incorporation = basic_details    
                if col == 17:
                    company_age = basic_details    
                if col == 19:
                    company_activity = basic_details    
                if col == 22:
                    company_number_members = basic_details    

                    data_main_details.update({
                        # 'company_CIN' : company_CIN.get_text(),
                        'company_name' : company_name.get_text(),
                        'company_status' : company_status.get_text(), 
                        'company_roc' : company_roc.get_text(),
                        'company_reg_no' : company_reg_no.get_text(),
                        'company_category' : company_category.get_text(), 
                        'company_sub_category' : company_sub_category.get_text(),
                        'company_reg_no' : company_reg_no.get_text(),
                        'company_category' : company_category.get_text(), 
                        'company_sub_category' : company_sub_category.get_text(),
                        'company_class' : company_class.get_text(),
                        'company_dateof_incorporation' : company_dateof_incorporation.get_text(), 
                        'company_age' : company_age.get_text(),
                        'company_activity' : company_activity.get_text(), 
                        'company_number_members' : company_number_members.get_text()
                    })
                
                col = col + 1  
                continue
        # print(data_main_details)


        # working module for share capital
        data_sharecap = {}
        col = 0          
        for basic_details in share_capial_details_main.find_all('p'):  
                if col == 1:
                    company_authorised_capital = basic_details
                if col == 3:
                    company_paidup_cap = basic_details

                    data_sharecap.update({
                        'company_authorised_capital' : company_authorised_capital.get_text(),
                        'company_paidup_cap' : company_paidup_cap.get_text(),
                    })
                
                col = col + 1  
                continue
        # print(data_sharecap)


    # listing and annual compliance details
        data_listing_annualcompliance = {}
        col = 0          
        for basic_details in listing_filing_main.find_all('p'):  
                if col == 1:
                    company_listing_status = basic_details
                if col == 3:
                    company_last_agm = basic_details
                if col == 5:
                    company_latest_blst = basic_details

                    data_listing_annualcompliance.update({
                        'company_listing_status' : company_listing_status.get_text(),
                        'company_last_agm' : company_last_agm.get_text(),
                        'company_latest_blst' : company_latest_blst.get_text(),
                    })
                
                col = col + 1  
                continue
        # print(data_listing_annualcompliance)

    # contact details
        data_contact_details = {}
        # for company_new in contact_info.find_all('div'):
        col = 0 
        for basic_details in contact_info.find_all('p'):  
                if col == 0:
                    company_email = str(basic_details.get_text())
                if col == 1:
                    company_website = basic_details
                if col == 3:
                    company_address = basic_details

                    data_contact_details.update({
                        'company_email' : company_email[11:],
                        'company_website' : company_website.get_text(),
                        'company_address' : company_address.get_text(),
                    })
                
                col = col + 1  
                continue
        # print(data_contact_details)

    # prosecution details
        data_prosecution = []
        for company_new in prosecution_details_main.find_all('tr'):
            col = 0  
            for basic_details in company_new.find_all('td'):
                if col == 0:
                    company_sno = basic_details
                if col == 1:
                    company_defaulting_entity = basic_details
                if col == 2:
                    company_court_name = basic_details
                if col == 3:
                    company_prosecution_section = basic_details
                if col == 4:
                    company_date_of_order = basic_details
                if col == 5:
                    company_status = basic_details    

                    data_prosecution.append({
                        'company_sno' : company_sno.get_text(),
                        'company_defaulting_entity' : company_defaulting_entity.get_text(), 
                        'company_court_name' : company_court_name.get_text(),
                        'company_prosecution_section' : company_prosecution_section.get_text(),
                        'company_date_of_order' : company_date_of_order.get_text(), 
                        'company_status' : company_status.get_text(),
                    })
                
                col = col + 1  
                continue
        # prosecution_details = data_prosecution[:]
        # print(prosecution_details)          
        # print(data_prosecution)                          #here index[0] refers to the heading which has been kept wantedly as to know if thers nothing

    # charges/borrowings
        data_charges = []
        for company_new in charges_data_main.find_all('tr'):
            col = 0  
            for basic_details in company_new.find_all('td'):
                if col == 0:
                    company_chargeid = basic_details
                if col == 1:
                    company_creation_date = basic_details
                if col == 2:
                    company_modification_date = basic_details
                if col == 3:
                    company_closure_date = basic_details
                if col == 4:
                    company_assets_undercharge = basic_details
                if col == 5:
                    company_amount = basic_details    
                if col == 6:
                    company_chargeholder = basic_details

                    data_charges.append({
                        'company_chargeid' : company_chargeid.get_text(),
                        'company_creation_date' : company_creation_date.get_text(), 
                        'company_modification_date' : company_modification_date.get_text(),
                        'company_closure_date' : company_closure_date.get_text(),
                        'company_assets_undercharge' : company_assets_undercharge.get_text(), 
                        'company_amount' : company_amount.get_text(),
                        'company_chargeholder' : company_chargeholder.get_text(),
                    })
                
                col = col + 1  
                continue
        # charge_details = data_charges[1:]
        # print(charge_details)
        # print(data_charges)       #here index[0] refers to the heading which has been kept wantedly as to know if thers nothing


    # establishment details
        data_establishment = []
        for company_new in establishments_main.find_all('tr'):
            col = 0  
            for basic_details in company_new.find_all('td'):
                if col == 0:
                    establishment_name = basic_details
                if col == 1:
                    establishment_city = basic_details
                if col == 2:
                    establishment_pincode = basic_details
                if col == 3:
                    establishment_address = basic_details

                    data_establishment.append({
                        'establishment_name' : establishment_name.get_text(),
                        'establishment_city' : establishment_city.get_text(), 
                        'establishment_pincode' : establishment_pincode.get_text(),
                        'establishment_address' : establishment_address.get_text(),
                    })
                
                col = col + 1  
                continue
        # establishment_details = data_establishment[1:]   
        # print(establishment_details)
        # print(data_establishment)       #here index[0] refers to the heading which has been kept wantedly as to know if thers nothing





    #director details
        data_directors = []
        row = 0
        for company_new in director_details_main.find_all('tr'):
            col = 0  
            for basic_details in company_new.find_all('td'):

                if col == 0:
                    director_din = basic_details
                if col == 1:
                    director_name = basic_details
                if col == 2:
                    director_designation = basic_details
                if col == 3:
                    director_appointment_date = basic_details
                if col == 4:
                    # director_additional_details = basic_details

                    # row = 0
                    # data_other_company_directors = []                  
                    # for other_directorships in basic_details:
                    #     if row == 0:
                    #         director_other_company = other_directorships
                    #     if row == 1:
                    #         director_other_company_designation = other_directorships
                    #     if row == 2:
                    #         director_other_company_appointmentdate = other_directorships
        
                    #         data_other_company_directors.append({
                    #             'director_other_company' : director_din.get_text(),
                    #             'director_other_company_designation' : director_name.get_text(), 
                    #             'director_other_company_appointmentdate' : director_designation.get_text(),                            
                    #         })  
                    #     row = row + 1
                    #     continue
                    

                    data_directors.append({
                        'director_din' : director_din.get_text(),
                        'director_name' : director_name.get_text(), 
                        'director_designation' : director_designation.get_text(),
                        'director_appointment_date' : director_appointment_date.get_text()
                    })
                
                col = col + 1  
                continue
            # row = row + 1
        

        directors_final_data = data_directors[1::2]



        # full_data = itertools.chain(directors_final_data, data_establishment, data_charges)
        # print(list(full_data))
        


        company_full_data = {
                            'CIN' : cin_details['company_CIN'],                
                            'basic_details' : data_main_details, 
                            'share_capital' : data_sharecap,  
                            'listing_and_annual_compliance' : data_listing_annualcompliance,
                            'company_contactmail_and_address' : data_contact_details,
                            'directors_details' : directors_final_data,
                            'prosecution_details' : data_prosecution[2:],
                            'charges_and_borrowings' : data_charges[2:],
                            'establishment_details' : data_establishment[2:],     
                            'zauba_corp_updated_date' : str(updated_on.b.get_text()[7:].rstrip())               
                            }

        # write the (company_full_data) to a json file 
        # write the (company_full_data) to a json file 
        json.dump(company_full_data, file)
        print(f"last saved CIN {cin_details['company_CIN']}")
        json.dump(exception_list, file_exeption)

  # TRY AND Except block
i = 0
total_hits = 0
exception_list = []
for url in company_database:
    try:
      url = url.get('URL data')
      getCompaniesDetails(url)
      total_hits += 1
      print(f'total scraped {total_hits}')
    except: 
      i += 1
      print(f'number of exception {i}' )
      exception_list.append(str(url))      
      # print(exception_list)
      continue