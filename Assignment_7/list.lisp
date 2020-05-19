(sdraw '(defun findEleFromList()
(princ "****Program to find nth elemen****")
(princ "Enter list with paranthesis : ")
(setq li (read))
(princ "Enter n : ")
(setq n (read))
(print "nth Element : ")
(car (nthcdr n li))
))









