import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


# ✅ Alphabetical order — matches flow_from_directory subfolder indexing:
#    0 → BACTERIAL_PNEUMONIA
#    1 → NORMAL
#    2 → VIRAL_PNEUMONIA
CLASS_NAMES = [
    'BACTERIAL_PNEUMONIA',
    'NORMAL',
    'VIRAL_PNEUMONIA'
]

CLASS_LABELS = {
    'BACTERIAL_PNEUMONIA': 'Bacterial Pneumonia',
    'NORMAL':              'Normal',
    'VIRAL_PNEUMONIA':     'Viral Pneumonia'
}

CLASS_INFO = {
    'BACTERIAL_PNEUMONIA': 'Bacterial pneumonia is a lung infection caused by bacteria, often showing localized opacity/consolidation on chest X-ray. Requires antibiotic treatment.',
    'NORMAL':              'No signs of pneumonia detected. Lung fields appear clear on this chest X-ray.',
    'VIRAL_PNEUMONIA':     'Viral pneumonia is a lung infection caused by a virus, typically showing more diffuse, bilateral patterns on chest X-ray than bacterial pneumonia.'
}


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load trained model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        # Preprocess image — same rescale as training generator
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        # Predict
        predictions = model.predict(test_image)
        class_idx = int(np.argmax(predictions, axis=1)[0])
        confidence = float(np.max(predictions))

        class_key = CLASS_NAMES[class_idx]
        label = CLASS_LABELS[class_key]
        info = CLASS_INFO[class_key]

        print(f"Predicted: {class_key} | Label: {label} | Confidence: {confidence:.2%}")

        return [{
            "image":      label,
            "class_key":  class_key,
            "confidence": f"{confidence * 100:.2f}",
            "info":       info
        }]