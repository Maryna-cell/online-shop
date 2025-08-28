# Online Shop

### Project Description
This project is a prototype of an online store developed using the Django framework. It was created to demonstrate web development skills and is an educational project.

### Key Features
* **Product Catalog:** The ability to view a list of products.
* **Shopping Cart:** Basic shopping cart functionality is implemented.
* **Order System:** A basic order processing system is included.
* **Internationalization:** The ability to switch between English and Spanish languages using the **`django-modeltranslation`** package.

### Technologies
The project was developed using the following technologies:
* **Django:** A Python web framework.
* **Python:** The programming language.
* **HTML/CSS:** For creating the user interface.
* **Database:** SQLite

### Running the project
Follow these instructions to run the project on your computer:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Maryna-cell/online-shop.git](https://github.com/Maryna-cell/online-shop.git)
    cd myshop
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # For Windows:
    venv\Scripts\activate
    # For macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Django server:**
    ```bash
    python manage.py runserver
    ```

The project will be available in your browser at `http://127.0.0.1:8000/`.

---
**Note:** At this stage, some functions (e.g., access to the shopping cart) do not have a full user interface, and they are accessed by directly entering the address in the URL bar.
