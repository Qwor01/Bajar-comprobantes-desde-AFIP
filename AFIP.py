import pyautogui as pt
from time import sleep

#login
sleep(3)
position = pt.locateOnScreen("cuitlog.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+5,y+50, duration=.05)
pt.tripleClick()
pt.typewrite("INGRESE SU CUIT AQUI", interval=.05)
position = pt.locateOnScreen("next.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(.5)
position = pt.locateOnScreen("pass.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+5,y+50, duration=.05)
pt.tripleClick()
pt.typewrite("INGRESE SU CONTRASEÑA AQUI", interval=.05)
position = pt.locateOnScreen("login.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(3)
#bajada
position = pt.locateOnScreen("misservicios.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(3)
pt.scroll(-4500)
sleep(.5)
position = pt.locateOnScreen("miscomprobantes.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(5)
position = pt.locateOnScreen("threepoints.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
position = pt.locateOnScreen("search.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(.5)
pt.typewrite("microteatro", interval=.05)
pt.moveTo(x,y+180, duration=.05)
pt.click()
sleep(.5)
position = pt.locateOnScreen("emitidos.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+200,y+200, duration=.05)
pt.click()
sleep(3)
position = pt.locateOnScreen("fechacomprobante.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+150,y+50, duration=.05)
pt.tripleClick()
pt.typewrite("01/10/2022 - 25/10/2022", interval=.05)
pt.scroll(-4500)
pt.moveTo(x-5000,y+50, duration=.05)
pt.click()
sleep(.5)
position = pt.locateOnScreen("busca.PNG", confidence=.7)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(3)
position = pt.locateOnScreen("excel.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(1)
position = pt.locateOnScreen("cerrar.PNG", confidence=.7)
x= position[0]
y= position[1]
pt.moveTo(x+140,y+10, duration=.05)
pt.click()
sleep(.5)
position = pt.locateOnScreen("pestana.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+260,y+15, duration=.05)
pt.click()
position = pt.locateOnScreen("miscomprobantes.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(5)
position = pt.locateOnScreen("threepoints.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
position = pt.locateOnScreen("search.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(.5)
pt.typewrite("microteatro", interval=.05)
pt.moveTo(x,y+180, duration=.05)
pt.click()
sleep(1)
position = pt.locateOnScreen("emitidos.PNG", confidence=.9)
x= position[0]
y= position[1]
pt.moveTo(x+500,y+200, duration=.05)
pt.click()
sleep(5)
position = pt.locateOnScreen("fechacomprobante.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+150,y+50, duration=.05)
pt.tripleClick()
pt.typewrite("01/10/2022 - 25/10/2022", interval=.05)
pt.scroll(-4500)
pt.moveTo(x-5000,y+50, duration=.05)
pt.click()
sleep(.5)
position = pt.locateOnScreen("busca.PNG", confidence=.6)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(3)
position = pt.locateOnScreen("excel.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x,y, duration=.05)
pt.click()
sleep(1)
position = pt.locateOnScreen("cerrar.PNG", confidence=.7)
x= position[0]
y= position[1]
pt.moveTo(x+140,y+10, duration=.05)
pt.click()
sleep(.5)
position = pt.locateOnScreen("pestana.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+260,y+15, duration=.05)
pt.click()
pt.moveTo(x-5000,y+500, duration=.05)
sleep(.5)
pt.click()
pt.scroll(4500)
sleep(.5)
position = pt.locateOnScreen("exit.PNG", confidence=.8)
x= position[0]
y= position[1]
pt.moveTo(x+5,y+5, duration=.05)
pt.click()