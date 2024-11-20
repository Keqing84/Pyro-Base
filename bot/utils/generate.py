import uuid

def sec_to_hum(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    return f"{days}d {hours}h {minutes}m {seconds}s"

class Encrypt:
    def token_text():
        text = str(uuid.uuid4()).split("-")[1:]
        return "_".join(text)
