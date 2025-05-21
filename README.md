# FaceRecognition

Programma failu aizsardzībai: pēc atvēršanas tā aktivizē tīmekļa kameru un pārbauda lietotāja seju, pārbaudijot, vai tas patiešām ir faila īpašnieks.
Ja kamera atpazīst lietotāju kā īpašnieku, fails tiek atvērts, pretējā gadījumā tas neatvēras.
Iespējams arī saglabāt jaunu fotoattēlu vai dzēst veco, un iestatījumos iespējams norādīt ceļu līdz datnei, kurā vēlaties noteikt seju parbaudi.
Grafiskā interfeisa izveidei  tiek izmantots tkinter, jo, salīdzinot ar citiem GUI, tas bija vienkāršākais un vieglāk apgūstams/izmantojams.
Īstenošanai mēs izmantojām OpenCV, lai uzņemtu un zīmētu kadrus, un face_recognition bibliotēku,lai aprēķinātu sejas vektorus.
Mēs arī izmantojam Miniconda, tā ļauj izveidot izolētas vides un izvairīties no versiju nesaderības starp bibliotēku/kodes versijām utt.

Autori: Artemijs Čudinovs, Kirils Ivanovs
