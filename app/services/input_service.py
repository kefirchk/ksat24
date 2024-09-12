from app.repositories import Repository


class InputService:
    def __init__(self):
        self.repo = Repository()

    def save(self, data):
        self.repo.add_one(data)

    def get_all(self):
        results = self.repo.get_all()
        return results
