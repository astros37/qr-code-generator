# QR Code Generator

A simple Python script to generate QR codes for any input text or URL.

## Features
- Generate QR codes from any text or URL.
- Save QR codes as PNG files.
- Easy to use command-line interface (CLI).

## Requirements
- Python 3.x
- `qrcode` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/qr-code-generator.git
   cd qr-code-generator
   ```

2. Install the required library:
   ```bash
   pip install qrcode[pil]
   ```

## Usage
1. Run the script:
   ```bash
   python qr_code_generator.py
   ```

2. Enter the text or URL you want to convert into a QR code.

3. The generated QR code will be saved as a PNG file (default name: `qr_code.png`) in the current directory.

## Example
### Input:
```text
Enter text or URL for the QR code: https://github.com
```

### Output:
- A file named `qr_code.png` will be created in the current directory.
- The QR code image will encode the URL `https://github.com`.

## Customization
You can customize the script to:
- Change the size of the QR code by modifying the `box_size` parameter.
- Adjust the border size by changing the `border` parameter.
- Save the file with a custom name by modifying the `output_file` variable.

## Contributing
Feel free to fork this repository and submit pull requests to add new features or improve the script. All contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

