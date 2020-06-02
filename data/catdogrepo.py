import sqlalchemy as db

'''pip install sqlalchemy'''
'''Может потребоваться pip install mysqlclient'''
'''Класс который инкапсулирует подключение к mysql базе и таблицам cat, dog и некоторых запросов'''
class CatDogRepository:
    def __init__(self, password, db_name, user='root', host='localhost'):
        con_string = 'mysql://%s:%s@%s/%s' % (user, password, host, db_name)
        print(con_string)
        engine = db.create_engine(con_string)
        self.connection = engine.connect()
        metadata = db.MetaData()     
        self.cat = db.Table('cat', metadata, autoload=True, autoload_with=engine)
        self.dog = db.Table('dog', metadata, autoload=True, autoload_with=engine)
    
    def getCatByBreed(self, breed):
        q = db.select([self.cat]).where(self.cat.columns.breed == breed)
        rp = self.connection.execute(q)
        r = rp.fetchone()
        return RecognitionOutputCat(r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8])

    def getDogByBreed(self, breed):
        q = db.select([self.dog]).where(self.dog.columns.breed == breed)
        rp = self.connection.execute(q)
        r = rp.fetchone()
        return RecognitionOutputDog(r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8])

class RecognitionOutputCat:
    def __init__(self, breed, weight, longevity_age, origin_country, wool_length, height, colors, history):
        self.breed = breed
        self.weight = weight
        self.longevity_age = longevity_age
        self.origin_country = origin_country
        self.wool_length = wool_length
        self.height = height
        self.colors = colors
        self.history = history
    


class RecognitionOutputDog:
    def __init__(self, breed, weight, longevity_age, origin_country, icf_group, height, colors, history):
        self.breed = breed
        self.weight = weight
        self.longevity_age = longevity_age
        self.origin_country = origin_country
        self.icf_group = icf_group
        self.height = height
        self.colors = colors
        self.history = history


# rep = CatDogRepository('pass', 'whatacatdog')
# cat = rep.getCatByBreed("abyssinian")
# print(cat.weight)