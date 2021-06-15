class SliceList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        print(key)
        if isinstance(key, int):
            return super().__getitem__(key)
        else:
            return [super(SliceList, self).__getitem__(k) for k in key]

a = SliceList([1, 2, 3])

print(a[0])
print(a[0, 2])