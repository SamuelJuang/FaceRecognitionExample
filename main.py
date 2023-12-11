import cv2
import os
import numpy as np
import face_recognition


foto = face_recognition.load_image_file("suspect/FotoTest1.png")
foto = cv2.cvtColor(foto,cv2.COLOR_BGR2RGB)

# fotoTest = face_recognition.load_image_file("pics/FotoTest2.jpeg")
# fotoTest = cv2.cvtColor(fotoTest,cv2.COLOR_BGR2RGB)
# fotoTest = cv2.resize(fotoTest,(0,0), fx = 0.5, fy = 0.5)

faceLoc = face_recognition.face_locations(foto)[0]
encodeFace = face_recognition.face_encodings(foto)[0]
print(encodeFace)
cv2.rectangle(foto, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),(255,0,255),2)

#Penggunaan Facial recognition pada 1 foto
# faceLocTest = face_recognition.face_locations(fotoTest)[0]
# faceLocEnc = face_recognition.face_encodings(fotoTest)[0]
#
# result = face_recognition.compare_faces([faceLocEnc],faceLocTest)
# print(result)
#
# if(result[0] == True):
#     cv2.rectangle(fotoTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]),(255,0,255),2)
#
cv2.imshow('Sample', foto)
# cv2.imshow('Test', fotoTest)
# cv2.waitKey(0)

#Penggunaan facial recognition pada sebuah directory banyak foto

#penggunaan pengkodean muka kedua
fotoEnc2 =face_recognition.load_image_file("suspect/William_suspect.jpg")
fotoEnc2 = cv2.cvtColor(fotoEnc2,cv2.COLOR_BGR2RGB)
fotoEnc2 = cv2.resize(fotoEnc2, (0, 0), fx=0.3, fy=0.3)
fotoEnc2 = cv2.rotate(fotoEnc2,cv2.ROTATE_90_CLOCKWISE)

faceLoc2 = face_recognition.face_locations(fotoEnc2)[0]
encodeFace2 = face_recognition.face_encodings(fotoEnc2)[0]
cv2.rectangle(fotoEnc2, (faceLoc2[3], faceLoc2[0]), (faceLoc2[1], faceLoc2[2]),(255,0,255),2)
cv2.imshow('Sample 2', fotoEnc2)


for filename in os.listdir("pics"):
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
        fotoTest = face_recognition.load_image_file(os.path.join("pics", filename))
        fotoTest = cv2.cvtColor(fotoTest, cv2.COLOR_BGR2RGB)
        if(filename == "FotoTest2.jpeg"):
            fotoTest = cv2.resize(fotoTest, (0, 0), fx=0.5, fy=0.5)

        faceLocTest = face_recognition.face_locations(fotoTest)
        if faceLocTest:
            faceLocEnc = face_recognition.face_encodings(fotoTest)
            for i in range(len(faceLocTest)):
                result2 = face_recognition.compare_faces([encodeFace], faceLocEnc[i], tolerance= 0.3) #0.4
                result = face_recognition.compare_faces([encodeFace2],faceLocEnc[i], tolerance= 0.6) #0.5
                print(f"Result for " + filename + " : " + str(result2) + "Using First Sample")
                print(f"Result for " + filename + " : " + str(result) + "Using second Sample")

                if result2[0]:
                    cv2.rectangle(fotoTest, (faceLocTest[i][3], faceLocTest[i][0]), (faceLocTest[i][1], faceLocTest[i][2]), (255, 0, 255), 2)
                    cv2.imshow(f"Match found in {filename}", fotoTest)
                elif result[0]:
                    cv2.rectangle(fotoTest, (faceLocTest[i][3], faceLocTest[i][0]),(faceLocTest[i][1], faceLocTest[i][2]), (255, 0, 255), 2)
                    cv2.imshow(f"Match found in {filename}", fotoTest)
cv2.waitKey(0)
