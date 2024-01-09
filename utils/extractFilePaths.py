def extract_distinct_file_paths(documents):
    file_paths = set()
    metadata_present = False

    for doc in documents:
        if hasattr(doc, 'metadata') and isinstance(doc.metadata, dict) and "file_path" in doc.metadata:
            file_paths.add(doc.metadata["file_path"])
            metadata_present = True

    return file_paths, metadata_present