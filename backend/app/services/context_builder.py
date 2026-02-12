def build_context(chunks, max_chars=2000):
    context = ""
    for c in chunks:
        if len(context) + len(c) > max_chars:
            break
        context += c + "\n"
    return context
