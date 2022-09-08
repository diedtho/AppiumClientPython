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

@dataclass
class TabItem:
    name: str
    number: int
    text: str
    webelement: WebElement
    parent: str
    button_id: str

@dataclass
class MenuItem:
    name: str
    number: int
    text: str
    webelement: WebElement
    parent: str
    button_id: str

def attrs2menu_items(webele, i, parent):
    elemid = webele.id
    elemtext = webele.text
    menu_item = MenuItem(name="unnamed", number=i, text=elemtext, webelement=webele, button_id=elemid, parent=parent)
    return menu_item

def attrs2tab_items(webele, i, parent):
    elemid = webele.id
    elemtext = webele.text
    tab_item = TabItem(name="unnamed", number=i, text=elemtext, webelement=webele, button_id=elemid, parent=parent)
    return tab_item

def attrs2buttons(webele, i, parent):
    elemid = webele.id
    elemtext = webele.text
    button = Button(name="unnamed", number=i, text=elemtext, webelement=webele, button_id=elemid, parent=parent)
    return button