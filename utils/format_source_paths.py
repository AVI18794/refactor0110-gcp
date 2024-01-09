def format_source_paths(file_paths):
    # Format each file path with "Source" in bold and the entire string in italics
    formatted_paths = [f"*__Source:__ [{path}]*" for path in file_paths]
    # Join multiple sources with a comma
    sources_string = ', '.join(formatted_paths)
    return sources_string