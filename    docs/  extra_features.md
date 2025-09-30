### Natural Language Processing, Speech Recognition, or Speech Synthesis
  
**Relevant to the theme**     
Our project predicts diseases based on symptoms. Right now, the system works with 0s and 1s. But in real life, people explain their symptoms in words or by speaking. NLP or speech can make the system more natural to use, since patients often describe symptoms in words or voice rather than selecting from binary options.

**Relevance to the proposed solution:**     
In the future, patients could just type or say their symptoms. The system would then turn those words into features the AI can understand. The AI would give a prediction, and with speech synthesis, it could even read out the results and advice—helpful for people who struggle with reading.

**Achievable**       
This can be done with tools that already exist:
* NLP: `spaCy`, `scikit-learn`       
* Speech Recognition: `speech_recognition library`         
* Speech Synthesis: `gTTS`, `pyttsx3`        

### Deep learning
**Relevant to the Theme**       
Right now, our project uses normal machine learning to predict diseases. Deep Learning can take this further, especially when working with bigger and more complex medical data like patient records, X-rays, or symptoms tracked over time.

**Proposed Solution**     
In the future, we could use:
* `Neural Networks (MLP)`: to find deeper patterns between symptoms and diseases.
* `CNNs`: for analysing medical images like X-rays or scans.
* `RNNs / LSTMs`: for time-series health data

**Achievable**     
This is possible with tools like `TensorFlow` and `PyTorch`, which are already widely used in medical AI


### Other Features: Chatbot / Softbot

**Relevant to the Theme**       
A chatbot is relevant because it can make the system more interactive. Instead of only selecting symptoms, patients could ask questions or get guidance in a conversational way.

**Proposed Solution**       
The chatbot could:
* Ask patients about their symptoms step by step.
* Give the predicted disease and advice.
* Share links to more medical info.

**Achievable**       
This is achievable with existing tools such as `Rasa`, `Dialogflow`, or simple rule-based Python chatbots. It can also be integrated with the trained model so predictions and advice are delivered through conversation.

