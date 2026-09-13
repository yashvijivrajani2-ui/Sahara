def generate_response(emotion):

    responses = {
        "happy": "I'm glad you're feeling happy!",
        "sad": "I'm here with you. You don't have to handle everything alone.",
        "upset": "I understand. Take a moment and breathe. I'm listening.",
        "neutral": "I'm here. Tell me what's on your mind.",
        "angry": "Take a deep breath and let's talk about it ."
    }

    return responses.get(emotion, "I'm listening.")