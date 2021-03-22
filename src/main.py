from selenium import webdriver
import webdriver_manager.chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = "https://egramswaraj.gov.in/approveActionPlan.do"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install(),
                           chrome_options=chrome_options)
result = browser.get(url=url)

myscript='''
fnyearId="2020";
planyearid="2020-2021";
$("#levelId").val(0);
level=3;
$("#accordionflgId").val(level);
document.getElementById("fnyearId").value=fnyearId;
document.getElementById("planyearid").value=planyearid;
state_cd='27';
level=3;
fyear='2020';
statenm='MAHARASHTRA';
$("#levelId").val(level);
$("#fnyearId").val(fyear); 
$("#stateId").val(state_cd);
$("#statenmId").val(statenm); 

function getgpreportBis(state_cd,level,fyear,zp_cd,bp_cd,typcod){
	 $("#levelId").val(level);
	 $("#stateId").val(state_cd);
	 $("#fnyearId").val(fyear); 
	 $("#zpcdId").val(zp_cd); 
	 $("#bpcdId").val(bp_cd);
	 $("#local_body_typ_cdid").val(typcod);
	 $("#accordionflgId").val(3);
}
getgpreportBis('27',3,'2020','424','4635',0);
getplanView('3087240','236630',5,4,'AHMEDNAGAR','AKOLE','RANAD KHURD-BUDRUK','3');
'''

browser.execute_script(myscript)

result = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.ID, 'collapseTwo')))
print(result.get_attribute('innerHTML'))
