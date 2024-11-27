from app.utils.external_apis import create_embeddings
from app.dependencies.database import vector_database
import uuid
import vecs


async def create_transcription_embeddings(text: str):
    embeddings = create_embeddings(text, "document")
    return embeddings


async def insert_embeddings(embeddings, metadata):
    docs = vector_database("podcasts")
    records = []

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
                },
            )
        )

    docs.upsert(records=records)
    docs.create_index(
        measure=vecs.IndexMeasure.cosine_distance,
        method=vecs.IndexMethod.hnsw,
    )
    return True
