from flask import render_template
import connexion


@app.route('/')
def home():
    return render_template('home.html')


def main():
    app = connexion.App(__name__, specification_dir='./')
    app.add_api('swagger.yml')
    app.run(host='0.0.0.0', port=5000, debug=True)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    main()
