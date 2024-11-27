# Main Linguapal System
from preprocessing import preprocess
from grammar_analysis import analyze_grammar
from vocabulary_analysis import check_vocabulary
from evaluation_function import evaluate_progress
from feedback_generation import generate_feedback
from lesson_recommendation import recommend_lesson
from audio_input import read_audio_input
from audio_output import speak_feedback

def main():
    # Step 1: Input (text or audio)
    mode = input("Choose input mode (text/audio): ").strip().lower()
    if mode == "text":
        user_input = input("Enter your text: ")
    elif mode == "audio":
        user_input = read_audio_input()
        print(f"Recognized text: {user_input}")
    else:
        print("Invalid mode. Please choose 'text' or 'audio'.")
        return

    # Step 2: Preprocess input
    preprocessed_text = preprocess(user_input)

    # Step 3: Analyze grammar
    grammar_errors = analyze_grammar(preprocessed_text)

    # Step 4: Analyze vocabulary
    vocabulary_feedback = check_vocabulary(preprocessed_text)

    # Step 5: Evaluate progress
    evaluation_score = evaluate_progress(grammar_errors, vocabulary_feedback)

    # Step 6: Generate feedback
    feedback = generate_feedback(grammar_errors, vocabulary_feedback, evaluation_score)
    print("\nFeedback:\n", feedback)

    # Step 7: Recommend next lesson
    next_lesson = recommend_lesson(grammar_errors, vocabulary_feedback)
    print("\nRecommended Lesson:\n", next_lesson)

    # Optional: Provide audio feedback
    speak_feedback(feedback)

if __name__ == "__main__":
    main()
