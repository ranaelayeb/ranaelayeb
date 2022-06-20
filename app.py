import pickle 
train_text_emb, val_text_emb, test_text_emb = pickle.load(open(r'C:\features-20220411T102232Z-001\features\text_emotion.pkl', 'rb'))
train_audio_emb, val_audio_emb, test_audio_emb = pickle.load(open(r'C:\features-20220411T102232Z-001\features\audio_emotion.pkl', 'rb'))
