charTable = {
    '"': [130,0],
    '@': [136,0],

    '…': [50, 6],
    '.': [55, 6],
    ':': [60, 6],
    '(': [65, 6],
    ')': [70, 6],
    '-': [75, 6],
    '\'':[80, 6],
    '!': [85, 6],
    '_': [90, 6],
    '+': [95, 6],
    '\\':[100,6],
    '/': [105,6],
    '[': [110,6],
    ']': [115,6],
    '^': [120,6],
    '&': [125,6],
    '%': [130,6],
    ',': [135,6],
    '=': [140,6],
    '$': [145,6],

    'â': [0,  12],
    'Â': [0,  12],
    'ö': [5,  12],
    'Ö': [5,  12],
    'ä': [10, 12],
    'Ä': [10, 12],
    '?': [15, 12],
    '*': [20, 12],
}

def getCoords(char): 
    code = ord(char)
    if code >= 65 and code <= 90: # capital A-Z
        return [(code - 65) * 5,0]
    elif code >= 97 and code <= 122: # lowercase a-z
        return [(code - 97) * 5,0]
    elif code >= 48 and code <= 57: # 0-9
        return [(code - 48) * 5,6]
    elif char in charTable:
        return charTable[char]
    else:
        return [150,11]

def renderText(text,root,w,getImage):
    text = text[:30]
    print(text)
    i = 0
    for char in root.songtitlecharacters:
        w.itemconfig(char,image=getImage("TEXT","",150,11,155,16))
    for char in text:
        coords = getCoords(char)
        w.itemconfig(root.songtitlecharacters[i],image=getImage("TEXT",char,coords[0], coords[1], coords[0] + 5,coords[1] + 6))
        i = i + 1

def scroll(root,w,getImage):
    if len(root.fullText) < 31: return
    root.scrollFrame = root.scrollFrame + 1
    if not root.scrollText.endswith(" *** " + root.fullText): root.scrollText = root.scrollText + " *** " + root.fullText
    if root.scrollFrame >= 150:
        root.scrollText = root.scrollText[1:]
        renderText(root.scrollText,root,w,getImage)
        root.scrollFrame = 0


def setText(text,root,w,getImage):
    if not hasattr(root,"fullText"): root.fullText = "AAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    if not hasattr(root,"scrollText"): root.scrollText = "AAAAAAAAAAAAAAAAAAAAAAAAAAAA *** AAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    if not hasattr(root,"scrollFrame"): root.scrollFrame = 0
    scroll(root,w,getImage)
    if not root.fullText == text:
        renderText(text,root,w,getImage)
        root.fullText = text
        root.scrollText = text