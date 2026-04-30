import pytest
from doc_manager import DocumentManager

# ==========================================
# Тести для upload_document
# ==========================================

def test_upload_valid_pdf():
    # Arrange (Підготовка)
    manager = DocumentManager()
    # Act (Дія)
    result = manager.upload_document("report.pdf", 5.0)
    # Assert (Перевірка)
    assert result == "Файл успішно завантажено" # EP: позитивний

def test_upload_invalid_extension():
    # Arrange
    manager = DocumentManager()
    # Act & Assert
    with pytest.raises(ValueError, match="Дозволено лише формат PDF"):
        manager.upload_document("image.jpg", 2.0) # EP: негативний

def test_upload_zero_size():
    # Arrange
    manager = DocumentManager()
    # Act & Assert
    with pytest.raises(ValueError, match="Розмір файлу не може бути 0 або менше"):
        manager.upload_document("empty.pdf", 0.0) # BVA: межа 0 (негативний)

def test_upload_max_allowed_size():
    # Arrange
    manager = DocumentManager()
    # Act
    result = manager.upload_document("big.pdf", 15.0)
    # Assert
    assert result == "Файл успішно завантажено" # BVA: межа 15.0 (позитивний)

def test_upload_exceed_max_size():
    # Arrange
    manager = DocumentManager()
    # Act & Assert
    with pytest.raises(ValueError, match="Файл занадто великий. Максимум 15 МБ"):
        manager.upload_document("huge.pdf", 15.1) # BVA: межа 15.1 (негативний)

# ==========================================
# Тести для assign_schema
# ==========================================

def test_assign_valid_schema():
    # Arrange
    manager = DocumentManager()
    # Act
    result = manager.assign_schema(101, "invoice")
    # Assert
    assert result is True # EP: позитивний (допустимий клас)

def test_assign_invalid_schema():
    # Arrange
    manager = DocumentManager()
    # Act & Assert
    with pytest.raises(ValueError, match="Невідома схема: unknown"):
        manager.assign_schema(101, "unknown") # EP: негативний (недопустимий клас)

# ==========================================
# Тести для calculate_processing_time
# ==========================================

def test_calc_time_zero_pages():
    # Arrange
    manager = DocumentManager()
    # Act & Assert
    with pytest.raises(ValueError, match="Кількість сторінок має бути більше 0"):
        manager.calculate_processing_time(0) # BVA: межа 0 (негативний)

def test_calc_time_small_doc():
    # Arrange
    manager = DocumentManager()
    # Act
    time = manager.calculate_processing_time(5)
    # Assert
    assert time == 7.5 # EP: позитивний (5 * 1.5)

def test_calc_time_exactly_ten_pages():
    # Arrange
    manager = DocumentManager()
    # Act
    time = manager.calculate_processing_time(10)
    # Assert
    assert time == 15.0 # BVA: межа 10 (позитивний)

def test_calc_time_large_doc():
    # Arrange
    manager = DocumentManager()
    # Act
    time = manager.calculate_processing_time(11)
    # Assert
    assert time == 18.0 # BVA: межа 11 (15.0 + 1.0 + 2.0) (позитивний)

def test_calc_time_very_large_doc():
    # Arrange
    manager = DocumentManager()
    # Act
    time = manager.calculate_processing_time(20)
    # Assert
    assert time == 27.0 # EP: позитивний (15.0 + 10.0 + 2.0)