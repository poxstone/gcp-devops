#!/bin/bash

declare PROJECT_ID="$1";
declare APP_VER="$2";

export FILE_APP_YAML="./kubernetes_files/app_spring.yaml";
grep "${FILE_APP_YAML}" -ne "\${PROJECT_ID}" | awk -F ":" '{print($1)}' | xargs -I {} sed -i {}'s/\${PROJECT_ID}/'${PROJECT_ID}'/' "${FILE_APP_YAML}";
grep "${FILE_APP_YAML}" -ne "\${APP_VER}" | awk -F ":" '{print($1)}' | xargs -I {} sed -i {}'s/\${APP_VER}/'${APP_VER}'/' "${FILE_APP_YAML}";

echo "Prepared all ready!"