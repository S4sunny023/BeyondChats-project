def find_citations(response_text, sources):
    citations = []
    for source in sources:
        if source['context'] in response_text:
            citations.append(source)
    return citations

def process_data(data):
    processed_results = []
    for item in data:
        if isinstance(item, dict) and 'response' in item:
            response_text = item.get('response', '')  # Use .get() to handle missing keys gracefully
            sources = item.get('sources', [])
            citations = find_citations(response_text, sources)
            processed_results.append({
                'response': response_text,
                'citations': citations
            })
        else:
            print(f"Skipping invalid item: {item}")
    return processed_results
