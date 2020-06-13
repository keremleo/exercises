#! /bin/bash

echo "Please enter root password : "

sudo root

a=$(echo $?)
b=$(whoami)

if [ a -ne 0 ]; then
   echo "You are not a root user"
else
   echo "Welcome $b "
fi


ls AccessLog.txt
cont=$(echo $?)
if [ $cont -ne 0 ]
then
   touch AccessLog.txt
elif [ $cont -eq 0 ]
then
   da=$(date)
   us=$(whoami)
   echo "$da       $us" >> AccessLog.txt
   #let count=$count+1
fi

python3 --version
cnt=$(echo $?)
if [ $cnt -ne 0 ]
then
        sudo yum install python3 -y
else
        sudo ls /usr/bin | grep "python3"
        num1=$(echo $?)
        if [ $num1 -ne 0 ]
        then
                sudo export $PATH=PATH:/usr/bin/python3
        fi
fi

ls phone_book.py 
varsa=$(echo $?)
if [ $varsa -eq 0 ]
then  
   python3 My_phone_book.py
else
   sudo yum git --version
   git_control=$(echo $?)
   if [ $git_control -eq 0 ]
      git clone fsfasf
   else
      sudo yum install git -y
      python3 proje/My_phone_book.py





