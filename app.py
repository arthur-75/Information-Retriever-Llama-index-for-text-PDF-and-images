from flask import Flask, render_template, request

# Import necessary modules and classes
from llama_index.schema import ImageNode
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index import ServiceContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.indices.multi_modal.base import MultiModalVectorStoreIndex
import qdrant_client

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create a local Qdrant vector store
qdrant_client = qdrant_client.QdrantClient(path="qdrant_db")

text_store = QdrantVectorStore(
    client=qdrant_client, collection_name="text_collection"
)
image_store = QdrantVectorStore(
    client=qdrant_client, collection_name="image_collection"
)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
service_context = ServiceContext.from_defaults(chunk_size=1024, llm=None, embed_model=embed_model)
indexx = MultiModalVectorStoreIndex.from_vector_store(vector_store=text_store, service_context=service_context, image_vector_store=image_store)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        test_query = request.form.get('text')
        retriever = indexx.as_retriever(similarity_top_k=3, image_similarity_top_k=3)
        retrieval_results = retriever.retrieve(test_query)

        # Process retrieval results
        results_info = []
        for res_node in retrieval_results:
            if isinstance(res_node.node, ImageNode):
                image_info = {
                    'type': 'image',
                    'file_path': res_node.node.metadata.get('file_path', ''),
                    'score': res_node.score
                }
                results_info.append(image_info)
            else:
                text_content = res_node.text[:150]+" ..."#res_node.node.metadata.get('text_content', 'No text content available')
                text_info = {
                    'type': 'text',
                    'file_path': res_node.node.metadata.get('file_path', ''),
                    'score': res_node.score,
                    'text_content': text_content
                }
                results_info.append(text_info)
        
        return render_template('index.html', test_query=test_query, results_info=results_info)

    except Exception as e:
        # Handle errors gracefully
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
