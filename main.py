from datetime import date, timedelta
from selenium import webdriver
from time import sleep
import pyautogui


class AbsenSenin:
    def __init__(self):
        AbsenHarian(email, pw, now, nis, nisn, nama, absenharian)
        AbsenInggris(email, pw, nama, absen, pertemuan, bj_senin, inggris)
        AbsenPWPB(email, pw, now, pwpb)
        AbsenIndo(email, pw, now, nama, absen, indo)


class AbsenSelasa:
    def __init__(self):
        AbsenHarian(email, pw, now, nis, nisn, nama, absenharian)
        AbsenSunda(email, pw, nama, absen, bj_selasa, sunda)
        AbsenIndo(email, pw, now, nama, absen, indo)
        AbsenPBO(email, pw, nama, bj_selasa, pbo)


class AbsenRabu:
    def __init__(self):
        AbsenHarian(email, pw, now, nis, nisn, nama, absenharian)
        AbsenPWPB(email, pw, now, pwpb)
        AbsenPBO(email, pw, nama, bj_selasa, pbo)
        AbsenPKN(email, pw, nama, pkn)
        # AbsenPKWU(email, pw, nama, pkwu)


class AbsenKamis:
    def __init__(self):
        AbsenHarian(email, pw, now, nis, nisn, nama, absenharian)
        AbsenPWPB(email, pw, now, pwpb)
        AbsenBK(email, pw, nama, bk)
        AbsenDB(email, pw, nama, now, db)
        AbsenAgama(email, pw, nama, agama)


class AbsenJumat():
    def __init__(self):
        AbsenHarian(email, pw, now, nis, nisn, nama, absenharian)
        AbsenPKK(email, pw, nama, bj_jumat, pkk)
        AbsenMTK(email, pw, bj_jumat, mtk)


class AbsenHarian:
    def __init__(self, email, pw, now, nis, nisn, nama, absenharian):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(absenharian)
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(now)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nis)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nisn)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nama)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[4]").click()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div[3]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span").click()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span").click()
        sleep(5)


class AbsenInggris:
    def __init__(self, email, pw, nama, absen, pertemuan, bj_senin, inggris):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(inggris)
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nama)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(absen)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/span").click()
        iframe = self.driver.find_element_by_class_name('picker-frame')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[4]/div").click()
        sleep(3)
        pyautogui.typewrite(bj_senin)
        pyautogui.press('enter')
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]").click()
        sleep(7)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div").click()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(pertemuan)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span").click()
        sleep(5)


class AbsenPWPB:
    def __init__(self, email, pw, now, pwpb):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(pwpb)
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[36]').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(now)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys('09')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys('02')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div/div/div/span/span').click()
        sleep(5)


class AbsenIndo:
    def __init__(self, email, pw, now, nama, absen, indo):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(indo)
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(now)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nama)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div").click()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(absen)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span").click()
        sleep(5)


class AbsenSunda:
    def __init__(self, email, pw, nama, absen, bj_selasa, sunda):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(sunda)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(absen)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/span/span[2]").click()
        sleep(1)
        iframe = self.driver.find_element_by_class_name('picker-frame')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[4]/div").click()
        sleep(3)
        pyautogui.typewrite(bj_selasa)
        pyautogui.press('enter')
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]").click()
        sleep(7)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span').click()
        sleep(5)


class AbsenPBO:
    def __init__(self, email, pw, nama, bj_selasa, pbo):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(pbo)
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(email)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nama)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div").click()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]/span").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/span/span[2]").click()
        sleep(1)
        iframe = self.driver.find_element_by_class_name('picker-frame')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[4]/div").click()
        sleep(3)
        pyautogui.typewrite(bj_selasa)
        pyautogui.press('enter')
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]").click()
        sleep(7)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span")
        sleep(5)


class AbsenPKN:
    def __init__(self, email, pw, nama, pkn):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(pkn)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div').click()
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span').click()
        sleep(5)


class AbsenBK:
    def __init__(self, email, pw, nama, bk):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(bk)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span').click()
        sleep(5)


class AbsenDB:
    def __init__(self, email, pw, nama, now, db):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(db)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(now)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]/span').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Basis Data')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div/div/span/span').click()
        sleep(5)


class AbsenAgama:
    def __init__(self, email, pw, nama, agama):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(agama)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Pendidikan Agama Islam')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Pendidikan Agama Islam')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span').click()
        sleep(5)


class AbsenPKWU:
    def __init__(self, email, pw, now, pkwu):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(pkwu)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[36]/span').click()
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(now)
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys('10')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys('00')
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div').click()
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[3]/div/div/div/span/span').click()
        sleep(5)


class AbsenPKK:
    def __init__(self, email, pw, nama, bj_jumat, pkk):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(pkk)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[7]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/span/span[2]").click()
        iframe = self.driver.find_element_by_class_name('picker-frame')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[4]/div").click()
        sleep(3)
        pyautogui.typewrite(bj_jumat)
        pyautogui.press('enter')
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]").click()
        sleep(7)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span').click()
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span').click()
        sleep(5)


