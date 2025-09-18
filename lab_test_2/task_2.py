import string

def simple_tokenize(text):
    """
    Tokenizes the input text by splitting on spaces and stripping simple punctuation.
    Returns a list of lowercased tokens.
    """
    import re
    
    # Use regex to find all word tokens, handling punctuation properly
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def sentiment_score(text):
    """
    Computes the total sentiment score for the input text.
    Uses the following lexicon:
        good: +1
        great: +2
        bad: -1
    Tokenizes by spaces and strips simple punctuation.
    Returns the integer sentiment score.
    """
    lexicon = {
        'good': 1,
        'great': 2,
        'bad': -1
    }
    tokens = simple_tokenize(text)
    score = 0
    for token in tokens:
        score += lexicon.get(token, 0)
    return score

# --- AI-drafted tests ---

def _test_sentiment_score():
    cases = [
        # (input, expected_output)
        ("good product with bad packaging but great value", 2),
        ("bad bad bad", -3),
        ("good! great, bad.", 2),
        ("This is a good, great, and bad example.", 2),
        ("", 0),
        ("unknown words only", 0),
        ("good good great", 4),
        ("BAD", -1),
        ("Great! Good. Bad?", 2),
        ("good, bad, good, bad, great", 2),
        ("good.", 1),
        ("bad.", -1),
        ("great.", 2),
        ("good bad", 0),
        ("good! bad! great!", 2),
        ("good;bad:great", 2),
        ("good... bad... great...", 2),
        ("good product", 1),
        ("bad product", -1),
        ("great product", 2),
    ]
    for i, (inp, expected) in enumerate(cases, 1):
        result = sentiment_score(inp)
        assert result == expected, f"Test case {i} failed: input={inp!r}, expected={expected}, got={result}"
    print("All sentiment_score tests passed.")

if __name__ == "__main__":
    _test_sentiment_score()

