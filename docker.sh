#!/bin/sh
cd haproxy-dg ;ansible-playbook -i hosts site.yml

echo $pwd
