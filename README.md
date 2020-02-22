hmlet

## Installation



1. Clone this repository: `git clone git@github.com:ArchitW/hmlet.git`.
2. cd into `hmlet` and run `pip3 install -r requirements.txt `
3. to start local server `python3 src/manage.py runserver` 
4. I have intentionally added database (passwords of admin and user will be provided via email) or else `python3 src/manage.py  makemigrations` and  `python3 src/manage.py  migrate` and `python3 src/manage.py  createsuperuser`
5. I have *not* written standard tests, but mocks can be seen under `scripts/` folder.
6. Please import `json` file from `API_insomnia` in your insomnia application. [download insomnia](https://insomnia.rest/)

## API Endpoints and Admin
- [Admin](https://hmlet.herokuapp.com/admin/)
- [Photo API](https://hmlet.herokuapp.com/api/photo/)
- [Login](https://hmlet.herokuapp.com/api/auth/jwt/)
- [Register](https://hmlet.herokuapp.com/api/auth/register/)

Please find rest of the endpoints in `API_insomnia's JSON file.`