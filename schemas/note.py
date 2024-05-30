

def noteEntity(item) -> dict:
    return {
        "title": item["title"],
        "desc": item["desc"],
        "urgent": item["urgent"],
    }


def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]
