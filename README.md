# FastAPI Project  - Real Estate Agency - Advertisement for properties

FastAPI project that is based on a MySQL database and consists of endpoints for a real estate agency.
These endpoints would allow the agency and its workers to post and approve ads, among other functionalities.
The project would enable property owners to register and offer their properties to the agency,
and potential buyers or renters to view available properties and add them to their wishlist.
The advertisements would contain detailed information about the property, the owner, and the price,
and filtering options would be available for ads.

## For settings and username and passwords
USER_SECRET=secret123
ALGORITHM=HS256
U bazi su iste vrednosti za sifre kao sto su korisnicka imena.

## Quick Guide

### Type of Property
Represents the various types of properties that are available.

### Type of Feature
Represents the different features that properties can have, including an optional value parameter for features that require additional information.

### Type of Property has Type of Feature
Specifies which types of properties can have particular features.

### Property
Describes a specific property and its attributes, including a foreign key from the Type of Property table.

### Property has Feature
Link features to specific property and records additional values for features that require them.

### Users, Clients, Employees
In order to carry out certain actions, such as creating advertisements or accessing advertising metrics, users and clients must be registered.
Users can also follow other advertisements, while employees are responsible for managing property types and features, as well as approving new ads.

### Advertisement
Comprises a property, client ID, and assigned employee, along with information about price, admission date, and status.

## Installation

### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```
### Activate Virtual environment
Open terminal and navigate to project directory, then run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |

### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```
### Database
Start MySQL server and execute all commands in **_init_db/init_db.sql_**

### Environment variables
1. Create new file **_.env_**
2. Copy all consts from **env-template** to **_.env_**
3. Assign values to const in .env file


## Run server
From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
