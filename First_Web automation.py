
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:\Development\Testing\Tools\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://fr-ru-uat.np.accenture.com/Ferrero_UAT/Logon.aspx');
time.sleep(2) # Let the user actually see something!
login_box = driver.find_element_by_name('txtUserid')
login_box.clear()
login_box.send_keys('input login here')
pass_box = driver.find_element_by_name('txtPasswd')
pass_box.clear()
pass_box.send_keys('input password here')
driver.find_element_by_id("btnLogin").click()

#**************login*******************

login = WebDriverWait(driver, 50).until(
EC.element_to_be_clickable((By.ID, "pag_MasterRoot_tab_Main_itm_Slsman")))
login.click()

#**************position item click and input*******************

WebDriverWait(driver, 50).until(
EC.element_to_be_clickable((By.ID, "pag_M_Slsman_grd_List_ctl01_pag_M_Slsman_grd_List_2_SLSMAN_CD_SortField")))
slsman_name = driver.find_element_by_name('pag_M_Slsman_gft_List_1_FilterField_Value')
slsman_name.click()
slsman_name.send_keys('E000000843')

#**************search btn click*******************

search = WebDriverWait(driver, 50).until(
EC.element_to_be_clickable((By.NAME, "pag_M_Slsman_grd_List_SearchForm_ButtonSearch_Value")))
search.click()


#**************on position click*******************

position = WebDriverWait(driver, 50).until(
EC.element_to_be_clickable((By.ID, "pag_M_Slsman_grd_List_ctl02_grs_SLSMAN_CD_Value")))
position.click()

#**************clear imei field*******************

imei = WebDriverWait(driver, 50).until(
EC.element_to_be_clickable((By.NAME, "pag_MS_EditGeneral_txt_e_IMEI_Value")))
imei.clear()

#**************save btn click*******************

driver.find_element_by_name("pag_MS_EditGeneral_frm_Detail_Save_Value").click()
WebDriverWait(driver, 50).until(
EC.alert_is_present())
Alert(driver).accept()
time.sleep(5)
driver.quit()



