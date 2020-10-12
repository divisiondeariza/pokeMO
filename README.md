# pokeMO
> Gotta fetch 'em all!

Small REST api built in Django that serves a pokemon basic info (included evolutions and preevolutions).
This data has beed previously stored using a command that retrieves it from [pokeapi.co](https://pokeapi.co/)

## Instalation

Clone this repo:

```bash
git clone https://github.com/divisiondeariza/pokeMO.git
```

Then setup the database:
```bash
cd pokeMO.git
./manage.py makemigrations
./manage.py migrate
```

## Usage

Run the server locally:
```bash
./manage.py runserver
```
Then you will be able to use the endpoind in this way:

```http://127.0.0.1:8000/api/v1/pokemons/{pokemon-name}/```

## Retrieving and storing evolution chains from pokeapi

In order save new chains in the database you have to use the command:
```bash
./manage.py fetch_chain CHAIN_ID
```
