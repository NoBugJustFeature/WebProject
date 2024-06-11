<H1>Installation and launch</H1>

> git clone https://github.com/NoBugJustFeature/WebProject.git

<H3>Create .env file using .env.example</H3>

To create SECRET_KEY you can use python the following code in the Python shell

> import secrets
>
> print(secrets.token_hex(24))

<H3>Create environment, install dependens and run server</H3>
 
> python -m venv env
> 
> env/Scripts/activate
>
> pip install -r WebProject/requirements.txt
>
> python WebProject/web/manage.py migrate
>
> python WebProject/web/manage.py runserver
