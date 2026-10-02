import src.lumache as lumache

def test_get_random_ingredients():
    result = lumache.get_random_ingredients()
    assert result == ["shells", "gorgonzola", "parsley"]