class AbsenMTK:
    def __init__(self, email, pw, bj_jumat, mtk):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27')
        self.driver.find_element_by_xpath(
            '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath(
            '//input[@type="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@type="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get(mtk)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[36]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div/label/div/div[1]/div/div[3]/div').click()
        self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/span/span[2]").click()
        iframe = self.driver.find_element_by_class_name('picker-frame')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[4]/div").click()
        sleep(3)
        pyautogui.typewrite(bj_jumat)
        pyautogui.press('enter')
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]").click()
        sleep(7)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/form/div[2]/div/div[3]/div/div/div/span/span').click()
        sleep(5)


email = "emaillu"
pw = "pwgooglelu"
nis = "nislu"
nisn = "nisnlu"
nama = "namalu"
absen = "absenlu"
kelas = "kelas lu"

bj_senin = "D:\\Users\\Zikri\\Pictures\\seragam\\senin.jfif"
bj_selasa = "D:\\Users\\Zikri\\Pictures\\seragam\\selasa.jfif"
bj_rabu = "D:\\Users\\Zikri\\Pictures\\seragam\\rabu.jfif"
bj_kamis = "D:\\Users\\Zikri\\Pictures\\seragam\\kamis.jfif"
bj_jumat = "D:\\Users\\Zikri\\Pictures\\seragam\\jumat.jfif"

absenharian = "https://docs.google.com/forms/d/e/1FAIpQLSfa_TAvzg0cc7yyQiydjzLr2wKuViXrsm8ISsDmnHtXerJ6bQ/viewform?usp=send_form"
inggris = "https://docs.google.com/forms/d/e/1FAIpQLSex1PJ6KS_SQ7NF7sEK_6m2vaXSn0FRg00_g0llpFksMXgRZg/viewform "
pwpb = "https://docs.google.com/forms/d/e/1FAIpQLSfKY2NpKSky16jeJXw4sj7EJwHId0CUcUjiFGkCb9qnvtixNQ/viewform"
indo = "https://docs.google.com/forms/d/e/1FAIpQLSfrl8L39589XiaupxifBOsiwvWjPFsc-xb1O8X3ULPKrOrB4Q/viewform"
sunda = "https://docs.google.com/forms/d/e/1FAIpQLScEzYMIR2162coCRfoOtZx3b3bDAzGGWltjyZtmy_RPuwjJEQ/viewform"
pbo = "https://docs.google.com/forms/d/e/1FAIpQLScfVFqcqtYHhoF-SfbNvhAaYbzvdX-8AqrM3ndOIpMUKLLNBw/viewform"
pkn = "https://docs.google.com/forms/d/e/1FAIpQLScRGtsHI_rTdv9xwUWxEhMCAf1ypZZJiPHnf1h8Y2n8IPz9bw/viewform?hr_submission=ChkI5N3RsocCEhAIno-gwbgDEgcI5-7sjbUDEAA"
bk = "https://docs.google.com/forms/d/e/1FAIpQLSeKaR8YDCy139kobOsLhmRB2Q8BD4Y1LMvElS2oVaYLvEPbAA/viewform"
db = "https://docs.google.com/forms/d/1mb81uBsZI_qeJFn9PXlwD1EloDWtWHatG8PxHTxRYdA/viewform?edit_requested=true"
agama = "https://docs.google.com/forms/d/e/1FAIpQLSdc5HevZ2z7gL-ZXG0-UaK9FcPIoW0Ulp4lftlMB4nNjj2aOg/viewform?hr_submission=ChkI5N3RsocCEhAIg8iV1cYDEgcIltnxgrUDEAE"
pkk = "https://docs.google.com/forms/d/e/1FAIpQLSf2ExRHpHyKv1KJDQ_LtaMiOYetVrsq9eEzuN0jJ1BYfuVkkQ/viewform"
mtk = "https://docs.google.com/forms/d/e/1FAIpQLSe64HnU2sUQktzhiCbgcel7O667RJHAcQrSqGuxBjjijBn2-w/viewform"
pkwu = "https://docs.google.com/forms/d/e/1FAIpQLScgLtZzvGpWYm9AEs4uWST41kF64UcHdkXez6Wi6_5S7dq9mw/viewform"

start_date = date(2020, 7, 20)
end_date = date.today()
delta = timedelta(days=1)
count = 0
while start_date <= end_date:
    pertemuan = [start_date.strftime("%A")]
    start_date += delta
    count += pertemuan.count("Monday")

today = date.today()
day = str(today.strftime("%d"))
month = str(today.strftime("%m"))
year = str(today.strftime("%Y"))
now = day+month+year
pertemuan = count


if today.strftime('%A') == "Monday":
    AbsenSenin()
    
elif today.strftime('%A') == "Tuesday":
    AbsenSelasa()

elif today.strftime('%A') == "Wednesday":
    AbsenRabu()

elif today.strftime('%A') == "Thursday":
    AbsenKamis()

elif today.strftime('%A') == "Friday":
    AbsenJumat()

else:
    print('rajin amat bang')
