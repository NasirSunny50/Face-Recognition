import cv2
import face_recognition

image_to_detect = cv2.imread('images/life.jpg')
cv2.imshow("test",image_to_detect)

all_face_location = face_recognition.face_locations(image_to_detect,model='hog')
print("There are {} no of images".format(len(all_face_location)))

for i,current_face_location in enumerate(all_face_location):
    top_pos,right_pos,bottom_pos,left_pos = current_face_location
    
    print("Found face {} at top:{}, right:{}, bottom:{}, left:{}".format(i+1,top_pos,right_pos,bottom_pos,left_pos))

    current_face_location=image_to_detect[top_pos:bottom_pos,left_pos:right_pos]
    cv2.imshow("Face no "+str(i+1),current_face_location)
    
    
    
