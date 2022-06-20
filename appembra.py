embracenet = EmbraceNet(input_size_list=[33,33], embracement_size=256)
embraced_output = embracenet(input_list=[train_text_emb['0'],train_audio_emb['0']])
post = tf.keras.layers.Dense(units=10)
post(embraced_output)
