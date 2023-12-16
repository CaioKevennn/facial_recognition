import face_recognition as fr
import numpy as np
import cv2
import os
faces=[]

def facial_recognition ():
    take_picture()
    foto_data= fr.load_image_file("./img/picture.jpeg")
    faces1=fr.face_encodings(foto_data)
    if len(faces1)>0:
        return True, faces1
    return False, []

def new_face(nome):
    new_face=facial_recognition()
    if new_face[0]:
        new_face_data=[nome,new_face[1]]
        faces.append(new_face_data)
        print('Rosto do ',nome, 'cadastrado com sucesso')
    else:
        print('Rosto não cadastrado')
    


def identify_face():
    face_test = facial_recognition()  # Assuming the captured face is in the most recent image
    
    if face_test[0]:
        for known_face in faces:
            for datas in known_face[1]:
                # Compare the face encodings
                match = fr.compare_faces([datas], face_test[1][0])

                if any(match):
                    print(f"Rosto identificado como  {known_face[0]}")
                    return
        print("Rosto não identificado.")
    else:
        print("Não há rostos na imagem")

    
    

def take_picture():
    cam=cv2.VideoCapture(0)
    
    while True:
        picture,frame = cam.read()
        cv2.imshow("Camera",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            break
    if picture:
        if not os.path.exists("img"):
            os.makedirs("img")

        # Define o caminho do arquivo de imagem
        caminho_arquivo = os.path.join("img", "picture.jpeg")

        # Salva a última imagem no formato JPEG antes de encerrar
        cv2.imwrite(caminho_arquivo, frame)
        print(f"Foto salva em: {caminho_arquivo}")
    else:
        print("Não foi possível capturar a imagem.")

new_face("caio")

identify_face()