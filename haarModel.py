import cv2
import os

def imageConverter(vid):
    ident = []
    for a in os.listdir(os.path.join(os.getcwd(),"Haars")):
       ident.append(cv2.CascadeClassifier(os.path.join(os.path.join(os.getcwd(), "Haars"), a )))
    output = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'MPEG'), 30, (1280, 720))
    while True:
        ret, frame = vid.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = frame.copy()
            detections = [ident[k].detectMultiScale(frame, scaleFactor=1.1, minNeighbors=15) for k in range(len(ident))]
            rets = []
            for mod in detections:
                if coloca_retangulo(img, mod) is not None:
                    rets.append(coloca_retangulo(img,mod))

            for r in range(len(rets) - 1):
                if abs(rets[r][1] - rets[r+1][1]) <= 50 and abs(rets[r][2] - rets[r+1][2]) <= 50:
                  img = rets[r][0]
                else:
                   img = img
                  
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            output.write(img)
        else: 
            break

def coloca_retangulo(img, faces):
  img_saida = img.copy()
  for face in faces:
    pos_x, pos_y, largura, altura = face
    cv2.rectangle(img_saida, (pos_x,pos_y), (pos_x+largura, pos_y+altura), color=(200,0,158), thickness=3)
    return [img_saida, pos_x, pos_y]

if __name__ == "__main__":
    vid = cv2.VideoCapture(os.path.join(os.getcwd(), "la_cabra.mp4"))
    imageConverter(vid)