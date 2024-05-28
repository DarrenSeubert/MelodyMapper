/******************************************************************************
 * Filename: downloadXml.test.js
 * Purpose:  Tests the downloadXml utility function.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the downloadXml utility function. The tests
 * ensure that the function correctly converts a base64 string to a Blob and
 * initiates a download of the Blob as a file in the browser. The tests mock
 * the necessary functions to prevent actual file downloads during testing.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 ******************************************************************************/

import { base64ToBlob } from "./downloadXml";
import downloadXml from "./downloadXml";
import { JSDOM } from "jsdom";

describe("base64ToBlob", () => {
  it("should return a Blob with the correct type and size", () => {
    const base64 = Buffer.from("Hello, world!", "utf-8").toString("base64"); // convert a string to base64
    const mimeType = "text/plain";
    const blob = base64ToBlob(base64, mimeType);

    expect(blob).toBeInstanceOf(Blob);
    expect(blob.size).toBe("Hello, world!".length);
    expect(blob.type).toBe(mimeType);
  });
});

describe("downloadXml", () => {
  let createElementSpy;
  let appendChildSpy;
  let removeChildSpy;
  let clickSpy;

  beforeEach(() => {
    // Create a new JSDOM instance before each test
    const { window } = new JSDOM();
    global.window = window;
    global.document = window.document;
    global.URL = window.URL;

    // Mock the necessary functions
    global.URL.createObjectURL = jest.fn(() => "blob:mocked");
    createElementSpy = jest
      .spyOn(document, "createElement")
      .mockImplementation(() => ({
        click: (clickSpy = jest.fn()),
      }));
    appendChildSpy = jest
      .spyOn(document.body, "appendChild")
      .mockImplementation(() => {});
    removeChildSpy = jest
      .spyOn(document.body, "removeChild")
      .mockImplementation(() => {});
  });

  afterEach(() => {
    // Clean up the mocks after each test
    createElementSpy.mockRestore();
    appendChildSpy.mockRestore();
    removeChildSpy.mockRestore();
    global.URL.createObjectURL.mockRestore();

    global.window = undefined;
    global.document = undefined;
    global.URL = undefined;
  });

  it("creates a blob and initiates a download", () => {
    // Use a valid base64 string
    const dataBase64 = "SGVsbG8sIHdvcmxkIQ=="; // 'Hello, world!' in base64
    const filename = "test.xml";

    downloadXml(dataBase64, filename);

    // Check that functions for creating and removing elements were called
    expect(global.URL.createObjectURL).toHaveBeenCalled();
    expect(createElementSpy).toHaveBeenCalledWith("a");
    expect(appendChildSpy).toHaveBeenCalled();
    expect(clickSpy).toHaveBeenCalled();
    expect(removeChildSpy).toHaveBeenCalled();
  });
});
