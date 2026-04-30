class DocumentManager:
    # список дозволених схем
    ALLOWED_SCHEMAS = ["invoice", "receipt", "contract"]

    def upload_document(self, file_name, file_size_mb):
        # перевірка формату та розміру файлу
        if not file_name.endswith(".pdf"):
            raise ValueError("Дозволено лише формат PDF")
        
        if file_size_mb <= 0:
            raise ValueError("Розмір файлу не може бути 0 або менше")
            
        if file_size_mb > 15.0:
            raise ValueError("Файл занадто великий. Максимум 15 МБ")
            
        return "Файл успішно завантажено"

    def assign_schema(self, doc_id, schema_type):
        if schema_type not in self.ALLOWED_SCHEMAS:
            raise ValueError(f"Невідома схема: {schema_type}")
            
        return True

    def calculate_processing_time(self, pages):
        # рахуємо приблизний час обробки
        if pages <= 0:
            raise ValueError("Кількість сторінок має бути більше 0")
            
        if pages <= 10:
            return round(pages * 1.5, 2)
        else:
            extra_pages = pages - 10
            return round(15.0 + (extra_pages * 1.0) + 2.0, 2)