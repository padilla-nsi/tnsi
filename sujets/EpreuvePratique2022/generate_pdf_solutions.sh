#!/bin/bash
for d in ./*/ ;
do (
	echo "$d" &&
	cd "$d" &&
	./../generate_one_pdf_solution.sh
); 
done

