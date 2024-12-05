symptom('flu').
symptom('yellowish eyes and skin').
symptom('dark colored urine').
symptom('pale bowel moment').
symptom('fatigue').
symptom('vomiting').
symptom('fever').
symptom('pain in joints').
symptom('weakness').
symptom('stomach pain').
treatment('flu','drink hot water','avoid cold eatables').
treatment('yellowish eyes and skin','put eyedrops','have healthy sleep','do not strain your eyes').
treatment('dark colored urine','drink lots of water,juices and eat fruits, avoid alcohol consumption').
treatment('pale bowel moment','drink lots of water and excerise regularly').
treatment('fatigue','drink lots of water,juices and eat fruits').
treatment('vomiting','drink salty water').
treatment('fever','put cold water cloth on head and take crocin').
treatment('pain in joints','apply pain spray and take pain killer').
treatment('weakness','drink salty water and eat fruits').
treatment('stomach pain','avoid outside food and eat fruits').

input:-dynamic(patient/2),
    repeat,
    symptom(X),
    write('does the patient have'),
    write(X),
    write('?'),
    read(Y),
    assert(patient(X,Y)),
    \+ not(X='stomach pain'),
    not(output).

disease(hemochromatosis):-
    patient('stomach pain',yes),
    patient('pain in joints',yes),
    patient('dark colored urine',yes),
    patient('yellowish eyes and skin',yes).

disease(hepatitis):-
    not(disease(hemochromatosis)),
    patient('pain in joints',yes),
    patient('fever',yes),
    patient('fatigue',yes),
    patient('vomiting',yes),
    patient('pale bowel moment',yes).

disease(hepatitis_b):-
    not(disease(hemochromatosis)),
    not(disease((hepatitis_c)),
    patient('pale bowel moment',yes),
    patient('dark colored urine',yes),
    patient('yellowish skin and eyes',yes)).

disease(hepatitis_a):-
    not(disease(hemochromatosis)),
    not(disease(hepatitis_c)),
    not(disease(hepatitis_b)),
    patient('flu',yes),
    patient('yellowish eyes and skin',yes).

disease(jaundice):-
    not(disease(hemochromatosis)),
    not(disease(hepatitis_c)),
    not(diease(hepatitis_b)),
    not(disease(hepatitis_a)),
    patient('yellowish eyes and skin',yes).

disease(flu):-
    not(disease(hemochromatosis)),
    not(disease(hepatitis_c)),
    not(disease(hepatitis_a)),
    patient('flu',yes).

output:-
    nl,
    possible_diseases,
    nl,
    advice.

possible_diseases:-
    disease(X),
    write('the patient may suffer from'),
    write(X),
    nl.

advice:-
    symptom(X),
    patient(X,yes),
    treatment(X,Y),
    write('For'), write(X), write(', the recommended treatment is: '),write(Y),nl.





?- Input
Does the patient have flu?|:yes
Does the patient has yellowish eyes and skin?|:yes
Does the patient have dark colored urine?|:yes
Does the patient have pale bowel moment??|:no
Does the patient have fatigue?|:no
Does the patient have vomitting?|:no
Does the patient have fever?|:no
Does the patient have pain in joints?|:no
Does the patient have weakness?|:no
Does the patient have stomach pain?|:no
