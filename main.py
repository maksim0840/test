from selenium import webdriver
from selenium.webdriver.common.by import By
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import time
class Application(App):
    def click(self,instance):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.dns-shop.ru/product/ae13f1e667ee3330/elektroocag-realflame-fobos-lux-brass-cernyj/")
        time.sleep(5)
        price = driver.find_element(By.XPATH,"//div[@class='product-buy__price-wrap product-buy__price-wrap_interactive']/div[1]").text
        driver.quit()
        self.label.text=price
    def build(self):
        together=BoxLayout()
        b=Button(text="start",on_press=self.click)
        self.label=Label(text="НИЧЕГО")
        together.add_widget(b)
        together.add_widget(self.label)
        return together
if __name__=='__main__':
    Application().run()