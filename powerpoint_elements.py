from dataclasses import dataclass
from appium.webdriver.webelement import WebElement

@dataclass
class Button:
    name: str
    number: int
    text: str
    webelement: WebElement
    parent: str
    button_id: str

def attrs2button(webele, i, parent):
    elemid = webele.id
    elemtext = webele.text
    button = Button(name="unnamed", number=i, text=elemtext, webelement=webele, button_id=elemid, parent=parent)
    return button

