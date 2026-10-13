import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_imports():
    import main
    import analytics
    import ai_analytics
    assert True