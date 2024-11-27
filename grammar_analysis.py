# Grammar Analysis Module: Detects grammatical errors using mock logic
import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

def analyze_grammar(preprocessed_text):
    """
    Uses spaCy to identify grammatical errors in the input.
    """
    doc = nlp(" ".join(preprocessed_text))
    grammar_errors = []
    for token in doc:
        # Mock logic: Treat words tagged as 'X' as errors
        if token.pos_ == "X":
            grammar_errors.append(f"Grammar issue with '{token.text}'")
    return grammar_errors
