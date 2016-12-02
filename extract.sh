#!/bin/bash
echo "Register No,Name,301,302,303,304,305,306,307(P),308(P),SGPA"
for i in {1..69}
do
pdftotext $i.pdf $i.txt -raw
# echo $i
# if [ $i -eq 18 ];then continue
# elif [ $i -eq 54 ];then continue
# else
# i="r"
#

# EN14 301 ENGINEERING MATHEMATICS III 4 D NOVEMBER,2015 Rg
# EN14 302 COMPUTER PROGRAMMING IN C 4 C NOVEMBER,2015 Rg
# CS14 303 COMPUTER ORGANISATION & DESIGN 4 C NOVEMBER,2015 Rg
# CS14 304 DISCRETE COMPUTATIONAL STRUCTURES 4 C NOVEMBER,2015 Rg
# CS14 305 ELECTRONIC CIRCUITS 4 D NOVEMBER,2015 Rg
# CS14 306 SWITCHING THEORY & LOGIC DESIGN 4 C NOVEMBER,2015 Rg
# CS14 307(P) PROGRAMMING LAB 2 A NOVEMBER,2015 Rg
# CS14 308(P) ELECTRONICS CIRCUITS LAB 2 B NOVEMBER,2015 Rg
# Semester Grade Point Average (SGPA-III) : 6.93


name=`cat $i.txt|grep NAME|cut -d: -f2`
reg=`cat $i.txt|grep "REGISTER No. :"|cut -d' ' -f4`
sub1=`cat $i.txt|grep 301|cut -d' ' -f7`
sub2=`cat $i.txt|grep 302|cut -d' ' -f8`
sub3=`cat $i.txt|grep 303|cut -d' ' -f8`
sub4=`cat $i.txt|grep 304|cut -d' ' -f7`
sub5=`cat $i.txt|grep 305|cut -d' ' -f6`
sub6=`cat $i.txt|grep 306|cut -d' ' -f9`
sub7=`cat $i.txt|grep 307|cut -d' ' -f6`
sub8=`cat $i.txt|grep 308|cut -d' ' -f7`
sgpa=`cat $i.txt|grep SGPA|cut -d' ' -f7`
echo $reg,$name,$sub1,$sub2,$sub3,$sub4,$sub5,$sub6,$sub7,$sub8,$sgpa
#fi
done
rm *.txt
