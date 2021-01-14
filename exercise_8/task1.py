class defaultDict(dict):

    def __init__(self, default):
        self.default = default

    def __getitem__(self, k):
        if k in self:
            return super().__getitem__(k)
        else: 
            return self.default

dd = defaultDict('default value')

print(dd["key"])