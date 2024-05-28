# Frontend Testing (React)

## Running Tests

1. Navigate to `/client` directory

2. Run `npm test test --env=jsdom --coverage --collectCoverageFrom='src/**/*.{js,jsx}'`

- When running this command, Jest starts in an interactive watch mode which automatically re-runs tests whenever it detects a change in your files. This is extremely useful during development as it provides instant feedback on whether your changes have broken any existing functionality. This command also collects code coverage information.

In addition to running your tests, Jest also provides a number of useful features such as:

- A comprehensive assertion library for validating test results
- Mocking and spy functionalities
- Snapshot testing for capturing and comparing UI changes
- Code coverage reports

For more information on Jest and its features, refer to the [official Jest documentation](https://jestjs.io/).

## How Tests are Organized in This Project:

In this project, tests are organized alongside their respective components. This means that for each component in the project, there is a corresponding test file in the same directory.

For example, if there is a component `FileUpload.jsx` in the `components` directory, the test file for this component would be `FileUpload.test.js` and it would be located in the same `components` directory.

This structure makes it easy to find the tests related to a specific component. It also encourages the development of tests alongside the component development, as the tests are always visible and accessible.

## Arrange, Act, Assert (AAA) Pattern

The Arrange, Act, Assert (AAA) pattern is a common way of writing unit tests for a method or function. It clearly separates what is being tested into three distinct sections:

- **Arrange**: All necessary preconditions and inputs are established. In the context of a React component, this could involve rendering the component with specific props or setting up a user event (like a click or a change event).

- **Act**: On the object or method under test. In the context of a React component, this could involve simulating user interactions or lifecycle methods, or triggering some other action that will change the state of the component. For tests that just check if an element renders on component load, this step can be omitted.

- **Assert**: That the expected results have occurred. In the context of a React component, this could involve checking that certain text is displayed, that certain callbacks were called, or that the component's state has changed as expected.

Here is an example from a test case in `SecurityStatement.test.js`:

```javascript
test("should close security statement when document is clicked", () => {
  // Arrange
  render(<SecurityStatement />); // Render the component

  // Act
  const securityStatementElement = screen.getByTestId(
    "security-statement-overlay",
  );
  act(() => {
    window.dispatchEvent(new MouseEvent("click")); // Simulates click event on window
  });

  // Assert
  expect(securityStatementElement).not.toBeInTheDocument();
});
```

## Snapshot Testing

- Provided by the Jest testing framework.

- Useful for catching unintended changes in your component's structure or behavior.

- Allows us to take "snapshot" of a component's output and save it to a file to check that the output of your component hasn't changed unexpectedly.

- It's typically used for components that have a large amount of markup, to avoid manually writing assertions for every element.

- However, it's not a replacement for other types of testing like unit or integration tests. It's best used in combination with these other tests to provide complete coverage.

Here is an example of a snapshot test from `SecurityStatement.test.js`:

```javascript
// Snapshot testing which compares the rendered component with a saved snapshot found in ./__snapshots__.
test("matches snapshot", () => {
  const tree = renderer.create(<SecurityStatement />).toJSON();
  expect(tree).toMatchSnapshot();
});
```

### Snapshot Location & Updating Snapshots:

- In this project, snapshot files are stored in a `__snapshots__` directory within the same directory as the component being tested. When a snapshot test is run for the first time, Jest creates a snapshot file in this directory. This file contains the output of the component's render method.

- For example, if you have a snapshot test for the `SecurityStatement` component in `SecurityStatement.test.js`, Jest will create a snapshot file named `SecurityStatement.test.js.snap` in the `__snapshots__` directory. This file will contain the output of the `SecurityStatement` component's render method.

- Subsequent test runs will compare the component's current output with the output stored in the snapshot file. If the outputs do not match, the test will fail. This helps catch unintended changes to the component's structure or behavior.

- To update the snapshot file, you can run your tests with the `-u` or `--updateSnapshot` flag. This will generate a new snapshot file based on the component's current output.

## Resource Links:

- [React Testing Tutorial](https://youtu.be/ML5egqL3YFE?si=sadG6u8fTjhvJE5b)
- [Guide to Testing React Components](https://www.freecodecamp.org/news/testing-react-hooks/)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro)
- [JEST (JavaScript) Testing](https://jestjs.io/)
