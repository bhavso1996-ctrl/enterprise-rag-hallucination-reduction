This project builds a document-based question answering system using enterprise policy documents.

When a user asks a question, the system first retrieves relevant sections from the policy documents using similarity search. A language model then generates an answer using only the retrieved document content.

If the documents do not contain enough information to answer the question, the system responds with “I don’t know” instead of generating an unsupported answer. This helps reduce incorrect or hallucinated responses.
