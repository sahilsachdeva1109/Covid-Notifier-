from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 2
)

print("Retrieving_data_from_https://www.worldometers.info/coronavirus/")
data = requests.get("https://www.worldometers.info/coronavirus/")
data = data.text
soup = BeautifulSoup(data, 'html.parser')
print("data_retrieved")
res = soup.find_all("td")
status = False
my_data = []
for i in range(len(res)):
  if str(res[i]) == '<td style="text-align:left;">World</td>':
   status = True
   continue
  if status==True:
    my_data.append(str(res[i])[4:-5])
  
  if str(res[i]) == '<td data-continent="all" style="display:none">All</td>':
    status=False
    break

output_1 = ["New cases: ", "new recovered: ","active cases: ","total deaths: ","total cases: "]
output_2 = my_data[1],my_data[5],my_data[6],my_data[2],my_data[0]
print(my_data)
display = ""
for a,b in zip(output_1,output_2):
  dt = a+b+"\n"
  display+=dt
print(display)

notifyMe("corona_data",display)