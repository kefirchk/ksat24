from app.database import FormData, db


class Repository:
    def get_all(self):
        results = FormData.query.all()
        return results

    def add_one(self, data):
        form_data = FormData(data=data)
        db.session.add(form_data)
        db.session.commit()
