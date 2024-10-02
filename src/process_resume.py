from src.models import TogetherModel
from src.prompts import preprocessing_prompt

model = TogetherModel()


def preprocess_resume(text):
    prompt = preprocessing_prompt.format(raw_resume_text=text)
    return model.generate(prompt)