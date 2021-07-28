from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import random

""" 
    UYARI:
        Bu Mini Proje öğrenilen bilgileri pekiştirme amacı ile yapılmıştır.
        Kullanılması Halinde Sorumluluk kullanan kişiye aittir!
    
    KULLANIM:
        1- Whatsapp Chat Botu ile seçtiğiniz kişi çevrim içi olduğunda
        o kişiye otomatik olarak mesaj gönderebilirsiniz.

        2- Seçtiğiniz kişi çevrimiçi olduğunda o kişiye messages.txt 
        dosyanıza yazdığınız mesajlardan biri rastgele seçilerek gönderilir.

        3- Aktiflik durumu Çevrimdışıyken Çevrimiçi olduğunda fonksiyon çalışır.
    
        4- Kullanıcı çevrimiçiyse ve durumu "Yazıyor" ise durum "Çevrimiçi" olursa
        fonksiyon yine çalışır.Ve otomatik yanıt gönderilir.
"""



# messages.txt dosyamıza eklediğimiz yazıların satırlara ayırılması ve liste olarak alınması
with open('messages.txt','r',encoding='utf-8') as messages:
    text = messages.read()
    messagelist = list()    
    messagelist = text.split('\n')     


# print(messagelist)
# messages.txt dosyamıza eklediğimiz yazıların yazdırılması


# Chat Bot Fonksiyonu
def StartChatBot():
    flag = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com')
    input('QR Kodu okuttuysanız herhangi bir tuşa basınız.') # QR Kodu okuttuktan sonra Bot un çalışması için herhangi bir tuşa basınız. 
    message_area = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    while True:
        message_area.click()
        wp_source = driver.page_source
        soup = bs(wp_source,'lxml')
        search = soup.find_all('div', {'class': ['zzgSd', '_3e6xi']})      
        try: 
            online = search[0].span.text # Whatsapp çevrimiçi bilgisinin alınması
            print(online)
            if (online in ['çevrimiçi','online']) and flag == False:
                print(f'Online-Çevrimiçi.')
                # messages.txt dosyasından rastgele yazı seçilmesi ve gönderilmesi
                msgToSend = messagelist[random.randint(0,len(messagelist)-1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            elif (online not in ['çevrimiçi','online']):
                print(f'Şuan da Çevrimdışı.')
                flag = False
        except:
            print(f'Şuan da Çevrimdışı.')
            flag = False

        # Çevrimiçi kontrolünün tekrar yapılması için seçtiğimiz süre.(Değiştirilebilir)     
        time.sleep(15) 

StartChatBot()