import arrr

def translate():
    english = Element("input").element.value
    pirate = arrr.translate(english)
    output = Element("output")
    output.element.innerText = pirate
