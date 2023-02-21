def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "siema" or p_message == "czesc":
        return "Elo Elo"

    if p_message == "obraź mi matkę":
        return "Twoja stara to gruba kurwa"