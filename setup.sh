#!/usr/bin/env sh

makePassword(){
    # function to generate a random password
    length=$1
    type=$2

    if [[ "$type" = "digits_and_numbers" ]];
    then
    allowed_characters='A-Za-z0-9'
    else
    allowed_characters='A-Za-z0-9!"#%'\''()*+,-.:;<=>?@[\]^_`{|}~'
    fi

    echo `LC_ALL=C tr -dc "$allowed_characters" </dev/urandom | head -c $length ; echo`
}

replace_string_in_file() {
    # utility to run sed command
    old_string=$1
    replacement=$2
    input_file=$3

    sed -i '' "s/$old_string/$replacement/g" "${input_file}"
}

password_length=47
SUPER_USER_EMAIL='admin@example.com'
SUPER_USERNAME='admin'
SUPER_PASSWORD=$(makePassword $password_length)
DJANGO_SECRET_KEY=$(makePassword $password_length)

FRONT_END_PORT='8080'

RABBITMQ_HOST='rabbitmqhost'
RABBITMQ_DEFAULT_USER='rabit_username'
RABBITMQ_DEFAULT_PASS=$(makePassword $password_length digits_and_numbers)

POSTGRES_DB='mydatabase'
POSTGRES_USER='db_username'
POSTGRES_PASSWORD=$(makePassword $password_length)

# login credentials
replace_string_in_file "<SUPER_USER_EMAIL>" "$SUPER_USER_EMAIL" ./envs/django.env
replace_string_in_file "<SUPER_USERNAME>" "$SUPER_USERNAME" ./envs/django.env
replace_string_in_file "<SUPER_PASSWORD>" "$SUPER_PASSWORD" ./envs/django.env
replace_string_in_file "<DJANGO_SECRET_KEY>" "$DJANGO_SECRET_KEY" ./envs/django.env

# rabbitmq config
replace_string_in_file "<RABBITMQ_HOST>" "$RABBITMQ_HOST" ./envs/django.env
replace_string_in_file "<RABBITMQ_HOST>" "$RABBITMQ_HOST" ./.env
replace_string_in_file "<RABBITMQ_DEFAULT_USER>" "$RABBITMQ_DEFAULT_USER" ./envs/rabbit.env
replace_string_in_file "<RABBITMQ_DEFAULT_PASS>" "$RABBITMQ_DEFAULT_PASS" ./envs/rabbit.env

# Nginx port
replace_string_in_file "<FRONT_END_PORT>" "$FRONT_END_PORT" ./envs/django.env
replace_string_in_file "<FRONT_END_PORT>" "$FRONT_END_PORT" ./.env

# database
replace_string_in_file "<POSTGRES_DB>" "$POSTGRES_DB" ./envs/db.env
replace_string_in_file "<POSTGRES_USER>" "$POSTGRES_USER" ./envs/db.env
replace_string_in_file "<POSTGRES_PASSWORD>" "$POSTGRES_PASSWORD" ./envs/db.env
