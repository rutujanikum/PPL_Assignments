airport(toronto,50,60).
airport(madrid,75,45).
airport(valencia,40,20).
airport(paris,50,60).
airport(toulouse,40,30).
airport(london,75,80).
airport(barcelona,40,30).
airport(malaga,50,30).

flight(toronto,iberia,madrid,800,480).
flight(toronto,united,madrid,75,45).
flight(toronto,air_canada,madrid,900,480).
flight(toronto,united,london,650,420).
flight(toronto,air_canada,london,500,360).
flight(madrid,air_canada,barcelona,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(madrid,iberia,valencia,40,20).
flight(madrid,iberia,malaga,50,60).
flight(malaga,iberia,valencia,80,120).
flight(valencia,iberia,barcelona,110,75).
flight(barcelona,iberia,london,220,240).
flight(paris,united,toulouse,40,30).
flight(toulouse,united,paris,40,30).
flight(madrid,iberia,toronto,800,480).
flight(madrid,united,toronto,75,45).
flight(madrid,air_canada,toronto,900,480).
flight(london,united,toronto,650,420).
flight(london,air_canada,toronto,500,360).
flight(barcelona,air_canada,madrid,100,60).
flight(barcelona,iberia,madrid,120,65).
flight(valencia,iberia,madrid,40,20).
flight(malaga,iberia,madrid,50,60).
flight(valencia,iberia,malaga,80,120).
flight(barcelona,iberia,valencia,110,75).
flight(london,iberia,barcelona,220,240).

check_flight(X,Y):-flight(X,_,Y,_,_).
check_cheap_flight(A,B,C):-flight(A,C,B,X,_), (X<400).
check_two_flight(X,Y):-(flight(X,A,Y,_,_), flight(X,B,Y,_,_)), (A\=B).
check_pref_flight(A,B,C):-flight(A,C,B,X,_), ((X<400);(C=air_canada)).
if_united_then_air_canada(A,B):-(flight(A,X,B,_,_),(X=united)) -> (flight(A,Y,B,_,_),(Y=air_canada)).
