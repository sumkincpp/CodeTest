#!/bin/bash
# Used in labs to reveal Kubernetes dashboard access token.
# K8s dashboard is started when a K8s based lab is started in 
# background script k8s-dashboard.sh

COLOR_RESET='\e[0m'
COLOR_LIGHT_GREEN='\e[0;1;32m' 
COLOR_CAUTION='\e[0;1;33m'

DASH_NAMESPACE=kubernetes-dashboard
SECRET_RESOURCE=$(kubectl get secrets -n $DASH_NAMESPACE -o name | grep secret/kubernetes-dashboard-token)
ENCODED_TOKEN=$(kubectl get "$SECRET_RESOURCE" -n $DASH_NAMESPACE -o=jsonpath='{.data.token}')
TOKEN=$(echo "$ENCODED_TOKEN" | base64 --decode)

echo ""
echo 'To access the Dashboard click on the Kubernetes Dashboard tab above this command '
echo 'line. At the sign-in prompt, select Token and paste in the token that is revealed below.'
echo ""
echo "--- ✂ --- ▼ Copy and paste this colored token for Dashboard access ▼ ---"
if [ -z "$TOKEN" ]
then
  echo -e "$COLOR_CAUTION"
  echo "⚠️  The Dashboard is initializing so the token is not available yet. Try again in a moment."
else
  echo -e "$COLOR_LIGHT_GREEN"
  echo -e "$TOKEN"
fi
echo -e "$COLOR_RESET"
echo "--- ✂ --- ▲"
echo ''
echo '💡 For Kubernetes clusters exposed to the public, always lock administrative access, including '
echo 'access to the Dashboard. Why? https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/'
echo ''
