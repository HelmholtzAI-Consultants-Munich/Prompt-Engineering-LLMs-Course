## Exercise (just for fun): Create Your Own Web Based Game

Use an LLM to create your own web-based game (something classic like snake). To simplify things, ask the LLM to put everything (HTML, CSS and JavaScript) into the same file (see Basic structure of an HTML file if you don't know anything about HTML).

Note: CSS and JavaScript are typically placed in separate files and linked to the HTML. However, for simplicity in this exercise, we include everything in one file.

### Basic structure of an HTML file

#### HTML (HyperText Markup Language): 
It provides the basic structure of your webpage, and has several "sections"
`<html>`: The root element that contains all the content of the webpage."
`<head>`: Contains meta-information, such as the title and linked resources like stylesheets.
`<body>`: This is where the content of your webpage goes, including headings, text, and interactive elements.

#### Style with CSS:

CSS (Cascading Style Sheets): Defines the look and feel of the app, such as colors, layout, fonts, and animations.
You can include CSS directly in your HTML file using the `<style>` tag within the `<head>` section.


#### Add Functionality with JavaScript:

JavaScript: Adds interactivity to the app and handles its logic, user inputs, and updates the display.
You can include JavaScript in your HTML file directly using the `<script>` tag, which you can place within the `<body>` section or at the end of the `<body>`.

#### Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Game</title>
    <style>
        /* CSS here */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        canvas {
            border: 1px solid #000;
        }
    </style>
</head>
<body>

    <canvas id="gameCanvas" width="400" height="400"></canvas>

    <script>
        // JavaScript here
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        // Game logic, controls, and drawing code goes here

    </script>
</body>
</html>
```