import datetime

class Note:
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    def __init__(self, id, title, body, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = (
            datetime.datetime.strptime(created_at, Note.DATE_FORMAT)
            if created_at
            else datetime.datetime.now()
        )
        self.updated_at = (
            datetime.datetime.strptime(updated_at, Note.DATE_FORMAT)
            if updated_at
            else self.created_at
        )

    def update(self, title=None, body=None):
        self.title = title or self.title
        self.body = body or self.body
        self.updated_at = datetime.datetime.now()