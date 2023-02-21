def handle_response(wiadomosc) -> str:
    p_wiadomosc = wiadomosc.lower()

    if p_wiadomosc == "siema" or p_wiadomosc == "czesc":
        return "Elo Elo"
