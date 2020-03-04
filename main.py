from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def mainPage():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def indexPage():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotionPage():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return '</br>'.join(text)


@app.route('/image_mars')
def marsImage():
    return render_template('marsImage.html')


@app.route('/promotion_image')
def promotion_image1():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return """<!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <title>Колонизация</title>
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                crossorigin="anonymous">
                <link rel="stylesheet" href={}>
              </head>
              <body>
                <h1>Жди нас, Марс!</h1>
                <img src="{}" alt="Марс">
                <div class="alert alert-dark" role="alert">
                  {}
                </div>
                <div class="alert alert-success" role="alert">
                  {}
                </div>
                <div class="alert alert-secondary" role="alert">
                  {}
                </div>
                <div class="alert alert-warning" role="alert">
                  {}
                </div>
                <div class="alert alert-danger" role="alert">
                  {}
                </div>
              </body>
            </html>""".format(url_for('static', filename='css/style.css'), url_for('static', filename='img/mars.jpg'),
                              *text)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <title>Колонизация</title>
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                crossorigin="anonymous">
              </head>
              
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                <h2>Эта планета близка к Земле;</h2>

                <div class="alert alert-success" role="alert">
                  На ней много необходимых ресурсов;
                </div>
                <div class="alert alert-secondary" role="alert">
                  На ней есть вода и атмосфера;
                </div>
                <div class="alert alert-warning" role="alert">
                  На ней есть небольшое магнитное поле;
                </div>
                <div class="alert alert-danger" role="alert">
                  Наконец, она просто красива!
                </div>
            </body>
            </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <title>Колонизация</title>
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                crossorigin="anonymous">
              </head>
            <body>
                <h1>Результаты отбора</h1>
                <h2>Претендента на участие в миссии {nickname}:</h2>
                <div class='alert alert-success'>Поздравляем!
                 Ваш рейтинг после {level} этапа отбора</div>
                <h4>составляет {rating}!</h4>
                <div class='alert alert-warning'>Желаем удачи!</div>
            </body>
            </html>
            '''


@app.route('/load_photo', methods=['GET', ])
def loadPhoto():
    return f'''
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <title>Отбор астронавтов</title>
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                crossorigin="anonymous">
                <link rel="stylesheet" href={url_for('static', filename='css/loadPhoto.css')}>
              </head>
            <body>
                <h1>Загрузка фотографии</h1>
                <h2>для участия в миссии</h2>
            <form method="post" enctype="multipart/form-data" class='login_form'>
               <div class="form-group">
                    <label for="photo">Выберите файл</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
                
            </form>
            </body>
            '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
