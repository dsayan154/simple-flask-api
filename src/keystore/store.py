import re
class KeyStore:
  def __init__(self) -> None:
      self.keyStore = {}
  def getitem(self, key: str):
    try:
      return self.keyStore[key]
    except KeyError as e:
      return e
  def setitem(self, newDict: dict):
    self.keyStore.update(newDict)
  def search(self, prefix='', suffix=''): 
    store = self.keyStore
    pattern = f'{prefix}.*{suffix}'
    filteredKeys = [ key for key in store.keys() if re.search(pattern, str(key)) != None ]
    return filteredKeys