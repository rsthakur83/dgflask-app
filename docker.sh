#!/bin/sh
cd haproxy-dg ;ansible-playbook -i hosts site.yml --extra-vars env=dev

echo $pwd
