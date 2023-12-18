import face_recognition as fr
import cv2
import os

faces = []


def facial_recognition():
    take_picture()
    foto_data = fr.load_image_file("./img/picture.jpeg")
    faces1 = fr.face_encodings(foto_data)
    if len(faces1) > 0:
        return True, faces1
    return False, []


def new_face(nome):
    new_face = facial_recognition()
    if new_face[0]:
        new_face_data = [nome, new_face[1]]
        faces.append(new_face_data)

        print("---------------------------------------------------\n\n")
        print("Rosto do ", nome, "cadastrado com sucesso.\n\n")
    else:
        print("Rosto não cadastrado")


def identify_face():
    face_test = facial_recognition()
    if face_test[0]:
        for known_face in faces:
            for datas in known_face[1]:
                match = fr.compare_faces([datas], face_test[1][0])
                if any(match):
                    
                    print("---------------------------------------------------\n\n")
                    print(f"Rosto identificado como  {known_face[0]}.\n\n")
                    return
        print("Rosto não identificado.")
    else:
        print("Não há rostos na imagem.")


def take_picture():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        picture, frame = cam.read()
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cam.release()
            cv2.destroyAllWindows()
            break
    if picture:
        if not os.path.exists("img"):
            os.makedirs("img")
        caminho_arquivo = os.path.join("img", "picture.jpeg")
        cv2.imwrite(caminho_arquivo, frame)
    else:
        print("Não foi possível capturar a imagem.")


def edit_face():
    if not faces:
        print("Nenhum rosto cadastrado para editar.")
        return
    name = input("Digite o nome da pessoa que  deseja editar:\n")
    for i, face_data in enumerate(faces):
        if face_data[0] == name:
            new_name = input("Digite o novo nome:\n ")
            if new_name:
                face_data[0] = new_name
            print("---------------------------------------------------\n\n")
            print("Informações editadas com sucesso.\n\n")
            return
    print("Rosto não encontrado. Certifique-se de que o nome está correto.\n\n")


def show_names():
    if not faces:
        print("Nenhum rosto cadastrado.")
    else:
            
        print("---------------------------------------------------\n\n")
        print("Rostos cadastrados:\n")
        for face_data in faces:
            print(face_data[0])


n1 = int
while n1 != "5":
    print("---------------------------------------------------")
    n1 = input(
        "O que deseja fazer?\n1-Cadastrar um rosto\n2-Verificar se um rosto está cadastrado\n3-Editar as informações de uma pessoa\n4-Listar os rostos cadastrados\n5-Sair\n"
    )
    if n1 == "1":
        new_face(input("Digite o nome da pessoa que deseja cadastrar: "))
    elif n1 == "2":
        identify_face()
    elif n1 == "3":
        edit_face()
    elif n1 == "4":
        show_names()
    elif n1 == "5":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
