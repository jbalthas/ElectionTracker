from selenium import webdriver
from time import sleep
from datetime import datetime

CurrV = 0; 

driver = webdriver.Chrome('/usr/local/bin/webdrivers/chromedriver')

driver.get("https://www.google.com/search?q=trump+vs+biden&oq=trump+vs+biden&aqs=chrome..69i57j0i131i433l5j69i61l2.10557j0j7&sourceid=chrome&ie=UTF-8")

biden = False; 
trump = False; 

            
        

def votes():

    
    Trump_eleP = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[3]/td[2]/span').text
    Biden_eleP = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[2]/td[2]/span').text

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print('---------------------------------')
    print("Current Time =", current_time + '\n')
    

    TrumpVotes = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[2]/td[4]/span').text
    BidenVotes = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[2]/td[4]/span').text

    TrumpPer = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[3]/td[3]/span').text
    BidenPer = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[2]/td[3]/span').text

    print ("------------ Popular ------------")
    print ("Trump votes: " + TrumpVotes + '\t || Trump Percent:' + TrumpPer)
    print ("Biden votes: " + BidenVotes + '\t || Biden Percent:' + BidenPer)
    print ("---------------------------------")
    
    

 
    driver.find_element_by_xpath('//*[@id="eob-mp-path_NV_1"]').click()
    sleep(1)
    Ne_TV = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[3]/td[3]/span').text
    Ne_TP = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[3]/td[2]/span').text
    Ne_BV =driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[2]/td[3]/span').text   
    Ne_BP = driver.find_element_by_xpath('//*[@id="1"]/table/tbody/tr[2]/td[2]/span').text


    print ("------------ Nevada -------------")
    print ("Trump votes: " + Ne_TV + '\t || Trump Percent:' + Ne_TP)
    print ("Biden votes: " + Ne_BV + '\t || Biden Percent:' + Ne_BP+'\n')
    
    Ne_TV = int(Ne_TV.replace(',', ''))
    Ne_BV = int(Ne_BV.replace(',', ''))

    
    
    if(Ne_TV > Ne_BV):
        print("Trump is winning by: " + '{:,}'.format(Ne_BV - Ne_TV) + " votes")
        CurrV = Ne_BV - Ne_TV
        trump = True
        biden = False
    else:
        print("Biden is winning by: " + '{:,}'.format(Ne_BV - Ne_TV) + " votes")
        CurrV = Ne_BV - Ne_TV
        trump = False
        biden = True

    



    print ("---------------------------------")
    pastFile = open("CurrentVotes.txt", "r")
    pastV = pastFile.read()

    pastV = int(pastV)
    if(pastV != CurrV):
        pastFile.close()
        text_file = open("CurrentVotes.txt", "w")
        n = text_file.write(str(CurrV))
        text_file.close()
        print("NEW RESULTS\n")
        if(biden == True):
            print("Biden is currently winning \nPast vote difference: " + '{:,}'.format(pastV) + "\tNew Resuls: "+ '{:,}'.format(CurrV))
        else:
            print("Trump is currently winning \nPast vote difference: " + '{:,}'.format(pastV) + "\tNew Resuls: "+ '{:,}'.format(CurrV))

    else:
        pastFile.close()

    
    

    Trump_eleP = int(Trump_eleP.replace(',', ''))
    Biden_eleP = int(Biden_eleP.replace(',', ''))

    if(Trump_eleP >= 270):
        print("DONALD TRUMP HAS WON THE ELECTION")
    elif(Biden_eleP >= 270):
        print("JOE BIDEN HAS WON THE ELECTION")
    else:
        print("Race is still on! \n")
    



    print("Quitting...")
    driver.quit()



  
    
    
votes()

