from app.utils.external_apis import create_embeddings
from app.dependencies.database import vector_database
import uuid
import vecs


async def create_transcription_embeddings(text: str):
    embeddings_dict = create_embeddings(text, "document")
    return embeddings_dict


async def create_user_embeddings(text: str):
    embeddings_dict = create_embeddings(text, "query")
    query_embeddings = embeddings_dict["embeddings"][0]["embedding"]
    return query_embeddings


async def retrieve_important_passages(query_embeddings, podcast_id):
    docs = vector_database("podcasts")
    similar_embeddings = docs.query(
        query_embeddings,
        limit=3,
        filters={"podcast_id": {"$eq": {podcast_id}}},
    )

    top_results = docs.fetch(similar_embeddings)

    top_passages = [result[2]["text"] for result in top_results]

    return top_passages


async def insert_embeddings(embeddings_dict, metadata):
    docs = vector_database("podcasts")
    records = []

    embeddings = embeddings_dict["embeddings"]

    for embedding in embeddings:
        vector_id = str(uuid.uuid4())
        fetch_id = vector_id
        while vector_id == fetch_id:
            try:
                fetch = docs.fetch([vector_id])
                fetch_id = fetch[0][0]
            except IndexError:
                fetch_id = None
            else:
                vector_id = str(uuid.uuid4())
        records.append(
            (
                vector_id,
                embedding["embedding"],
                {
                    "podcast_id": metadata["podcast_id"],
                    "user_id": metadata["user_id"],
                    "chunk_id": embedding["index"],
                    "text": embeddings_dict["text"][embedding["index"]],
                },
            )
        )

    docs.upsert(records=records)
    docs.create_index(
        measure=vecs.IndexMeasure.cosine_distance,
        method=vecs.IndexMethod.hnsw,
    )
    return True
