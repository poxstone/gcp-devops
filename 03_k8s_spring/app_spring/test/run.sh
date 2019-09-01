#!/bin/sh
cd $(dirname $0)

#cd ../complete

#mvn clean package
#ret=$?
#if [ $ret -ne 0 ]; then
#exit $ret
#fi
#rm -rf target

#
#mvn clean compile
#ret=$?
#if [ $ret -ne 0 ]; then
#exit $ret
#fi
#rm -rf target


cd ../complete

./gradlew build
ret=$?
if [ $ret -ne 0 ]; then
exit $ret
fi
rm -rf build

./gradlew compileJava
ret=$?
if [ $ret -ne 0 ]; then
exit $ret
fi
rm -rf build

exit
