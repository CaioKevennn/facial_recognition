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
    


def identify_face(face):
    face_test = facial_recognition(face)
    
    if face_test[0]:
        face_to_check=face_test[1][0]
        result=[]

        for data in faces:
            face_data=data[1][0]
            test = fr.compare_faces([face_data],face_to_check,)
    
            if any(test):
                result.append(data[0])

        print("O rosto encontrado é de:",result)
    else:
        print('nenhum rosto encontrado')

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

#take_picture()
new_face("Caio Keven")


#new_face("Ed","./img/ed.jpg")
#new_face("Oto","./img/oto.jpg")
#identify_face("./img/oto_desconhecido.jpg")
identify_face("./img/picture.jpeg")
            
        






#Test if the code recognizes that there is a face
#print(facial_recognition("./img/oto_desconhecido.jpg"))
##Test if the code recognizes that there is not  a face
#print(facial_recognition("./img/carro.jpg"))
#new_face("Oto",("./img/oto_desconhecido.jpg"))

#print(new_face("Oto",("./img/oto.jpg")))

#print(new_face("Caio",("./img/oto_desconhecido.jpg")))
#print(new_face("Keven",("./img/oto_desconhecido.jpg")))
#print("-------------------------------------------------")
#print(len(faces))
#print("-------------------------------------------------")
#identify_face("./img/oto.jpg")
#for i in faces:
 #   for K in i[1]:
        #print(K)

