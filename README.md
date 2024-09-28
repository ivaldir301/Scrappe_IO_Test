# Laptop Prices Web Scrapper

## Description
This project aims to pick the best prices out of hundreds of products on the [webscrape.io](https://www.webscrape.io) website. With a focus on efficiency and accuracy, the Laptop Prices Web Scrapper utilizes advanced web scraping techniques to provide users with the most competitive prices available online.

## Tech Stack
- **Python 3**
- **Libraries:** `httpx`, `selectolax`, `pandas`
- **Web Framework:** `FastAPI`
- **Containerization:** `Docker`
- **CI/CD:** GitHub Actions
- **Deployment:** Render

## How to Run the Project

### Using Docker
To run the project using Docker, follow these steps:

1. **Clone the project in your local machine**

```
        mkdir laptop-scraper
        cd laptop-scraper
        git clone https://github.com/ivaldir301/Scrappe_IO_Test.git .   
        git switch dev
```

1. **Build the Docker Image:**

```
        docker build -t laptop-scrapper .
```

2. **Run the docker image**

```
        docker run -d -p 8009:8009 laptop-scrapper
```

### Folder Structure

```
├── logs
├── utils
├── scrapper 
│   ├── models
│   └── scrapper_io
│       ├── main.py
│       └── utils.py
├── README.md
├── requirements.txt
├── Dockerfile
├── .env-example
└── .gitignore
```

### Contribuiting

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

```
1 - Fork the repository.
2 - Create a new branch for your feature or bug fix.
3 - Make your changes and commit them with clear messages.
4 - Push your changes to your forked repository.
5 - Create a pull request describing your change
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.