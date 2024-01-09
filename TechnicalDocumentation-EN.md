# Technical Documentation

**English** | [Türkçe](/TechnicalDocumentation-TR.md)

### About

A Python Flask based, open source, web application made to introduce the Burhaniye region to children in a fun game format.

### Languages Used

- Python v3.12.0
- JavaScript vES14
- HTML5
- CSS3

### Libraries Used

- Flask v3.0.0
- Jinja2 v3.1.2 
- Socket v1.0.0
- Secrets v1.0.0
- TailwindCSS v3.4.1

### Programs Used in the Development Process

- Visual Studio Code v1.85.1 (code editor)
- GitHub Desktop v3.3.6 (Git interface)
- Windows Terminal v1.18.3181.0 (terminal interface)
- Git Bash v5.2.15 (terminal)

### Interface

HTML5 and Jinja2 are used in the interface of the application. TailwindCSS was used for styling the interface except for the background image, only CSS3 was used for the background image. JavaScript was used to play the sound effects in the interface. JavaScript is also used to automatically redirect the user to the start page in case of a "404 Page Not Found" error.

### Backend

Flask, a Python web library, was used on the server side. Flask is preferred because it is a simple and fast library. Apart from Flask, Python's own "secrets" and "socket" libraries were also used. Socket was used to access the IP address of the local computer where the application is running. Secrets is used to generate a 32 character random secret password. This password is the secret key of the Flask application.

### Deployment

Our Flask-based application was released for free thanks to [PythonAnyWhere.com](https://www.pythonanywhere.com/). Although the application used version 3.12.0 of Python during development, the release version on PythonAnyWhere uses version 3.10.0 of Python. This is because the latest Python version supported by PythonAnyWhere is 3.10.0.

### Version Control

Git was used for version control. The application is completely open source. [You can access all the code on GitHub](https://github.com/DogukanUrker/BurhaniyeAPP)

### QR Code

[QR Code Generator](https://www.qr-code-generator.com/) was used for the QR code. The link "<https://www.pythonanywhere.com/>" is embedded in the QR code.

### Audio Files/Effects

All audio files and effects are in "mp3" format. This is because the mp3 file extension is supported by almost all web browsers. Sound effects (applause, correct and incorrect answers) are taken from [pixabay](https://pixabay.com/sound-effects/). Audio files (voice narrations) were recorded with Samsung Note 10, HUAWEI MateBook D 15 and iPhone 11 devices. The recordings were converted from "m4a" or "ogg" format to "mp3" format using the website [Convertio](https://convertio.co/).

### Images

The background image was taken from [Creative Fabrica](https://www.creativefabrica.com/). For other images, [Google Images](https://images.google.com/) and [Bing Images](https://www.bing.com/images) were used. File formats used were "png", "jpeg", "webp" and "jfif".

