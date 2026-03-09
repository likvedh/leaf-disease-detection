import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'dataset')


# dataset paths should point to processed split created by dataset/prepare.py
# Training utility functions are implemented below.

def build_model(num_classes, freeze_base=True):
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    if freeze_base:
        for layer in base_model.layers:
            layer.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    return model


def get_generators(data_dir, img_size=(224,224), batch_size=32):
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.0
    )
    val_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        os.path.join(data_dir, 'train'),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical'
    )
    val_generator = val_datagen.flow_from_directory(
        os.path.join(data_dir, 'val'),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical'
    )
    test_generator = val_datagen.flow_from_directory(
        os.path.join(data_dir, 'test'),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )
    return train_generator, val_generator, test_generator


def main():
    # load dataset generators
    num_classes = 11  # update if classes change
    train_gen, val_gen, test_gen = get_generators(os.path.join(BASE_DIR, 'dataset', 'processed'))

    model = build_model(num_classes=num_classes, freeze_base=True)
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-4),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # train head first
    model.fit(
        train_gen,
        epochs=5,
        validation_data=val_gen
    )

    # fine-tune last layers
    for layer in model.layers[-20:]:
        layer.trainable = True
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(
        train_gen,
        epochs=10,
        validation_data=val_gen
    )

    # save model
    # save class indices for later mapping
    import json
    class_indices = train_gen.class_indices
    with open(os.path.join(BASE_DIR, 'class_indices.json'), 'w') as f:
        json.dump(class_indices, f)
    # also attach class_names attribute to the model for convenience
    class_names = [k for k, v in sorted(class_indices.items(), key=lambda x: x[1])]
    model.class_names = class_names
    model.save(os.path.join(BASE_DIR, 'model.h5'))
    print("Model saved to model.h5 and class_indices.json")

if __name__ == '__main__':
    main()


def main():
    # placeholder main function
    print("Training script placeholder")

if __name__ == '__main__':
    main()
