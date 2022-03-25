import connexion
from bookshelf import get_user_groups

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('api.yaml')
app.app.before_request(get_user_groups)


if __name__ == '__main__':
    app.run(port=8080)
