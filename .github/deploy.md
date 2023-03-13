
## Deploy

SlackBot -> AWS Lightsail

* issue : container deploy fail "exec format error"
  * when build image set another platform
    ~~~
    docker build --platform linux/amd64 -t {for imagename:tag} .
    ~~~

  * create container
    ~~~
    aws lightsail create-container-service --service-name {myservice} --power nano --scale 1
    ~~~

    
  * push image on container
    ~~~
    aws lightsail push-container-image --service-name slackbot --label slackbot --image {myimage}
    ~~~