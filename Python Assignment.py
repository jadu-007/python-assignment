from selenium import webdriver
import autoit
import time

from selenium import webdriver
import csv
with open('python_assignment.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    
    spamwriter.writerow(["Diary No.",
                         "Case No.",
                         "Present/Last Listed On",
                         "Status/Stage",
                         "Disp.Type",
                         "Category",
                         "Act",
                         "Petitioner(s)",
                         "Respondent(s)",
                         "Pet. Advocate(s)",
                         "Resp. Advocate(s)",
                         "U/Section"])
driverpth = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=driverpth)

for year in range(2020,2000,-1):
    for diary_number in range(1,100):
        driver.get("https://main.sci.gov.in/case-status")
        time.sleep(3)
        text=driver.find_element_by_id("ansCaptcha").send_keys(driver.find_element_by_id("cap").text.strip())
        text=driver.find_element_by_id("CaseDiaryNumber").send_keys(str(diary_number))
        driver.find_element_by_xpath("//select[@name='CaseDiaryYear']/option[text()="+str(year)+"]").click()
        driver.find_element_by_id("getCaseDiary").click()
        print("Diary Number ",diary_number,"\nYear ",year)
        print("Done")

        time.sleep(3)
        tbodies = driver.find_element_by_class_name("container_cs")

        tds = tbodies.find_elements_by_tag_name("td")

        td=[]
        for i in range(1,21,2):
            td.append(tds[i].text)
        with open('python_assignment.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(td)




