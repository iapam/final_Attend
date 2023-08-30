# Student Attendance System Based on Facial Recognition

Machine Learning project to recognise people from an Image.

Built with the help of [dlib's](http://dlib.net/) for face recognition built with deep learning.
The model has an accuracy of 99.38%.

## Dependencies:

- Python 3.x
- Numpy
- [dlib](http://dlib.net/)

    Tip: Installing dlib can be a tedious job. On macOS or Linux you may follow [this link](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf).

- Extras:

    - OpenCV (required only in `webcam.py` for capturing frames from the webcam)
    - cvzone
    - cmake
    - face-recognition
    - openpyxl
    - psycopg2
    - firebase_admin


## Procedure:

- Clone this repository `git clone git@github.com:iapam/final_Attend`.

### Training:
- Make folder `images`.
- crop image 216x216 and add id generated during registration
- Add images of each person you want to recognise to a folder by their name in `images`.

    Example
    ```bash
    $ mkdir images
    $ cd images
    
    ```
    Then copy all the images of the person to `images` folder.

- The images are then extracted by the face encodings algorithm using the convolutional
  layer of the deep CNN to represent the numerical representation of the facial
  features

    Note: There has to be only one face per image otherwise encoding will be for the first face found in the image.

- During attendance taking,  If the newly obtained features is matched with the already extracted features in the dataset, an attendance is taking.
- The user can the generate reports once attendance is taken.



## Vote of Thanks
- Thanks to [Adam Geitgey](https://github.com/ageitgey) whose blog inspired me to make this project.
- Thanks to [Davis King](https://github.com/davisking) for creating dlib and for providing the trained facial feature
  detection and face encoding models used in this project.
