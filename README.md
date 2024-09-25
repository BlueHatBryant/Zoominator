# Zoominator  

**Zoominator** is a Python script that automatically logs into Zoom and joins your scheduled classes or meetings with just a click. Designed for students and professionals alike, this tool streamlines the process of attending online meetings.  

## Features  

- **Automatic Login**: Logs into your Zoom account using your email and password.  
- **Join Meetings**: Quickly joins a Zoom meeting using the meeting invite link.  
- **Customizable Time Inputs**: Prompts you for start and end times in Eastern Standard Time (EST) to run the script.  
- **Automated Shutdown**: Shuts down your computer automatically at the end of the class.  

## Prerequisites

To run Zoominator, you will need:  

- Python 3.  
- [Selenium](https://pypi.org/project/selenium/) library  
- [pytz](https://pypi.org/project/pytz/) library (for timezone handling)  
- [pyautogui](https://pypi.org/project/PyAutoGUI/) library  
- A web browser and its corresponding WebDriver (e.g., ChromeDriver for Google Chrome)  

## Installation  

1. Clone this repository:  

```bash  
   git clone https://github.com/yourusername/Zoominator.git  
   cd Zoominator  
```
Install the required libraries:  

```pip install selenium pytz pyautogui```    
Download the appropriate WebDriver for your browser and ensure it’s in your system’s PATH.  

Create a file named zoominator-details.txt in the same folder as the script with the following format:  

make a text file  
```bash 
zoom_email=your_email@example.com
zoom_password=your_password
invite_link=https://us04web.zoom.us/j/your_meeting_id?pwd=your_passcode
display_name=Your Display Name
```
### Usage
Open the script (zoominator.py) and set your Zoom credentials and meeting details in the zoominator-details.txt file as specified above.   

Run the script:  

```bash
python zoominator.py
```
Sit back and watch as the script logs you in and joins your meeting!  

### License  
This project is licensed under the MIT License - see the LICENSE file for details.  

### Contributing  
Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.  

### Acknowledgments  
Inspired by the need for easier access to online classes and meetings during remote learning.  