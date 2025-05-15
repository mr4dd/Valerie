from transformers import BartTokenizer, BartConditionalGeneration

class Summarizer:
    def __init__(self, text):
        self.text = text
    
        model_name = "facebook/bart-large-cnn"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartConditionalGeneration.from_pretrained(model_name)
    
    def generate_summary(original):
        inputs = tokenizer.encode("summarize: "+ original, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=100, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        return summary

    def summarize_single(self):
        return generate_summary(self.text)

    def summarize_batch(self): 
        summaries = []
        for sample in self.text:
            summaries.append(generate_summary(sample))

        return summaries
