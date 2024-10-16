# Hand Tracking Volume Control

This project utilizes hand tracking technology to control the volume of your computer. It uses OpenCV and MediaPipe to detect hand landmarks and the Pycaw library to adjust the system volume based on the distance between two fingers.

## Features

- Real-time hand detection
- Volume control based on hand distance
- Visual feedback with on-screen indicators

## Files

- **HandTrackingModule.py**: A modular version of the hand tracking code, providing a cleaner structure and reusability.
- **VolumeControl.py**: Uses the hand tracking module to control the computer's volume.

## Requirements

Make sure to install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Chikara11/HandTrackingVolumeControl.git
   cd HandTrackingVolumeControl
   ```

2. Activate your virtual environment:

   ```bash
   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Run the volume control program:

   ```bash
   python VolumeControl.py
   ```

4. Adjust the distance between your thumb and index finger to control the volume. The volume level will be displayed on the screen.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
