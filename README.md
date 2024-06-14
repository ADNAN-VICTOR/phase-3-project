# Coffee Shop Database Management

This project aims to provide a simple SQLite database management system for coffee shops and beans. It includes functionalities for adding, retrieving, and deleting coffee shops and beans from the database. Additionally, it allows users to find the best preparation method for a specific coffee bean based on its rating.

## Features

- **Coffee Shop Management**: Add, retrieve, and delete coffee shops.
- **Bean Management**: Add, retrieve, and delete coffee beans.
- **Best Preparation Method**: Find the best preparation method for a specific bean based on its rating.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python main.py
    ```

## Usage

1. Initialize the database by running the script. This will create the necessary tables if they don't exist already.

2. Use the provided functions to manage coffee shops and beans in the database:
    - `add_shop()`: Add a new coffee shop.
    - `get_all_shops()`: Retrieve all coffee shops.
    - `get_shops_by_name()`: Retrieve coffee shops by name.
    - `delete_shop()`: Delete a coffee shop.
    - `add_bean()`: Add a new coffee bean.
    - `get_all_beans()`: Retrieve all coffee beans.
    - `get_beans_by_name()`: Retrieve coffee beans by name.
    - `best_preparation_for_bean()`: Find the best preparation method for a bean.
    - `delete_bean()`: Delete a coffee bean.

## Contributing

Contributions are welcome! If you have any ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
