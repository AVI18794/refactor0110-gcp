#DOWNLOAD THE BASE PYTHON VERSION. Change the part with the python version name after the colon: Eg:- python:3.x
FROM python:3.10-slim



#EXPOSE THE PORT:- FOR GOOGLE CLOUD PORT 8080 WORKS SO TRY THAT. Change the port number using port number in place of 8080
EXPOSE 8080

#SET THE WORKING DIRECTORY.Eg:- /app here the working directory is app

WORKDIR /app
# You can change the working directory to root as / 


#INSTALL GIT ON THE DOCKER SO THAT WE CAN CLONE THE REMOTE REPO
#RUN THIS ONLY WHEN YOU WANT TO CLONE THE REMOTE REPO INTO YOUR CONTAINER.
#This step is optional and it will install the git. If not needed comment this part and try building the image again
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

#CLONE YOUR CODE THAT LIVES IN REMOTE REPO TO WORKDIR
#RUN THE BELOW CODE IF YOUR CODE LIVES IN REMOTE REPO TO CLONE IT FROM THERE
#Pass the repo name after git clone to clone the repo to the working directory.

# RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN git clone <git-repo-link> .


#IF YOUR CODE LIVES IN THE SAME DIRECTORY AS DOCKERFILE THEN COPY ALL YOUR ALL FILES FROM YOUR SERVER TO CONTAINER including app.py and requirement.txt using following command.
# COPY . .

#RUN THE COMMAND TO INSTALL THE LIBRARIES MENTIONED IN REQUIREMENT.TXT
RUN pip3 install -r requirements.txt

#An ENTRYPOINT allows you to configure a container
#that will run as an executable. 
#Here, it also contains the entire streamlit run command 
#for your app, so you don’t have to call it from the command line:

#Change the entrypoint to the filename which you want to start from Eg:in place of streamlit_app.py pass in the filename from which the execution starts.
# ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]