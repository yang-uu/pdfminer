import urllib.parse

def url(base, **kw):
    return base + urllib.parse.urlencode(kw)

print(url("hej.com/search?", name="nils", lastname="hermansson", age="25"))