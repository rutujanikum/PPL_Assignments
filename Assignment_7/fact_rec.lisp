(load "sdraw.generic")
(defun factorial(num)
	(sdraw '(if (= num 1)
		1
		(* num (factorial(- num 1)))))
)