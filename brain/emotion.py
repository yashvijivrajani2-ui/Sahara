from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def detect_emotion(text):
    text_lower = text.lower()

    # Angry
    angry_words = [
        "angry", "furious", "rage", "mad", "hate",
        "annoyed", "irritated", "frustrated", "pissed"
    ]

    # Sad
    sad_words = [
        "sad", "cry", "crying", "depressed", "heartbroken",
        "unhappy", "hurt", "lonely", "miserable"
    ]

    # Happy
    happy_words = [
        "happy", "excited", "great", "amazing", "wonderful",
        "joy", "glad", "love", "good"
    ]

    # Scared
    scared_words = [
        "scared", "afraid", "fear", "terrified",
        "frightened", "nervous", "worried"
    ]

    # Check clear emotion words first
    if any(word in text_lower for word in angry_words):
        return "angry"

    if any(word in text_lower for word in sad_words):
        return "sad"

    if any(word in text_lower for word in scared_words):
        return "scared"

    if any(word in text_lower for word in happy_words):
        return "happy"

    # VADER fallback
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.5:
        return "happy"
    elif score <= -0.5:
        return "sad"
    else:
        return "neutral"