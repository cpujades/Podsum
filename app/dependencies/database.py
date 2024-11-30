from app.core.config import config
import vecs

DB_CONNECTION = config.DB_CONNECTION


def vector_database(collection_name):
    vx = vecs.create_client(DB_CONNECTION)

    docs = vx.get_or_create_collection(collection_name, dimension=1024)

    return docs
