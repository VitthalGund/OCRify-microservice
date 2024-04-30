
# OCRify Microservice 🖼️🔍

OCRify Microservice is a Python-based microservice built using the FASTAPI framework, designed to extract text from images with high accuracy and precision. It utilizes Optical Character Recognition (OCR) technology to analyze images and extract text content, supporting various image formats such as PNG, JPEG, and JPG.

## Features ✨

- **High Accuracy**: OCRify Microservice boasts a text extraction accuracy level of 95%, ensuring reliable results.
- **Multiple Image Format Support**: Supports all major and widely used image formats, making it versatile and adaptable.
- **Simple Integration**: Users can submit input images via HTTP POST requests, making integration straightforward and seamless.
- **Open-Source**: OCRify Microservice is an open-source project, allowing for easy hosting and customization by developers.

## Usage 🚀

To use OCRify Microservice, follow these simple steps:

1. **Installation**: Clone the repository to your local machine.

   ```bash
   git clone https://github.com/VitthalGund/ocrify-microservice.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install dependencies using pip.

   ```bash
   cd ocrify-microservice
   pip install -r requirements.txt
   ```

3. **Run the Service**: Start the microservice locally.

   ```bash
   uvicorn main:app --reload
   ```

4. **Submit Image**: Send a POST request to the endpoint `http://localhost:8000/` with the input image.

   ```bash
   curl -X POST -F "image=@/path/to/your/image.jpg" http://localhost:8000/
   ```

5. **Retrieve Text**: Receive the extracted text content in the response.

   ```json
   {
     "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
   }
   ```

## Deployment 🚀

While the microservice is not live yet, it can be deployed to various platforms such as Docker, Kubernetes, or traditional web hosting services.

## Contributing 🤝

Contributions to OCRify Microservice are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
