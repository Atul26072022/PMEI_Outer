import requests
import time
from outerconfig import PMEIDBLink, InnerDbUrl
while(True):
    PDIDBlink = requests.get(InnerDbUrl.pdi_fetch)
    data = PDIDBlink.json()
    response_data = data["data"]
    for data in response_data:

        PDI_POST_Data = requests.post(PMEIDBLink,data)
        
        payload = {
            "PDI_ID_INPUT_COIL": data["PDI_ID_INPUT_COIL"],
            "READ_FLAG":True
        }
        requests.patch("http://127.0.0.1:8000/pdi/",payload)
        print("Data transfered")
        # print(datatras)
        
        
    # for i in range(len(response_data)):
    #     send_data = response_data[i]
    #     payload = {
    #                 "coil":send_data
    #             }
        
    #     # del send_data['id']
    #     # del send_data['PDI_READ_FLAG']
    #     # red_flag = send_data['PDI_ID_INPUT_COIL']
    #     # print("red flag",red_flag)
    #     PDI_POST_Data = requests.post("http://127.0.0.1:8001/pdi/schedulecancell/",payload)
    #     PDI__red_flag_true = requests.post("http://127.0.0.1:8000/pdi/schedulecanceel/",payload)
    
    
    
    time.sleep(10)