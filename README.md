Project Aleksandria
===============

Simple project to register users on courses.

```mermaid
classDiagram
Course --|> User : author
Enrollment --|> User
Enrollment --|> Course
Review --|> User : user
Review --|> Course : course