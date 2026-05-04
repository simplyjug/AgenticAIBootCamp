# Day 5: Multimodal Generative AI

## Theory: Beyond Text

Multimodal AI handles text, images, audio, etc. Generative models can create or understand multiple modalities.

### Key Concepts
- **CLIP**: Matches text and images.
- **DALL-E**: Generates images from text.
- **Integration**: Combining modalities for richer AI.

### Applications
- Image captioning, generation, multimodal chat.

## Practical: Using CLIP for Image-Text Matching

### Setup
1. Install transformers: `pip install transformers`

### Hands-on Exercises
1. Load CLIP model.
2. Match text to images.

## Code Examples

### CLIP Example
```python
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image = Image.open("image.jpg")
inputs = processor(text=["a photo of a cat"], images=image, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
print(logits_per_image)
```

## Resources
- [CLIP Paper](https://arxiv.org/abs/2103.00020)

## Done When
- [ ] You understand multimodal benefits.
- [ ] You've run a CLIP example.