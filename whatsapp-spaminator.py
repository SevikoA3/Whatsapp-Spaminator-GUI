from selenium import webdriver
import tkinter as tk
import time

window = tk.Tk()
window.title("The Whatsapp-Spaminator")
window.geometry("750x400")
window.minsize(750, 400)

#untuk command
def checkint(x) :
    try :
        int(x)
        return False
    except ValueError :
        return True

def spam() :
    nama = input1.get()
    pesan = input2.get()
    if(nama == "" or pesan == "" or checkint(input3.get())) :
        pesanError.config(text="Masukkan Nama atau Pesan Terlebih dahulu dan Jangan Lupa Input di Pertanyaan ke-3 dengan Angka")
    else :
        jumlah = int(input3.get())
        pesanError.config(text="")
        driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
        driver.implicitly_wait(15) 
        driver.get('https://web.whatsapp.com')
        driver.find_element_by_css_selector("span[title='" + nama + "']").click()
        for _ in range(jumlah):
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(pesan)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        time.sleep(3)
        driver.quit()

#untuk tulisan
label1 = tk.Label(window, text="Nama yang akan di spam :", font="none 18 bold")
label1.place(anchor=tk.CENTER, relx = 0.5, rely = 0.1)
label2 = tk.Label(window, text="Pesan yang akan dikirim :", font="none 18 bold")
label2.place(anchor=tk.CENTER, relx = 0.5, rely = 0.3)
label3 = tk.Label(window, text="Dikirim berapa kali?", font="none 18 bold")
label3.place(anchor=tk.CENTER, relx = 0.5, rely = 0.5)
pesanError = tk.Label(window, text="", fg="red")
pesanError.place(anchor=tk.CENTER, relx = 0.5, rely = 0.9)

#untuk masukan
input1 = tk.Entry(window, width = 20, font="none 12 bold")
input1.place(anchor=tk.CENTER, relx = 0.5, rely = 0.2)
input2 = tk.Entry(window, width = 40, font="none 12 bold")
input2.place(anchor=tk.CENTER, relx = 0.5, rely = 0.4)
input3 = tk.Entry(window, width = 10, font="none 12 bold")
input3.place(anchor=tk.CENTER, relx = 0.5, rely = 0.6)

#tombol
tombolSpam = tk.Button(window, text="Spam!", command=spam, font="none 14 bold")
tombolSpam.place(anchor=tk.CENTER, relx = 0.5, rely = 0.75)

window.mainloop()