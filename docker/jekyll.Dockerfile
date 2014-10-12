FROM ubuntu:14.04

MAINTAINER yourname

RUN apt-get update
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get -y install make g++ python git ruby ruby-dev

#Do not forget to install your markdown converter gem  
#( e.g. kramdown or rdisount)
RUN gem install bundler therubyracer jekyll

#Download your jekyll website repository from github
RUN git clone https://github.com/username/websiterepository

#Set the default workdir
WORKDIR /websiterepository

#Expose the default port from jekyll
EXPOSE 4000

#Set the default command to execute at launch
CMD ["jekyll", "serve"]
