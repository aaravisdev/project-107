import cv2

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def goal_track(img, bbox):
    # Define your logic for processing the tracked object here if needed
    pass

# Initialize the tracker (assuming you have the tracker initialized)
tracker = cv2.TrackerCSRT_create()  # You can use a different tracker based on your requirements

# Your video capture code goes here to start reading the video
video = cv2.VideoCapture('your_video_file.mp4')  # Change 'your_video_file.mp4' to your video file path

# Assuming the initial frame is read and the object to be tracked is selected or detected
ret, img = video.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)

while True:
    ret, img = video.read()
    if not ret:
        break
    
    success, bbox = tracker.update(img)
    
    if success:
        drawBox(img, bbox)
        goal_track(img, bbox)
    else:
        cv2.putText(img, "LOST", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow("Tracking", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
