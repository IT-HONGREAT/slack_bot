## Deploy

SlackBot -> AWS Lightsail

### local deploy

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

### prod deploy

> local test 기반으로 CI/CD 작성됨.

Lightsail CI/CD Process(및 참고한 것.)

* docker build 시 configuration 을 위한 docker buildx [옵션 관련 참고한 repo](https://github.com/docker/setup-buildx-action)
* lightsail 구조상 컨테이너 내부에 image push가 가능
    * push 된 이미지는 lightsail 이미지에서 tag가 지정되기 때문에 별도로 파싱이 필요 하다.

* Container Deploy 시 manifest 를 cli-input-json 로 이용함.
    * image name 관련 파싱에 [json프로세서 - jq](https://www.44bits.io/ko/post/cli_json_processor_jq_basic_syntax) 를 이용함.


* github secrets >> ".env" in running CI/CD workflow when it is building.
  * build-args 로 Dockerfile에 ARG 전달, setup_env.sh 의 실행문 RUN 하여 .env 완성
    * Check by `RUN cat .env` 

| No  | github secret key    | For             |
|-----|:---------------------|-----------------|
| 1   | NOTION               | setting         |                            
| 2   | SLACK_APP_TOKEN      | setting         |                            
| 3   | SLACK_BOT_TOKEN      | setting         |                            
| 4   | SLACK_SIGNING_SECRET | setting(현재 필요X) |                            
| 5   | NOTION_reservation   | notion_DB       |                            
| 6   | NOTION_lunch         | notion_DB       |                            
