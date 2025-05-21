# FaceRecognition

Programma failu aizsardzībai: pēc atvēršanas tā aktivizē tīmekļa kameru un pārbauda lietotāja seju.
Ja kamera jūs atpazīst, fails tiek atvērts, pretējā gadījumā tas neatvēras.
Varat arī saglabāt jaunu fotoattēlu vai dzēst veco, un iestatījumos varat norādīt ceļu līdz datnei, kuras vēlaties noteikt seju parbaudi.
Grafiskā interfeisa izveidei izmantojām tkinter, jo, salīdzinot ar citiem GUI, tas bija vienkāršākais un vieglāk apgūstams/izmantojams.
Īstenošanai mēs izmantojām OpenCV, lai uzņemtu un zīmētu kadrus, un face_recognition bibliotēku,lai aprēķinātu sejas vektorus.
Mēs arī izmantojam Miniconda, tā ļauj izveidot izolētas vides un izvairīties no versiju nesaderības starp bibliotēku/kodes versijām utt.

Autori: Artemijs Čudinovs, Kirils Ivanovs
