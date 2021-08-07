from pymongo import MongoClient

class MongoConnection:
    mongo_client = MongoClient()
    db_lusiadas = mongo_client.lusiadas_chants
    chants_collections = db_lusiadas.chant

    def insert_chant(self, chant):
        result_obj = self.chants_collections.insert_one(chant)
        return result_obj.acknowledged

    def get_chant(self, chant_number, stranza):
        chant = self.chants_collections.find_one({"chant_number": chant_number, "stranza": stranza})
        return chant



