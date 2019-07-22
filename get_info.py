import re


class GetInfo(object):
    @staticmethod
    def info():
        first_name = str(input("苗字を入力してください(ガナの方が識別率高いです):"))
        first_name = GetInfo.formats(first_name)
        last_name = str(input("名前を入力してください(ガナの方が識別率高いです):"))
        last_name = GetInfo.formats(last_name)
        domain = str(input("ドメインを入力してください:"))
        return first_name, last_name, domain

    @staticmethod
    def formats(key_world):
        key_world = key_world.strip()
        key_world = re.sub(r'[^\w\s]', '', key_world)
        from pykakasi import kakasi
        kakasi = kakasi()
        kakasi.setMode('H', 'a')
        kakasi.setMode('K', 'a')
        kakasi.setMode('J', 'a')
        conv = kakasi.getConverter()
        key_world = conv.do(key_world)
        return key_world


if __name__ == "__main__":
   g = GetInfo()
   first_name, last_name, domain = g.info()
   print(first_name, last_name, domain)


