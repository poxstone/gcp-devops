# Devops test

## Vars
```bash
declare PROJECT_ID='';
declare APP_VER='1.0.0a';
```

## java spring build and run
```bash
# go to dir
cd app_spring/complete/;

# gradle build
gradle build;
java -jar build/libs/app_spring-0.1.0.jar;
# maven build
mvn
# get web app
curl -X GET "localhost:8080/greeting?name=Perdro";
```

## Docker container jar
```bash
docker build -t "gcr.io/${PROJECT_ID}/app_sprig:${APP_VER}" -f "docker/Dokerfile" "./";
docker run --rm -it -p 8080:8080 "gcr.io/${PROJECT_ID}/app_sprig${APP_VER}";

# docker upload gcp
gcloud auth configure-docker -q;
docker push "gcr.io/${PROJECT_ID}/app_sprig:${APP_VER}";
```

## Kubernetes deploy
- Create cluste:
```bash
gcloud beta container --project "${PROJECT_ID}" clusters create "k8s-app" --zone "us-east1-d" --machine-type "n1-standard-1" --preemptible --num-nodes "1" --enable-autoscaling --min-nodes "1" --max-nodes "3" --enable-autorepair --subnetwork "projects/${PROJECT_ID}/regions/us-east1/subnetworks/default";

gcloud container clusters get-credentials "k8s-app" --zone us-east1-d --project "${PROJECT_ID}";

kubectl apply -f kubernetes_files/app_spring.yaml \
              -f kubernetes_files/app_spring_service.yaml \
              -f kubernetes_files/app_spring_ingress_backendconfig.yaml \
              -f kubernetes_files/app_spring_ingress.yaml;


```
