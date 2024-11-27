# Feedback Module: Generates textual feedback for the learner
def generate_feedback(grammar_errors, vocabulary_feedback, evaluation_score):
    """
    Summarizes analysis results into actionable feedback for the learner.
    """
    feedback = f"Grammar Errors: {', '.join(grammar_errors)}\n"
    feedback += f"Vocabulary Suggestions: {', '.join(vocabulary_feedback['missing'])}\n"
    feedback += f"Evaluation Score: {evaluation_score:.2f}"
    return feedback
