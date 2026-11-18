# Lab 5 – Foundation Models and Engineering Maintenance Assistant

## Problem

The engineering problem addressed in this lab is to develop a maintenance assistant that can answer questions about common mechanical equipment problems using pretrained foundation models and Retrieval-Augmented Generation (RAG).

The assistant uses information from a maintenance knowledge base to help identify possible equipment problems and provide maintenance recommendations.

## Foundation Models

Three pretrained models were used in this laboratory:

- **CLIP ViT-B/32:** Used for zero-shot image classification of steel surface defects without additional training.
- **SmolLM2-360M-Instruct:** A small language model used to generate answers to engineering questions.
- **all-MiniLM-L6-v2:** An embedding model used to convert text into numerical vectors and retrieve relevant information based on similarity.

These models were already pretrained and did not require training from scratch.

## Knowledge Base

The knowledge base contains six maintenance passages covering:

- Bearing vibration and its possible causes.
- Bearing overheating and lubrication problems.
- Pump cavitation and its symptoms.
- Shaft misalignment and its effects.
- Belt slippage and its causes.
- Safety procedures before servicing rotating machinery.

The assistant uses these passages to retrieve relevant information before generating an answer.

## Architecture

The application uses Retrieval-Augmented Generation (RAG) to combine semantic search with a small language model.

**Question → Retrieval → LLM → Answer**

1. The user enters a maintenance question.
2. The embedding model converts the question into a numerical vector.
3. Semantic search retrieves the most relevant passages from the knowledge base.
4. The retrieved passages are provided to the language model.
5. The language model generates an answer using the retrieved information.

The original assistant retrieved two passages. For the project modification, this was increased to three passages to provide more information when answering maintenance questions.

## Evaluation

The modified assistant was evaluated using five supported questions and two unsupported questions.

| Question | Correct Retrieval? | Grounded Answer? | Problem Observed |
| :--- | :--- | :--- | :--- |
| 1. Why might a bearing overheat? | Yes | Yes | No Probelm |
| 2. What could cause shaft vibration? | Yes | Partial | It Confused causes and effects of vibration |
| 3. What are symptoms of cavitation? | Yes | Partial | It included unrelated bearing vibration informaation |
| 4. Why might a belt slip? | Yes | Yes | No problem |
| 5. What should I do before doing regular maintenance on shafts? | Yes | Yes | No problem |
| Unsupported 1 - What torque should I use to tighten the bearing housing bolts? | No | No | Random torque value of 5.5 kg-cm |
| Unsupported 2 - What kind of pump do I need for a Nuclear Plant? | No | No | Unverifiable answer |

The assistant retrieved relevant information for all five supported questions. However, some answers included incorrect or unrelated information.

For the two unsupported questions, the assistant generated answers even though the required information was not available in the knowledge base.

## Failure Cases

### Failure 1 - Unsupported information generated - Question 1 (Unsupported)
> The model generated a torque of 5.5 kg-cm, but the knowledge base doesn't contain this information. This failure was mainly caused by generation.

### Failure 2: Unrelated information included - Question 3
> The model retrieved the correct information about cavitation but also included unrelated bearing vibration information. This failure was mainly caused by generation.

## Engineering Conclusion

The RAG assistant can provide useful information for common mechanical maintenance problems by using a pretrained language model and a maintenance knowledge base.

However, I would not deploy it in an industrial environment without additional testing, more reliable maintenance information, and human verification. The assistant generated unsupported answers that could lead to equipment damage or safety risks.

The application can be used as a extra tool rather than replacing final engineering judgement.