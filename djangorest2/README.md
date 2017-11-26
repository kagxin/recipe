brew install mysql-connector-c
pip install mysqlclient==1.3.12

sudo vim /usr/local/bin/mysql_config

#libs="-L$pkglibdir"
#libs="$libs -l "
libs="-L$pkglibdir"
libs="$libs -lmysqlclient -lssl -lcrypto"

DATABASES = {
    'default': {
        'NAME': 'restdb',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '2012',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    }
}

CREATE DATABASE <dbname> CHARACTER SET utf8;


https://www.cnblogs.com/pluviophile/p/7860736.html