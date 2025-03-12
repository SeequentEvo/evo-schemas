#!/bin/bash
# Checks a commit to ensure Seequent or Bentley emails were not used

EMAIL=$(git config user.email)

if [[ $(echo $EMAIL | grep -i "@seequent.com") || $(echo $EMAIL | grep -i "@bentley.com") ]]; then
  echo "Please enable 'no-reply' commit settings in your GitHub account"
  echo "See https://docs.github.com/articles/setting-your-email-in-git"
  exit 1
fi
