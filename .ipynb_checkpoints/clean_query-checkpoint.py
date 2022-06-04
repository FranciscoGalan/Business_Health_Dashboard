def clean_query(query):
    clean = query.replace('\n', " ").replace("  ", " ").replace(" S", "S").replace('\t', '')
    return clean