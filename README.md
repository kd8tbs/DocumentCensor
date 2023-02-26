# DocuShield
<p align="center">
  <img src="https://user-images.githubusercontent.com/23301116/221422653-aceafc9e-7c33-4bf1-b150-f8fcb9056646.png" alt="DocuShield Logo"/>
</p>

## Overview
DocuShield is a simple program that takes a Microsoft Office word document as input and with Natural Language Processing it detects possibly sensitive information and removes it. Then, the app exports a copy of the censored document. 

This program was originally developed at the Central Michigan University, Reimagine Hackathon of 2023

## System Requirements
- Text Files that can be used with DocuShield:
  - .docx (Micosoft Office Word)
- Versions of Python DocuShield has been tested with:
  - 3.10.10
- Python Libraries/Modules Installed:
  - [spaCy](https://spacy.io/usage)
  - [tkinter](https://www.tutorialspoint.com/how-to-install-tkinter-in-python)
  - [docx](https://pypi.org/project/python-docx/)
  - [os](https://docs.python.org/3/library/os.html)
  - [PIL](https://pypi.org/project/Pillow/)
  - [re](https://docs.python.org/3/library/re.html)

## How to run 
**At this time, only use docx files with DocuShield!!!**

1. Install Python Ver 3.10.10 and the Libraries/Modules listed in the **System Requirements**
2. Download and open the code in your favorite IDE (We used VSCode)
3. Run the program from the FrontEnd.py file
4. Once the GUI for DocuShield appears, either enter a path to the file you wish to use, or click **Select docx**, then a file explorer window will appear and you may choose a file to utilize 

![DocuShield_GUI](https://user-images.githubusercontent.com/23301116/221427538-3b0ea673-27e3-44e0-b979-ffad3983366f.PNG)

5. Finally, click **Shield**

A document of the same name as your original file with "-Shielded" added to the end, will appear. This new document will be located in the same directory of the original file. All sensitive information will be replaced with the phrase "[REDACTED]", in your new document.

## Credits 
### Our Team
- [Gary Pinsky](https://github.com/kd8tbs)
- [Jared Dunham](https://github.com/gitgud115)
- Danny Mills 
- [Jack Tadych](https://github.com/Jack-Tadych)

### Last README update: 02/26/2023
