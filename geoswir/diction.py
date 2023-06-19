import requests
def check_word(word):
    slownik = {
        "ą":"%C4%85",
        "ć":"%C4%87",
        "ę":"%C4%99",
        "ł":"%C5%82",
        "ń":"%C5%84",
        "ó":"%C3%B3",
        "ś":"%C5%9B",
        "ź":"%C5%BA",
        "ż":"%C5%BC"
    }
    word = word.lower()
    for i, j in slownik.items():
        word = word.replace(i,j)
    url = 'https://sjp.pl/{}'.format(word)
    check = requests.get(url)
    status = check.status_code
    if (">dopuszczalne" in check.text and "niedopuszczalne w grach <" in check.text):
        return True
    if "niedopuszczalne w grach <" in check.text:
        return False
    elif status != 200:
        return False
    return True