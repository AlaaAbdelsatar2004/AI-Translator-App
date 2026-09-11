import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# تحميل النموذج والـ Tokenizer مرة واحدة عند تشغيل البرنامج
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate_text(text, source_lang_code, target_lang_code):
    """
    دالة تأخذ النص وكود اللغة المصدر وكود اللغة الهدف وتعيد النص المترجم
    """
    try:
        # تحديد لغة المصدر للـ Tokenizer
        tokenizer.src_lang = source_lang_code
        
        # تحويل النص إلى أرقام يفهمها النموذج
        inputs = tokenizer(text, return_tensors="pt")
        
        # الحصول على الـ ID الخاص بلغة الهدف لإجبار النموذج على الترجمة لها
        forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang_code)
        
        # توليد الترجمة
        with torch.no_grad(): # لتسريع العملية وتقليل استهلاك الذاكرة
            generated_tokens = model.generate(
                **inputs,
                forced_bos_token_id=forced_bos_token_id,
                max_length=200
            )
        
        # فك تشفير الأرقام إلى نص مرة أخرى
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return translated_text
    except Exception as e:
        return f"حدث خطأ أثناء الترجمة: {str(e)}"