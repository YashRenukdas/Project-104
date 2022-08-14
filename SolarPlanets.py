import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20,250), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.putText(img, "Mercury", (110,250), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (190,260), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (290,265), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
cv2.putText(img, "Moon", (321,160), cv2.FONT_HERSHEY_DUPLEX, 0.3, (255,255,255))
cv2.putText(img, "Mars", (383,260), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (555,400), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (760,320), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (964,300), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1110,300), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))

cv2.imshow("Planets",img)
cv2.waitKey(0)
cv2.imwrite("SolarSystemWithPlanetames.jpg",img)