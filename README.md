# NotificationService
This project refers to the coding exercise for the selection process at Modak. The project is a service responsible for sending emails to people, with a spam limit.

## Technical Choices

#### Development Language
The chosen development language was Python due to its simplicity, integration capabilities, and wide range of available libraries. Additionally, the developer responsible for the project has proficiency in Python.

#### Programming Paradigm
Although Python is commonly used in functional programming, this project was developed following Object-Oriented Programming (OOP) principles, such as SOLID, ensuring easy maintenance and scalability of the code.

#### Project Architecture
The project architecture is based on Clean Architecture but also incorporates some practices from Hexagonal Architecture to handle interactions with external components.

The project is divided into the following layers:

- _Domain entities layer_, which contains the email type definitions, for example.
- _Application layer_, which contains the service responsible for sending emails, for example.
- _Infrastructure layer_, which contains the adapter for the gateway, for example.

This architecture was chosen to provide benefits in terms of maintainability, scalability, and system adaptability to changes in external requirements and technologies.

#### Code Organization and Quality
To assist in the development, Github was used as the code review control system.

To ensure good code readability and adherence to programming standards, the main linters in the market were used: flake8, mypy, black, isort, autoflake, and pylint.

To assist in Pull Request reviews, a Git pipeline was configured to evaluate the code with these linters.

#### Development Environment
Docker + Poetry was used to develop the project, as Docker ensures a consistent and isolated environment for development, while Poetry simplifies dependency management for the application.

#### Libraries Used:

- pydantic: A library that helps define data models (such as entities), offering data validation, easy serialization, easy deserialization, and optimized performance.
- unittest: A testing library that has native integration, mocks, etc.

#### Project Execution
To run the project, it is recommended to use Docker. The step-by-step instructions for executing the project are very simple.
