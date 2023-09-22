import easyocr

# reader = easyocr.Reader(['en'])

def checkNum(reader: easyocr.Reader, img):
    results = reader.readtext(image=img, allowlist='0123456789')
    
    result = results[0]
    bbox = result[0]
    text = result[1]
    score = result[2]
    
    return bbox, text, score
    