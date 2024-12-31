from tensorflow.keras import layers, models, regularizers

def build_model():
    model = models.Sequential([
        layers.Flatten(input_shape=(28, 28)),
        
        # First dense layer with batch normalization and dropout
        layers.Dense(256, activation='relu', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        
        # Second dense layer
        layers.Dense(128, activation='relu', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        
        # Output layer
        layers.Dense(10, activation='softmax')
    ])
    
    return model
