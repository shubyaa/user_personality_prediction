from transformers import pipeline

# Creating the Q&A pipeline
nlp = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')

# description_text = "Hello, my name is Adarsh. I’m Katherine’s husband, it’s a pleasure to meet you. Katherine was telling me about how I absolutely had to come down to Nantucket and meet all of her friends so here I am! I’m so glad you decided to host a beach party, I love snorkelling. The party was fantastic. It was very kind of you to drive my wife and I to the beach today, we had lots of fun. Your cooking is delicious! Please tell me the recipe you used for your lasagne, Katherine says it’s a secret but I’m sure you wouldn’t mind sharing, right? Anyway, tell me a bit about yourself. How did you and Katherine meet?"

def answer_questions(question_text, context_text): 
    # Convert this to a dictionary
    question_set = {
                'question':question_text, 
                'context':context_text
               }
    # Run it through the NLP pipeline
    results = nlp(question_set)
    
    return results['answer']


# final_result = answer_questions('What does Katherine love?', description_text)

# print(final_result)