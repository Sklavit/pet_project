
Install nvm and node

```
# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js
nvm install node --lts # install the latest LTS version of Node.js

# verifies the right Node.js version is in the environment
node -v # should print ?

# verifies the right NPM version is in the environment
npm -v # should print ?
```

```
npm install -g npm@latest
```

Install pnpm

```
npm install -g pnpm
```

Install Vite

To install Vite globally, you can use the following command:
```
npm install -g create-vite
```

After installing Vite, you can create a new project using the following command:
```
pnpm create vite web_todo --template react-ts
```

After creating the project, navigate into the project directory and install the dependencies:
```
cd my-vite-project
pnpm install
```

Start the development server:
```
pnpm dev
``` 
This will start the development server, and you can 
now open your browser to http://localhost:5173 to see your new Vite, React, and TypeScript app.

## Other popular packages to try

React Router: This is a standard library for routing in React. It enables the navigation among views of various components in a React Application, allows changing the browser URL, and keeps the UI in sync with the URL.  
Redux: This is a predictable state container for JavaScript apps. It helps you write applications that behave consistently, run in different environments (client, server, and native), and are easy to test.
Styled Components: This library allows you to use component-level styles in your application that are written with a mixture of JavaScript and CSS.  
React Query: It's a data fetching library for React that provides hooks to fetch, cache and update asynchronous data in your React applications.  
Formik: It's a small library that helps with handling form state, input validation, and form submission in React.  
Material-UI: A popular UI framework for React that implements Google's Material Design.  
Ant Design: Another UI library that provides a set of high-quality React components out of the box.  
React Testing Library: A very light-weight solution for testing React components. It provides light utility functions on top of react-dom and react-dom/test-utils, in a way that encourages better testing practices.  
Remember to install these libraries using your package manager (like npm or pnpm) and import them in your React components as needed.

# Installing "emotion" with support of react and typescript

To install the "emotions" package with TypeScript support, you need to install the package itself and its TypeScript definitions. 


1. First, install the "emotion" package and its related packages.

```bash
pnpm add @emotion/react @emotion/styled
```

2. Next, install the TypeScript definitions for these packages:

```bash
pnpm add -D @types/emotion @types/@emotion/react @types/@emotion/styled
```

3. Finally, you can import and use "emotion" in your TypeScript files like so:

```typescript
import styled from '@emotion/styled'

const Container = styled.div`
  margin: 40px;
  border: 2px solid #282c34;
  border-radius: 10px;
`;
```


