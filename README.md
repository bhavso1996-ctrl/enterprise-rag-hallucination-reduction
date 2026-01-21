Enterprise RAG Hallucination Reduction

This project implements a document-based question answering system using enterprise policy documents. The main focus is to reduce hallucinated answers by ensuring that the system only responds using information that is actually present in the documents.

Overview

When a user asks a question, the system retrieves relevant sections from the policy documents using similarity-based search. The language model then generates an answer based only on the retrieved content. If the documents do not contain enough information to answer the question, the system responds with “I don’t know” instead of guessing.

This helps make the system safer and more reliable, especially for policy or compliance-related use cases.

Key Features

- Retrieval-based question answering over enterprise policy documents  
- Similarity search for relevant document sections  
- Answers generated only from retrieved context  
- Safe handling of out-of-scope questions  
- Console-based interaction for easier inspection and debugging  

Example Outputs

The repository includes screenshots showing example questions, retrieved results, and system responses. These examples demonstrate both correct policy-based answers and cases where the system intentionally refuses to answer when information is not available.

Why This Matters

In enterprise settings, incorrect or fabricated answers can cause confusion or compliance issues. This project shows how constraining a language model with retrieved document content can reduce hallucinations and improve answer reliability.

Tech Stack

- Python  
- Natural Language Processing  
- Vector similarity search  
- Retrieval-Augmented Generation  
- Large Language Models  


- This project focuses on backend logic and model behavior rather than a graphical user interface. Automatically generated files such as document chunks and embeddings are excluded from the repository to keep it clean and manageable.
