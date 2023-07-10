FROM python:3.10.4
COPY . /test-project
WORKDIR /test-project
RUN pip install pipenv
RUN pipenv install
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -  \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable
#RUN pipenv run behave -f allure_behave.formatter:AllureFormatter -o result-folder bdd/login.feature
#COPY . result-folder-docker
