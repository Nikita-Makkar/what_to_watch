
# Новый импорт:
from datetime import datetime
from random import randrange

# Импортируем функцию render_template():
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


# @app.route('/')
# def index_view():
#     # Определяется количество мнений в базе данных:
#     quantity = Opinion.query.count()
#     # Если мнений нет...
#     if not quantity:
#         # ...то возвращается сообщение:
#         return 'В базе данных мнений о фильмах нет.'
#     # Иначе выбирается случайное число в диапазоне от 0 до quantity...
#     offset_value = randrange(quantity)
#     # ...и определяется случайный объект:
#     opinion = Opinion.query.offset(offset_value).first()
#     return opinion.text
@app.route('/')
def index_view():
    quantity = Opinion.query.count()
    if not quantity:
        return 'В базе данных мнений о фильмах нет.'
    offset_value = randrange(quantity)
    # Извлекаем все записи, пропуская первые offset_value записей,
    # и берём первую запись из получившегося набора:
    opinion = Opinion.query.offset(offset_value).first()
    # Передаём в шаблон весь объект opinion:
    return render_template('index.html', opinion=opinion)

@app.route('/add')
def add_opinion_view():
    return 'Страница в разработке!'


if __name__ == '__main__':
    app.run()